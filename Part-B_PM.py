import csv
import json
import time
import traceback
from pathlib import Path

# Part B — Resilient File Processor

def process_files(directory):
    folder = Path(directory)
    processed = 0
    failed = 0
    errors = []

    if not folder.exists():
        print(f"Directory {directory} does not exist.")
        return

    for file in folder.glob("*.csv"):
        retries = 3
        while retries > 0:
            try:
                with open(file, "r", newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    rows = list(reader)

                    if not rows:
                        raise ValueError("Empty file")

                    processed += 1
                    break

            except PermissionError as e:
                retries -= 1
                if retries == 0:
                    failed += 1
                    errors.append({
                        "file": file.name,
                        "error": str(e)
                    })
                time.sleep(1)

            except Exception as e:
                failed += 1
                errors.append({
                    "file": file.name,
                    "error": traceback.format_exc()
                })
                break

    report = {
        "files_processed": processed,
        "files_failed": failed,
        "error_details": errors
    }

    with open("processing_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    
    print("Processing complete. Report saved to processing_report.json")

if __name__ == "__main__":
    # Create a dummy 'data' folder if it doesn't exist for testing
    Path("data").mkdir(exist_ok=True)
    process_files("data")
