import time
import functools
import random

# Part D — AI Augmented Task

"""
Prompt Used:
You are an expert Python developer creating educational code for beginners. Your task is to write a production-ready Python script that reads a CSV file, automatically detects its delimiter, and converts the data to JSON format.

**Core Requirements:**
- Use `csv.Sniffer()` to automatically detect the delimiter (comma, tab, semicolon, or pipe)
- Use `pathlib.Path` for all file path operations
- Use context managers (`with` statements) for all file operations
- Make the code beginner-friendly with clear variable names, helpful comments, and simple logic flow

**Code Quality Standards:**
- Include error handling for missing files, invalid CSV data, and file permission issues
- Add inline comments explaining what each section does (especially the Sniffer logic)
- Keep functions small and focused with single responsibilities
- Use descriptive function and variable names that explain intent
- Avoid advanced Python patterns that would confuse beginners

**Functionality:**
The script should:
1. Accept a CSV file path as input (either as a command-line argument or hardcoded for testing)
2. Detect the delimiter automatically using `csv.Sniffer()`
3. Read all rows from the CSV file
4. Convert the CSV data to JSON (with the first row as headers/keys)
5. Write the JSON output to a file in the same directory as the input CSV

**Output Format:**
- The script should be a single, runnable `.py` file
- Include a brief docstring at the top explaining what the script does
- Add a `if __name__ == "__main__":` block so it can be executed directly

Make the code clear enough that a Python beginner could understand and modify it without struggle.
"""

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    wait = delay * (2 ** attempts)
                    print(f"Retrying in {wait} seconds...")
                    time.sleep(wait)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def unstable_function():
    if random.random() < 0.5:
        raise ValueError("Random failure")
    print("Success!")

"""
Critical Evaluation (~200 words):
The AI-generated retry decorator successfully implements a retry mechanism for functions that raise exceptions. 
The decorator uses a wrapper function to repeatedly call the target function until it succeeds or reaches 
the maximum number of attempts. One positive aspect of the implementation is the use of `functools.wraps`, 
which preserves the original function’s metadata such as name and docstring.

The code also implements exponential backoff using `delay * (2 ** attempts)`. This is a good strategy because 
it gradually increases the waiting time between retries, reducing pressure on external systems.

However, the implementation still has some limitations. The decorator catches all exceptions using 
`except Exception`, which means it cannot distinguish between retryable and non-retryable errors. 
For example, configuration errors or invalid user input should not trigger retries. 
Another limitation is the lack of logging support.

Additionally, the decorator does not allow users to specify which exception types should trigger retries. 
A possible improvement would be adding a parameter like `retry_exceptions=(Exception,)`.

Overall, the AI-generated solution is functional but could be improved with better exception filtering, 
logging, and configuration options.
"""

if __name__ == "__main__":
    try:
        unstable_function()
    except Exception as e:
        print(f"Function failed after retries: {e}")
