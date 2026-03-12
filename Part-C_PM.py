import json
import logging

# Part C — Interview Ready

"""
Q1 — Execution Flow of try/except/else/finally

Execution order:
1. try: Code that may cause an error runs here.
2. except: Runs if an exception occurs.
3. else: Runs only if no exception occurs in try.
4. finally: Always runs regardless of error.

Execution cases:
Case 1 (valid): try → else → finally
Case 2 (invalid): try → except → finally
"""

def execution_flow_example():
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid number")
    else:
        print("Number entered:", num)
    finally:
        print("Program finished")

"""
Q2 — safe_json_load
"""
logging.basicConfig(filename="json_errors.log", level=logging.ERROR)

def safe_json_load(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error("File not found")
        return None
    except json.JSONDecodeError:
        logging.error("Invalid JSON format")
        return None
    except PermissionError:
        logging.error("Permission denied")
        return None
    else:
        return data

"""
Q3 — Fixed Code
Problems fixed:
- removed bare except
- removed return in finally
- added detailed error message
"""

def process_data(data_list):
    results = []
    for item in data_list:
        try:
            value = int(item)
        except ValueError as e:
            print(f"Invalid value '{item}': {e}")
            continue
        else:
            results.append(value * 2)
    return results

if __name__ == "__main__":
    print("Part C PM loaded.")
