import matplotlib.pylab as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

def sl():
    iris = load_iris()

    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

    iris_df = pd.DataFrame(x_train, columns=iris.feature_names)

    plt.figure(figsize=(10, 10))
    plt.plot(iris_df)
    plt.show()

def tf():
    x_data = [1, 2, 3, 4, 5]
    y_data = [6, 7, 8, 9, 10]

    w = tf.Variable(0.7)  # Weight
    b = tf.Variable(0.7)  # Bias
    learn_rate = 0.01  # 학습률

    print(' step|    w|    b| cost')
    print('-----|-----|-----|-----')

    for i in range(1, 1101):
        with tf.GradientTape() as tape:
            hypothesis = w * x_data + b
            cost = tf.reduce_mean((hypothesis - y_data) ** 2)
        dw, db = tape.gradient(cost, [w, b])

        w.assign_sub(learn_rate * dw)
        b.assign_sub(learn_rate * db)

        if i in range(1101):
            print(f' {i:4d}| {w.numpy():.2f}| {b.numpy():.2f}| {cost:.2f}')
            plt.figure(figsize=(7, 7))
            plt.title(f'[Step {i:d}] h(x) = { w.numpy():.2f}x + {b.numpy():.2f}')
            plt.plot(x_data, y_data, 'o')
            plt.plot(x_data, w * x_data + b, 'r', label='hypothesis')
            plt.xlabel('x_data')
            plt.ylabel('y_data')
            plt.xlim(0, 6)
            plt.ylim(1, 7)
            plt.legend(loc='best')
            plt.show()
