from skimage.io import imread, imsave

def read_image(path, isgray=False):
    """
    Reads an image from a path.
    """
    image = imread(path, as_gray=isgray)
    return image

def save_image(image, path):
    """
    Saves an image to a path.
    """
    imsave(path, image)