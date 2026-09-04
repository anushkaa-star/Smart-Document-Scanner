# Smart Document Scanner and Quality Analyzer

A Python-based Computer Vision project that automatically detects a document from an input image, corrects its perspective, enhances its readability, and evaluates the quality of the scanned document.

## Project Overview

The Smart Document Scanner processes a document photograph using computer vision techniques.

The system performs the following steps:

1. Validates the input image.
2. Loads and preprocesses the image.
3. Detects edges in the image.
4. Detects the document region.
5. Applies perspective transformation to straighten the document.
6. Enhances the scanned document for better readability.
7. Analyzes document quality using blur and brightness measurements.
8. Generates a JSON quality report.
9. Saves all processed results in the output directory.

## Features

- Input image validation
- Document boundary detection
- Edge detection
- Perspective correction
- Document enhancement
- Blur quality analysis
- Brightness analysis
- Automatic quality report generation
- Command-line execution
- Automated input validation tests

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- Python unittest

## Project Structure

```text
Smart-Document-Scanner/
│
├── docs/
│
├── input/
│   └── document.jpg
│
├── output/
│   ├── detected_document.jpg
│   ├── edges.jpg
│   ├── enhanced_document.jpg
│   ├── scanned_document.jpg
│   └── quality_report.json
│
├── src/
│   ├── main.py
│   ├── preprocessing.py
│   ├── document_detection.py
│   ├── perspective.py
│   ├── enhancement.py
│   ├── quality_analysis.py
│   ├── quality_report.py
│   └── validation.py
│
├── tests/
│   └── test_validation.py
│
├── .gitignore
├── requirements.txt
└── README.md
````

## Requirements

The project requires:

* Python 3.13.1 or compatible Python 3.x version
* pip
* OpenCV
* NumPy
* Matplotlib

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project directory

```bash
cd Smart-Document-Scanner
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If the virtual environment is already active, this step can be skipped.

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Input Image

Place the document image inside the `input` directory.

For example:

```text
input/document.jpg
```

The project accepts common image formats supported by the input validation module.

## Running the Project

Run the following command from the project root:

```bash
python src/main.py --input input/document.jpg
```

The output directory is automatically created if it does not already exist.

A custom output directory can also be specified:

```bash
python src/main.py --input input/document.jpg --output results
```

## Command-Line Arguments

### `--input`

Specifies the path of the input document image.

Example:

```bash
python src/main.py --input input/document.jpg
```

This argument is required.

### `--output`

Specifies the directory where processed files will be saved.

Example:

```bash
python src/main.py --input input/document.jpg --output output
```

This argument is optional.

If it is not specified, the default output directory is:

```text
output/
```

## Processing Pipeline

The project follows this computer vision pipeline:

```text
Input Image
     |
     v
Input Validation
     |
     v
Image Preprocessing
     |
     v
Edge Detection
     |
     v
Document Detection
     |
     v
Perspective Transformation
     |
     v
Document Enhancement
     |
     v
Quality Analysis
     |
     v
Quality Report
     |
     v
Output Files
```

## Output Files

After successful execution, the following files are generated:

### `scanned_document.jpg`

Contains the document after perspective transformation.

The transformation corrects the orientation and perspective of the detected document.

### `enhanced_document.jpg`

Contains the enhanced grayscale version of the scanned document.

The enhancement improves contrast and readability while preserving document details.

### `detected_document.jpg`

Contains the original image with the detected document boundary highlighted.

This output helps visualize the document detection stage.

### `edges.jpg`

Contains the edge-detected representation of the input image.

This output helps visualize the edge detection stage used during document detection.

### `quality_report.json`

Contains the document quality analysis results.

Example:

```json
{
    "blur_score": 1454.24,
    "brightness": 194.84,
    "messages": [
        "Document quality looks good."
    ]
}
```

The values in this file are generated automatically by the program.

## Document Quality Analysis

The project evaluates the scanned document using image quality measurements including:

### Blur Score

The blur score is used to estimate image sharpness.

A higher value generally indicates stronger image detail and lower blur.

### Brightness

Brightness is measured to determine whether the document image has an appropriate lighting level.

### Quality Messages

The system generates status messages based on the calculated quality measurements.

## Testing

The project includes automated tests for input validation.

Run the tests from the project root:

```bash
python -m unittest tests/test_validation.py
```

The tests verify:

* A valid image path is accepted.
* A missing image produces a `FileNotFoundError`.
* An unsupported file format produces a `ValueError`.

A successful test execution should display:

```text
Ran 3 tests

OK
```

## Error Handling

The application validates input before processing.

For example, if an invalid input path is provided:

```bash
python src/main.py --input input/not_found.jpg
```

The application displays an error message instead of attempting to process the missing file.

Example:

```text
Error: Input file not found: input/not_found.jpg
```

## Reproducibility

The project uses a `requirements.txt` file to specify the required Python dependencies.

After activating the virtual environment, all dependencies can be installed using:

```bash
pip install -r requirements.txt
```

The complete project can then be executed from the command line using:

```bash
python src/main.py --input input/document.jpg
```

## Future Improvements

Possible future improvements include:

* Support for multiple document images
* Automatic document orientation detection
* Improved document boundary detection for difficult backgrounds
* OCR-based text extraction
* PDF generation
* Additional image quality metrics
* Support for batch document processing

## Author

Developed as a Computer Vision course project.

```

### Bas itna karo ab ❤️

1. **Poora code block copy karo**
2. `README.md` mein paste karo
3. **Ctrl + S**
4. Abhi GitHub pe kuch upload/change mat karna.

