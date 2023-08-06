import numpy as np
import os
from collections import Counter


def plot_keras_history(history, name='', acc='acc'):
    """Plots keras history."""
    import matplotlib.pyplot as plt

    try:
        training_acc = history.history[acc]
        validation_acc = history.history['val_' + acc]
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs = range(len(training_acc))

        plt.ylim(0, 1)
        plt.plot(epochs, training_acc, 'tab:blue', label='Training acc')
        plt.plot(epochs, validation_acc, 'tab:orange', label='Validation acc')
        plt.title('Training and validation accuracy  ' + name)
        plt.legend()

        plt.figure()

        plt.plot(epochs, loss, 'tab:green', label='Training loss')
        plt.plot(epochs, val_loss, 'tab:red', label='Validation loss')
        plt.title('Training and validation loss  ' + name)
        plt.legend()
        plt.show()
        plt.close()
        return training_acc, validation_acc
    except KeyError:
        # When validation_split is not used, do this:
        training_acc = history.history[acc]
        loss = history.history['loss']

        epochs = range(len(training_acc))

        plt.ylim(0, 1)
        plt.plot(epochs, training_acc, label='Training acc', c='tab:blue')
        plt.plot(epochs, loss, label='Training loss', c='tab:orange')
        plt.title('Training accuracy and training loss  ' + name)
        plt.legend()
        plt.show()
        plt.close()
        return training_acc


def plot_history_df(history, path, name='', acc='acc'):
    """Plots keras history."""
    import matplotlib.pyplot as plt
    import os

    training_acc = history[acc]
    validation_acc = history['val_' + acc]
    loss = history['loss']
    val_loss = history['val_loss']

    epochs = range(len(training_acc))

    plt.ylim(0, 1)
    plt.plot(epochs, training_acc, 'tab:blue', label='Training acc')
    plt.plot(epochs, validation_acc, 'tab:orange', label='Validation acc')
    plt.title('Training and validation accuracy ' + name)
    plt.legend()
    plt.savefig(os.path.dirname(path) + '/history_acc.pdf')
    # plt.show()
    plt.close()

    plt.figure()

    plt.plot(epochs, loss, 'tab:green', label='Training loss')
    plt.plot(epochs, val_loss, 'tab:red', label='Validation loss')
    plt.title('Training and validation loss ' + name)
    plt.legend()
    plt.savefig(os.path.dirname(path) + '/history_loss.pdf')
    # plt.show()
    plt.close()
    return training_acc, validation_acc


def plot_confusion_matrix(cm,
                          target_names,
                          path='',
                          title='Confusion Matrix',
                          cmap=None,
                          normalize=True,
                          fname='/confusion-matrix.pdf'):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    fname:        filename.

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure()  # figsize=(4, 3.33))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True class')
    plt.xlabel('Predicted class\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.savefig(path + fname, bbox_inches='tight')
    # plt.show()
    plt.close()


def do_cm(x_val: np.ndarray,
          y_val: np.ndarray,
          model,
          perform_per_sample_majority_vote: bool = False,
          val_sample_origin: bool = False,
          perform_majority_vote: bool = False):
    from sklearn.metrics import classification_report, confusion_matrix

    assert isinstance(x_val, np.ndarray), 'Param `X` must be np.ndarray but is ' + str(type(x_val))
    assert isinstance(y_val, np.ndarray), 'Param `Y_labels` must be np.ndarray but is ' + str(type(y_val))

    assert x_val.shape[0] == y_val.shape[0]

    # Confusion Matrix and Classification Report
    y_pred = model.predict(x_val, y_val, x_val, y_val, y_val, return_df_metrics=False)
    y_val = np.argmax(y_val, axis=1)
    cm = confusion_matrix(y_val, y_pred)

    with open(os.path.dirname(model.output_directory) + '/classification-report.txt', 'w') as f:
        f.write('Classification Report\n')
        f.write(classification_report(y_val, y_pred))
    plot_confusion_matrix(cm, set(y_val), os.path.dirname(model.output_directory), normalize=False)

    assert perform_per_sample_majority_vote is False or \
           perform_majority_vote is False, 'perform_per_sample_majority_vote and _perform_majority_vote cannot both be active in do_cm()!'

    if perform_per_sample_majority_vote:
        cm_lst = np.zeros(np.array(cm).shape).tolist()
        val_sample_origin_np = np.array(val_sample_origin)

        for sample_id in set(val_sample_origin_np.flatten()):  # loop over all existing sample origin id's
            indices = np.where(val_sample_origin_np == sample_id)[0]  # find all indices that belong to some sample
            majority_vote_pred = Counter(y_pred[indices].tolist()).most_common()[0][
                0]  # find the sample that was most commonly predicted
            ground_truth = Counter(y_val[indices].tolist()).most_common()  # find ground truth for current segment
            assert len(ground_truth) == 1  # check that ground truth really exists only once for all slices
            ground_truth = ground_truth[0][0]  # determine ground truth label

            cm_lst[ground_truth][majority_vote_pred] += 1  # increment confusion matrix at correct cell

        fname = model.output_directory.replace(os.sep, '_')
        plot_confusion_matrix(np.array(cm_lst), set(y_val),
                              path=os.path.dirname(model.output_directory),
                              fname=f'/confusion-matrix-per-sample-vote-normalized.pdf')
        plot_confusion_matrix(np.array(cm_lst).astype(int), set(y_val),
                              normalize=False,
                              path=os.path.dirname(model.output_directory),
                              fname=f'/confusion-matrix-per-sample-vote-nonnormalized.pdf')
        with open(f'{os.path.dirname(model.output_directory)}/confusion-matrix-per-sample-vote-nonnormalized.txt',
                  'w') as f:
            f.write(np.array2string(np.array(cm_lst).astype(int)))

    if perform_majority_vote:
        assert False, 'perform_majority_vote has been disabled.'
        reduced_cm = []
        if perform_majority_vote:
            for line in cm:
                # we first see how long the current line is
                # then we add zeros to a reduced_cm
                # then we determine the relative majority and set this one to '1'
                # => relative majority vote
                line_len = len(line)  # check length of current line
                reduced_cm.append([0] * line_len)  # add zeros to fit the line length
                reduced_cm[-1][np.argmax(line)] = 1  # find argmax of line and set it to '1'
        reduced_cm_arr = np.array(reduced_cm)  # create np array
        plot_confusion_matrix(reduced_cm_arr,
                              set(y_val),
                              path=os.path.dirname(model.output_directory),
                              normalize=False,
                              fname='/confusion-matrix-vote.pdf')
