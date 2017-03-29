"""
Imported into the main program to help it graph data.
"""

import matplotlib.dates as mdate
import matplotlib.pyplot as plt


# This is the basic plot - finished. Only one that is currently finished and in use
def three_plots(x, y1, y2, y3, title, xlabel, ylabel1, ylabel2, ylabel3, save_file):
    """
    Made three subplots for the data
    :param x:
    :param y1:
    :param y2:
    :param y3:
    :param title:
    :param ylabel1:
    :param ylabel2:
    :param ylabel3:
    :return:
    """
    # Subplot 1

    fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

    ax1 = plt.subplot(3, 1, 1)
    plt.plot(x, y1)
    plt.ylabel(ylabel1)
    plt.setp(ax1.get_xticklabels(), visible=False)

    # Subplot 2
    ax2 = plt.subplot(3, 1, 2)
    plt.plot(x, y2)
    plt.ylabel(ylabel2)
    plt.setp(ax2.get_xticklabels(), visible=False)

    # Subplot 3
    ax3 = plt.subplot(3, 1, 3)
    plt.plot(x, y3)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel3)

    # use to add text to figure image
    # fig.text(0, 0, 'Note the spikes around 1am appear to be from hail hitting the box. Not likely to be\n'
    # 'due to wind as the inconsistency coincides with reported hail')

    # Adjust the x-axis to look nice
    fig.suptitle(title)

    xfmt = mdate.DateFormatter('%H:%M')  # this is what make the x-axis format correctly
    ax3.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()  # This works alright

    plt.savefig(save_file)
    plt.show()

def single_plot(x, y, title, xlabel, ylabel, save_file):
    fig = plt.figure()
    ax1 = plt.subplot(1, 1, 1)

    ax1.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    xfmt = mdate.DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()

    plt.savefig(save_file)
    plt.show()




# Not finished - see official vs unofficial data comparison for example of this type
def overlay_two(x, y1, y2, title, ylabel1, ylabel2, save_file=False):
    """

    :param x:
    :param y1:
    :param y2:
    :param title:
    :param ylabel1:
    :param ylabel2:
    :param save_file:
    :return:
    """


def histogram(data, bins, title, ylabel, save_file=False):
    """

    :param data:
    :param bins:
    :param title:
    :param ylabel:
    :param save_file:
    :return:
    """


def correlation_histogram(x, y, title, xlabel, ylabel, save_file=False):
    """
    2D historgram chart
    :param x:
    :param y:
    :param title:
    :param xlabel:
    :param ylabel:
    :param save_file:
    :return:
    """


def correlation_scatter(x, y, title, xlabel, ylabel):
    """
    2D scatter plot with trend line possibly
    :param x:
    :param y:
    :param title:
    :param xlabel:
    :param ylabel:
    :return:
    """
