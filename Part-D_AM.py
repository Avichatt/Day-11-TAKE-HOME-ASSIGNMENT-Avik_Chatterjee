"""
# Part D — AI Augmented Task

## 1️⃣ Prompt Used

```
Write a Python script that reads a CSV file and automatically detects the delimiter.
Possible delimiters are comma, tab, semicolon, or pipe.
Use csv.Sniffer() to detect the delimiter.
Then convert the CSV data into a JSON file.
Use pathlib and context managers.
Make the code beginner friendly.
```

---

# 2️⃣ AI Generated Code
"""

import csv
import json
from pathlib import Path

def csv_to_json(csv_file, json_file):

    with open(csv_file, "r", encoding="utf-8") as f:

        sample = f.read(1024)
        f.seek(0)

        dialect = csv.Sniffer().sniff(sample)

        reader = csv.DictReader(f, dialect=dialect)

        data = list(reader)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    # csv_to_json("data.csv", "data.json")
    print("Part D AM loaded. Function available: csv_to_json")

"""
---

# 3️⃣ Test Cases

Test file 1
name,age
Alice,22
Bob,25

Test file 2
name;age
Tom;30
Jerry;28

---

# 4️⃣ Critical Evaluation (≈200 words)

The AI-generated script correctly reads a CSV file and converts it into JSON format. One important thing the AI did well was using csv.Sniffer() to automatically detect the delimiter. This allows the script to work with different CSV formats such as comma-separated, semicolon-separated, tab-separated, or pipe-separated files. The code also used csv.DictReader, which is useful because it converts rows into dictionaries using the header names as keys. This makes the JSON output structured and easy to understand.

Another positive aspect is the use of pathlib and context managers (with open). These practices improve code readability and ensure files are properly closed after reading or writing.

However, the AI output still has some limitations. It does not handle edge cases such as empty files, missing headers, or incorrect CSV formatting. If the CSV file is extremely large, the script loads the entire file into memory using list(reader), which could cause performance issues. Another improvement would be adding command-line arguments so users can specify input and output files dynamically.

Overall, the AI solution is a good starting point, but it would benefit from better error handling, validation checks, and support for large files to make it production-ready.
"""
