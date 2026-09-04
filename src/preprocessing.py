import cv2


def load_image(image_path):
    """Load an image from the given path."""
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    return image


def preprocess_image(image):
    """Convert image to grayscale and reduce noise."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    return gray, blurred