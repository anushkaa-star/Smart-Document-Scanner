import json


def save_quality_report(quality_data, output_path):
    """Save document quality results as a JSON report."""

    report = {
        "blur_score": quality_data["blur_score"],
        "brightness": quality_data["brightness"],
        "status": quality_data["messages"]
    }

    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)