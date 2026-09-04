import os
import sys
import unittest


# Allow Python to find modules inside the src folder
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from validation import validate_input


class TestInputValidation(unittest.TestCase):

    def test_valid_image(self):
        """Check that a valid image path is accepted."""
        result = validate_input("input/document.jpg")
        self.assertTrue(result)

    def test_missing_image(self):
        """Check that a missing image raises an error."""
        with self.assertRaises(FileNotFoundError):
            validate_input("input/not_found.jpg")

    def test_unsupported_format(self):
        """Check that an unsupported format raises an error."""
        with open("input/test_file.txt", "w") as file:
            file.write("test")

        try:
            with self.assertRaises(ValueError):
                validate_input("input/test_file.txt")
        finally:
            os.remove("input/test_file.txt")


if __name__ == "__main__":
    unittest.main()