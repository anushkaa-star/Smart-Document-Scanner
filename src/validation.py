import os


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def validate_input(image_path):
    """Validate the input image path and file format."""

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Input file not found: {image_path}"
        )

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            "Unsupported image format. "
            "Use JPG, JPEG, or PNG."
        )

    return True