import cv2
import numpy as np


def detect_edges(blurred_image):
    """Detect edges in the preprocessed image."""
    edges = cv2.Canny(blurred_image, 30, 100)

    kernel = np.ones((5, 5), np.uint8)

    edges = cv2.morphologyEx(
        edges,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    return edges


def find_document_contour(image):
    """Detect the largest bright rectangular document region."""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Separate the bright paper from the darker background
    _, binary = cv2.threshold(
        gray,
        170,
        255,
        cv2.THRESH_BINARY
    )

    # Fill small gaps caused by notebook lines and shadows
    kernel = np.ones((15, 15), np.uint8)

    binary = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=4
    )

    binary = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    image_area = image.shape[0] * image.shape[1]

    candidates = []

    for contour in contours:
        area = cv2.contourArea(contour)

        # Ignore small regions
        if area < image_area * 0.15:
            continue

        perimeter = cv2.arcLength(contour, True)

        if perimeter == 0:
            continue

        approximation = cv2.approxPolyDP(
            contour,
            0.04 * perimeter,
            True
        )

        if len(approximation) != 4:
            continue

        if not cv2.isContourConvex(approximation):
            continue

        candidates.append(
            (area, approximation)
        )

    if not candidates:
        return None

    candidates.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return candidates[0][1]