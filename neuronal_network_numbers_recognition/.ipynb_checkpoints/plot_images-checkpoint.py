import matplotlib.pyplot as plt
import numpy as np


def plot_number(image):
    plt.imshow(image.squeeze(), cmap=plt.get_cmap('gray'))
    plt.axis('off')
    plt.show()


def plot_random_image(data, label):
    random_index = np.random.randint(len(data))
    print(f"This image repsent a: {label[random_index]}")
    plot_number(data[random_index])