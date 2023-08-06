import numpy as np
import os
import pandas as pd
import random
import sys
import tensorflow
import time
from tensorflow.python.framework.errors_impl import ResourceExhaustedError, InternalError, UnknownError
from tqdm import tqdm

import useckit.models
from useckit.deeplearning import unison_shuffle_np_arrays_3, enable_gpu_growth, force_cpu_training, \
    unison_shuffle_np_arrays, create_ohc_labels
from useckit.plotting import do_cm, plot_history_df


class AutoEvaluator:
    def __init__(self,
                 x_train: np.ndarray,  # training data (mandatory)
                 y_train: np.ndarray,  # training labels (mandatory)
                 x_val: np.ndarray,  # validation data (mandatory)
                 y_val: np.ndarray,  # validation labels (mandatory)
                 nb_classes: int,  # number of classes (mandatory)
                 custom_name: str = '',
                 input_shape: tuple = None,
                 base_output_directory: str = '_useckit_out',
                 verbose: int = 0,
                 enable_window_slicing=False,
                 window_stride=None,
                 window_size=None,
                 seed=42,
                 kcrossvalidation_k=None,
                 disable_normalization_check=False,
                 shuffle_window_slices=True,
                 epochs=None,
                 class_weights=None,
                 enable_cnn=True,
                 enable_encoder=True,
                 enable_fcn=True,
                 enable_inception=True,
                 enable_mcdcnn=True,
                 enable_mcnn=True,
                 enable_mlp=True,
                 enable_resnet=True,
                 enable_tlenet=True,
                 enable_twiesn=True,
                 ):
        if not isinstance(x_train, np.ndarray):
            raise TypeError("x_train-parameter is of type " + str(type(x_train)) + ". Expected np.ndarray.")

        if not isinstance(y_train, np.ndarray):
            raise TypeError("y_train-parameter is of type " + str(type(y_train)) + ". Expected np.ndarray.")

        if not isinstance(x_val, np.ndarray):
            raise TypeError("x_val-parameter is of type " + str(type(x_val)) + ". Expected np.ndarray.")

        if not isinstance(y_val, np.ndarray):
            raise TypeError("y_val-parameter is of type " + str(type(y_val)) + ". Expected np.ndarray.")

        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.nb_classes = nb_classes

        for idx, _y_ohc in enumerate(y_train):
            if sum(_y_ohc) != 1:
                raise ValueError(
                    'y_train has OHC-vectors in it that are not one-hot-encodings, i.e., either many-hot-encodings'
                    ' or zero-hot-encodings. This is currently not supported: ' + str(_y_ohc) + ' at idx ' + str(idx))

        for idx, _y_ohc in enumerate(y_val):
            if sum(_y_ohc) != 1:
                raise ValueError(
                    'y_val has OHC-vectors in it that are not one-hot-encodings, i.e., either many-hot-encodings'
                    ' or zero-hot-encodings. This is currently not supported: ' + str(_y_ohc) + ' at idx ' + str(idx))

        # sanitize parameters
        if np.isnan(x_train).any():
            raise ValueError('Critical: `x_train` contains NaN values!')
        if np.isnan(x_val).any():
            raise ValueError('Critical: `x_val` contains NaN values!')
        if not disable_normalization_check:
            train_max, train_min = np.amax(x_train), np.amin(x_train)
            val_max, val_min = np.amax(x_val), np.amin(x_val)
            if train_max > 1:
                raise ValueError('Critical: `x_train` contains maximum value ' + str(train_max))
            if val_max > 1:
                raise ValueError('Critical: `val_max` contains maximum value ' + str(val_max))
            if train_min < -1:
                raise ValueError('Critical: `train_min` contains minimum value ' + str(train_min))
            if val_min < -1:
                raise ValueError('Critical: `val_min` contains minimum value ' + str(val_min))

        self.shape = None

        if enable_window_slicing:
            if window_stride is None:
                raise TypeError('window_stride must not be None if window slicing is used.')

            if window_size is None:
                raise TypeError('window_size must not be None if window slicing is used.')

            self.x_train, self.y_train, self.train_sample_origin = self._create_slices(x_train,
                                                                                       y_train,
                                                                                       window_stride,
                                                                                       window_size,
                                                                                       shuffle=shuffle_window_slices)
            self.x_val, self.y_val, self.val_sample_origin = self._create_slices(x_val,
                                                                                 y_val,
                                                                                 window_stride,
                                                                                 window_size,
                                                                                 shuffle=shuffle_window_slices)

        self.base_output_directory = base_output_directory + ('' if custom_name == '' else '_' + custom_name + '_')

        self.complete_history_df = None

        self.enable_cnn = enable_cnn
        self.enable_encoder = enable_encoder
        self.enable_fcn = enable_fcn
        self.enable_inception = enable_inception
        self.enable_mcdcnn = enable_mcdcnn
        self.enable_mcnn = enable_mcnn
        self.enable_mlp = enable_mlp
        self.enable_resnet = enable_resnet
        self.enable_tlenet = enable_tlenet
        self.enable_twiesn = enable_twiesn

        self.enable_window_slicing = enable_window_slicing

        self.verbose = verbose

        self.base_dir_created = False

        self.seed = seed

        if input_shape is None:
            self.input_shape = self.x_train.shape[1:]
        else:
            self.input_shape = input_shape

        if kcrossvalidation_k is not None:
            raise NotImplementedError("kcrossvalidation_k is not implemented yet.")

        self.epochs = epochs
        if class_weights is not None:
            assert isinstance(class_weights, dict), 'class_weights must be a dict. See: https://bit.ly/3ljOI9c'
        self.class_weights = class_weights

    @staticmethod
    def _create_slices(data: np.ndarray,
                       labels: np.ndarray,
                       stride: int,
                       slice_size: int,
                       shuffle: bool = True) -> [np.ndarray, np.ndarray]:
        if not data.shape[0] == labels.shape[0]:
            raise TypeError("Error in AutoEvaluator::_create_slices(). Data and Labels differ in size.")

        if not len(data.shape) <= 3:
            raise TypeError("Error in AutoEvaluator::_create_slices(). Dimension not supported.")

        ret_sliced_data, ret_sliced_labels, ret_sample_origin = [], [], []

        for sample_id, (array, label) in enumerate(zip(data, labels)):
            array_slices, label_slices, sample_origin = [], [], []

            lost_samples_cnt, added_cnt = 0, 0

            for step_idx in range(0, array.shape[0], stride):
                arr = array[step_idx:step_idx + slice_size]

                if not arr.any():
                    pass  # do not append if slice consists only of zero
                else:
                    array_slices.append(arr)
                    label_slices.append(label)
                    sample_origin.append(sample_id)

            for i in range(len(array_slices)):
                if array_slices[i].shape == array_slices[0].shape:
                    ret_sliced_data.append(array_slices[i])
                    ret_sliced_labels.append(label_slices[i])
                    ret_sample_origin.append(sample_origin[i])
                    added_cnt += 1
                else:
                    lost_samples_cnt += 1

            if not all(s.shape == array_slices[0].shape for s in array_slices):
                print('Warning: `slices` array created in AutoEvaluator::_create_slices() is ragged. '
                      'Check parameters stride, slice_size and shape of array. Lost',
                      lost_samples_cnt, 'samples and created', added_cnt,
                      'new samples. Check your slicing window settings.', file=sys.stderr)

        ret_sliced_data_np = np.array(ret_sliced_data)
        ret_sliced_labels_np = np.array(ret_sliced_labels)
        sample_origin_np = np.array(ret_sample_origin)

        print('Info: Slicing window data consumes', round(ret_sliced_data_np.nbytes / 1024 / 1024, 2), 'mb.',
              file=sys.stderr)

        # TODO check that supressing null arrays does not result in a skewed data set

        if shuffle:
            return unison_shuffle_np_arrays_3(ret_sliced_data_np, ret_sliced_labels_np, sample_origin_np)
        else:
            return ret_sliced_data_np, ret_sliced_labels_np, sample_origin_np

    def _construct_all_models(self) -> list:
        if not isinstance(self.input_shape, tuple):
            raise TypeError("input_shape-parameter is of type " + str(type(self.input_shape)) + ". Expected tuple.")

        if not isinstance(self.nb_classes, int):
            raise TypeError("input_shape-parameter is of type " + str(type(self.input_shape)) + ". Expected int.")

        if not isinstance(self.base_output_directory, str):
            raise TypeError(
                "base_output_directory-parameter is of type " + str(type(self.input_shape)) + ". Expected str.")

        if not isinstance(self.verbose, int):
            raise TypeError("verbose-parameter is of type " + str(type(self.input_shape)) + ". Expected int.")

        def create_subdir(nn_name, cnt=0):
            try:
                if not self.base_dir_created:
                    dir_to_create = './' + self.base_output_directory + str(cnt) + nn_name
                else:
                    dir_to_create = './' + self.base_output_directory + nn_name
                os.makedirs(dir_to_create)
                if not self.base_dir_created:
                    self.base_dir_created = True
                    self.base_output_directory = self.base_output_directory + str(cnt) + '/'
            except FileExistsError:
                create_subdir(nn_name, cnt + 1)

        def write_summary(model):
            with open(model.output_directory + '/model-summary.txt', 'w') as f:
                from contextlib import redirect_stdout
                with redirect_stdout(f):
                    try:
                        model.model.summary()
                    except AttributeError as ae:
                        print(str(ae))

        subdir_lst, models_lst = [], []

        if self.enable_cnn:
            subdir_lst.append('/cnn/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.cnn.Classifier_CNN(self.base_output_directory + subdir_lst[-1],
                                                  self.input_shape,
                                                  self.nb_classes,
                                                  verbose=self.verbose,
                                                  nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_encoder:
            subdir_lst.append('/encoder/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.encoder.Classifier_ENCODER(self.base_output_directory + subdir_lst[-1],
                                                          self.input_shape,
                                                          self.nb_classes,
                                                          verbose=self.verbose,
                                                          nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_fcn:
            subdir_lst.append('/fcn/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.fcn.Classifier_FCN(self.base_output_directory + subdir_lst[-1],
                                                  self.input_shape,
                                                  self.nb_classes,
                                                  verbose=self.verbose,
                                                  nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_inception:
            subdir_lst.append('/inception/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.inception.Classifier_INCEPTION(self.base_output_directory + subdir_lst[-1],
                                                              self.input_shape,
                                                              self.nb_classes,
                                                              verbose=self.verbose,
                                                              nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_mcdcnn:
            subdir_lst.append('/mcdcnn/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.mcdcnn.Classifier_MCDCNN(self.base_output_directory + subdir_lst[-1],
                                                        self.input_shape,
                                                        self.nb_classes,
                                                        verbose=self.verbose,
                                                        nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_mcnn:
            subdir_lst.append('/mcnn/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.mcnn.Classifier_MCNN(self.base_output_directory + subdir_lst[-1],
                                                    self.nb_classes,
                                                    verbose=self.verbose,
                                                    nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_mlp:
            subdir_lst.append('/mlp/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.mlp.Classifier_MLP(self.base_output_directory + subdir_lst[-1],
                                                  self.input_shape,
                                                  self.nb_classes,
                                                  verbose=self.verbose,
                                                  nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_resnet:
            subdir_lst.append('/resnet/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.resnet.Classifier_RESNET(self.base_output_directory + subdir_lst[-1],
                                                        self.input_shape,
                                                        self.nb_classes,
                                                        verbose=self.verbose,
                                                        nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_tlenet:
            subdir_lst.append('/tlenet/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.tlenet.Classifier_TLENET(self.base_output_directory + subdir_lst[-1], self.verbose,
                                                        nb_epochs=self.epochs)
            write_summary(m)
            models_lst.append(m)

        if self.enable_twiesn:
            subdir_lst.append('/twiesn/')
            create_subdir(subdir_lst[-1])
            m = useckit.models.twiesn.Classifier_TWIESN(self.base_output_directory + subdir_lst[-1], self.verbose)
            write_summary(m)
            models_lst.append(m)

        return models_lst

    @staticmethod
    def enable_gpu_growth():
        return enable_gpu_growth()

    @staticmethod
    def force_cpu_training():
        return force_cpu_training()

    def evaluate(self):
        start_time = time.time()
        all_models = self._construct_all_models()

        def reset_training(exception):
            """Tested function to retrain on CPU in case of resource allocation errors."""
            print('CRIT switching to CPU training for', str(type(model)), 'due to', str(type(exception)))
            print(exception)
            print('!  (This is not a terminal error.)')
            # backup env variable
            environ_backup_flag = False
            if 'CUDA_VISIBLE_DEVICES' in os.environ:
                env_var = os.environ['CUDA_VISIBLE_DEVICES']
                environ_backup_flag = True
            self.force_cpu_training()
            with tensorflow.device('/cpu:0'):
                model.fit(self.x_train,
                          self.y_train,
                          self.x_val,
                          self.y_val,
                          np.argmax(self.y_val, axis=1))
                if environ_backup_flag:
                    os.environ['CUDA_VISIBLE_DEVICES'] = env_var

        # fit models and plot training process
        for model in tqdm(all_models):
            self.set_seed()
            if self.verbose > 0:
                print('++ Fitting model:', str(type(model)))
            try:
                model.fit(self.x_train,
                          self.y_train,
                          self.x_val,
                          self.y_val,
                          np.argmax(self.y_val, axis=1))
            except ResourceExhaustedError as ree:
                reset_training(ree)
            except InternalError as ie:
                reset_training(ie)
            except UnknownError as ue:
                reset_training(ue)
            except RecursionError as re:
                print('++ RecursionError (err01) ENCOUNTERED IN MODEL ', str(type(model)))
                print(str(re))
                print('++ CONTINUE!')
                continue
            except ValueError as ve:
                print('++ ValueError (err03) ENCOUNTERED IN MODEL ', str(type(model)))
                print(str(ve))
                print('++ CONTINUE!')
                continue

            self.set_seed()
            if not ('Classifier_TWIESN' in str(type(model)) or 'Classifier_MCNN' in str(type(model))):
                self._plot_history(model.output_directory + '/history.csv', type(model).__name__)
            self.set_seed()
            pass  # end of training loop

            # perform predictions
            if self.verbose > 0:
                print('++ Model', str(type(model)), 'finished fit().')
            self.set_seed()
            # create a list of metrices
            # Original function has some strange handling of types that's why the parameters are this way.
            try:
                if self.enable_window_slicing:
                    do_cm(self.x_val, self.y_val, model)
                    do_cm(self.x_val, self.y_val, model, perform_per_sample_majority_vote=True)
                else:  # no window slicing here
                    do_cm(self.x_val, self.y_val, model)
            except RecursionError as re:
                print('++ RecursionError (err02) ENCOUNTERED IN MODEL ', str(type(model)))
                print(str(re))
                print('++ CONTINUE!')
                continue

            if self.verbose > 0:
                print('++ Model', str(type(model)), 'finished predictions [do_cm()].')
            pass  # end of validation

        if self.complete_history_df is not None:
            self.complete_history_df.to_csv(self.base_output_directory + '/complete_history.csv')
        print("AutoEvaluator.evaluate() took", round(time.time() - start_time, 2) / 3600, 'hours')

    def _plot_history(self, path, modelname):
        hist_df = pd.read_csv(path, dtype=np.float64)
        hist_df['epoch'] = hist_df.index
        hist_df['modelname'] = modelname

        if self.complete_history_df is None:  # in case of initialization
            self.complete_history_df = hist_df
        else:
            self.complete_history_df = self.complete_history_df.append(hist_df,
                                                                       ignore_index=True,
                                                                       verify_integrity=True)

        plot_history_df(hist_df, path, name=modelname, acc='accuracy')

    def set_seed(self):
        import tensorflow as tf
        tf.keras.backend.clear_session()
        if self.seed is not None:
            tf.random.set_seed(self.seed)
            tf.random.set_seed(self.seed)
            random.seed(self.seed)
            np.random.seed(self.seed)
            os.environ['PYTHONHASHSEED'] = str(self.seed)
            os.environ['TF_CUDNN_DETERMINISTIC'] = '1'

    @staticmethod
    def unison_shuffle_np_arrays(a: np.ndarray, b: np.ndarray):
        return unison_shuffle_np_arrays(a, b)

    @staticmethod
    def create_ohc_labels(labels_array):
        return create_ohc_labels(labels_array)
