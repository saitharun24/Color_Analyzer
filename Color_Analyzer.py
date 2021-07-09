# Importing the required packages
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse

# Converting the RGB color into it's respective hex code
def rgb_hex(rgb):
    hex = "#"
    for i in rgb:
        i = int(i)
        hex += ("{:02x}".format(i))
    return hex

# Preprocessing the image for ensuring proper color recognition
def prep_img(img):
    modified_img = cv2.resize(img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
    return modified_img

# Performing KMeans clustering to segregate the colors from the given image and plotting it as a pie chart
def color_analysis(img):
    clf = KMeans(n_clusters=5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_

    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex = [rgb_hex(ordered_colors[i]) for i in counts.keys()]

    # Plotting the obtained hex values as a pie chart
    plt.pie(counts.values(), labels=hex, colors=hex)
    plt.axis('off')
    plt.title("Color Scheme")
    plt.savefig("color_analysis_report.png")
    # print(hex)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the colour scheme of your image')

    # Command line argument to take the filename of the image and to print both the image and scheme or only the scheme
    parser.add_argument('filename', type=str, help='Enter the filename of your target image')
    parser.add_argument('--s', nargs='*', default=False,
                        help='Specifies if you want the image and color scheme or the color scheme only. Leave blank in case you want both the picture and colour scheme else type --s after the arguments for colour scheme only')

    args = parser.parse_args()
    filename = args.filename
    if vars(args).get('s', False) is not False:
        if not args.s:
            args.s = True

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Plotting the image if the user wats the image along with the scheme
    if args.s:
        plt.figure(figsize=(10, 8))
    else:
        fig = plt.figure(figsize=(14, 6))
        fig.add_subplot(1, 2, 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title("Image")
        fig.add_subplot(1, 2, 2)

    # Calling the function prep_img that preprocesses the image
    modified_img = prep_img(img)

    # Calling the function color_analysis that gets the color scheme from the image
    color_analysis(modified_img)
