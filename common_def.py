import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os


def show_image(image_path, dpi):
    img = mpimg.imread(image_path)
    plt.figure(dpi=dpi)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def play_video(relative_path):

    absolute_path = os.path.abspath(relative_path)
    print(f"Absolute path: {absolute_path}")
    os.startfile(absolute_path)


def show_full_path(relative_path):

    absolute_path = os.path.abspath(relative_path)
    print(f"Absolute path: {absolute_path}")