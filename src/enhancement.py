import cv2


def enhance_document(image):
    """Enhance document readability while preserving natural appearance."""

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce small noise without destroying handwriting
    denoised = cv2.GaussianBlur(gray, (3, 3), 0)

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(denoised)

    # Light sharpening
    sharpened = cv2.addWeighted(
        enhanced,
        1.3,
        cv2.GaussianBlur(enhanced, (0, 0), 2),
        -0.3,
        0
    )

    return sharpened