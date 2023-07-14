import cv2
import matplotlib.pyplot as plt


def selectImageSection():
    # Load image
    img = cv2.imread("screenshot.png")

    # let us get the coordinates of the part we want to crop out
    # We use matplotlib to do it thus:

    # plt.imshow(img)
    # plt.show()
    # extracted coordinates are  y = (158:1085)  x = (1682:2357).

    # cropped_image = img[start_y:end_y, start_x:end_x]
    cropped_image = img[158:1085, 1682:2357]
    cv2.imwrite("output_image.png", cropped_image)  # saves the image as output_image
    cv2.imshow("output_image.png", cropped_image)  # shows the image on screen
    cv2.waitKey(5000)  # helps it stay on the screen
    cv2.destroyAllWindows()
