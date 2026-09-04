import cv2


def calculate_blur_score(image):
    """Calculate image sharpness using Laplacian variance."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    score = cv2.Laplacian(gray, cv2.CV_64F).var()

    return round(score, 2)


def calculate_brightness(image):
    """Calculate average brightness of the image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightness = gray.mean()

    return round(brightness, 2)


def analyze_quality(image):
    """Analyze the quality of a scanned document."""
    blur_score = calculate_blur_score(image)
    brightness = calculate_brightness(image)

    quality_messages = []

    if blur_score < 100:
        quality_messages.append("Image may be blurry.")

    if brightness < 70:
        quality_messages.append("Image may be too dark.")

    if brightness > 200:
        quality_messages.append("Image may be too bright.")

    if not quality_messages:
        quality_messages.append("Document quality looks good.")

    return {
        "blur_score": blur_score,
        "brightness": brightness,
        "messages": quality_messages
    }