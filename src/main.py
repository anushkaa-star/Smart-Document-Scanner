import argparse
import os

from preprocessing import load_image, preprocess_image
from document_detection import detect_edges, find_document_contour
from perspective import perspective_transform
from enhancement import enhance_document
from quality_analysis import analyze_quality
from quality_report import save_quality_report
from validation import validate_input

import cv2


def main(image_path, output_dir):
    # Validate input image
    validate_input(image_path)

    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the document image
    image = load_image(image_path)

    print("Image loaded successfully!")
    print("Image dimensions:", image.shape)

    # Preprocess the image
    gray, blurred = preprocess_image(image)

    # Detect edges
    edges = detect_edges(blurred)

    # Find document contour
    document_contour = find_document_contour(image)

    if document_contour is None:
        print("No document detected.")
        return

    print("Document detected successfully!")

    # Apply perspective transformation
    scanned = perspective_transform(image, document_contour)

    # Save the scanned document
    scanned_path = os.path.join(output_dir, "scanned_document.jpg")
    cv2.imwrite(scanned_path, scanned)

    print("Perspective transformation completed!")
    print(f"Scanned document saved to {scanned_path}")

    # Enhance the scanned document
    enhanced = enhance_document(scanned)

    # Save enhanced document
    enhanced_path = os.path.join(output_dir, "enhanced_document.jpg")
    cv2.imwrite(enhanced_path, enhanced)

    print("Document enhancement completed!")
    print(f"Enhanced document saved to {enhanced_path}")

    # Analyze document quality
    quality = analyze_quality(scanned)

    print("\n--- Document Quality Report ---")
    print("Blur score:", quality["blur_score"])
    print("Brightness:", quality["brightness"])

    for message in quality["messages"]:
        print("Status:", message)

    # Save quality report
    report_path = os.path.join(output_dir, "quality_report.json")
    save_quality_report(quality, report_path)

    print(f"Quality report saved to {report_path}")

    # Draw the detected document boundary
    detected = image.copy()

    cv2.drawContours(
        detected,
        [document_contour],
        -1,
        (0, 255, 0),
        3
    )

    # Save results
    edges_path = os.path.join(output_dir, "edges.jpg")
    detected_path = os.path.join(output_dir, "detected_document.jpg")

    cv2.imwrite(edges_path, edges)
    cv2.imwrite(detected_path, detected)

    print(f"Edge image saved to {edges_path}")
    print(f"Detected document saved to {detected_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Smart Document Scanner and Quality Analyzer"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input document image"
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Directory where processed files will be saved"
    )

    args = parser.parse_args()

    try:
        main(args.input, args.output)
    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")