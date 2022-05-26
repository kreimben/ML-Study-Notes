from matplotlib import pylab as plt
from scipy import stats


def make_plot(first_data, second_data):
    linear_regress = stats.linregress(first_data, second_data)

    plt.figure(figsize=(7, 7))
    plt.plot(first_data, second_data, '.')
    plt.plot(first_data, linear_regress.slope * first_data + linear_regress.intercept, 'r')
    plt.legend(['S1 x S2', f'Y = {linear_regress.slope:.2f} * X + {linear_regress.intercept:.2f}'])
    plt.title(f'R = {linear_regress.rvalue:.2f}')
    plt.xlabel('first_data')
    plt.ylabel('second_data')
    plt.show()