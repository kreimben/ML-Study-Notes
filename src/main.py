import pandas as pd
import matplotlib.pylab as plt
from scipy import stats

s1 = pd.Series([10, -20, 30, -40, 50])
s2 = pd.Series([1, -2, 3, -4, 5])
s3 = pd.Series([-10, 20, -30, 40, -50])

df = pd.DataFrame({'S1': s1, 'S2': s2, 'S3': s3})

r12 = stats.linregress(df.S1, df.S2)
r23 = stats.linregress(df.S2, df.S3)
r13 = stats.linregress(df.S1, df.S3)


def make_plot(r, first_data, second_data):
    plt.figure(figsize=(7, 7))
    plt.plot(first_data, second_data, '.')
    plt.plot(first_data, r12.slope * df.S1 + r12.intercept, 'r')
    plt.legend(['S1 x S2', f'Y = {r.slope:.2f} * X + {r.intercept:.2f}'])
    plt.title(f'R = {r.rvalue:.2f}')
    plt.xlabel('first_data')
    plt.ylabel('second_data')
    plt.show()


make_plot(r12, df.S1, df.S2)
make_plot(r13, df.S1, df.S3)
make_plot(r23, df.S2, df.S3)