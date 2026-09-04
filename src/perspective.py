import cv2
import numpy as np


def order_points(points):
    """Arrange four points as top-left, top-right, bottom-right, bottom-left."""
    points = points.reshape(4, 2)

    ordered = np.zeros((4, 2), dtype=np.float32)

    total = points.sum(axis=1)
    difference = np.diff(points, axis=1)

    ordered[0] = points[np.argmin(total)]       # Top-left
    ordered[2] = points[np.argmax(total)]       # Bottom-right
    ordered[1] = points[np.argmin(difference)] # Top-right
    ordered[3] = points[np.argmax(difference)]  # Bottom-left

    return ordered


def perspective_transform(image, document_contour):
    """Transform the detected document into a flat top-down view."""
    points = order_points(document_contour)

    top_left, top_right, bottom_right, bottom_left = points

    width_top = np.linalg.norm(top_right - top_left)
    width_bottom = np.linalg.norm(bottom_right - bottom_left)
    max_width = int(max(width_top, width_bottom))

    height_left = np.linalg.norm(bottom_left - top_left)
    height_right = np.linalg.norm(bottom_right - top_right)
    max_height = int(max(height_left, height_right))

    destination = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(points, destination)

    warped = cv2.warpPerspective(
        image,
        matrix,
        (max_width, max_height)
    )

    return warped
