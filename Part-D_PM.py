import time
import functools
import random

# Part D — AI Augmented Task

"""
Prompt Used:
Write a Python decorator called retry(max_attempts=3, delay=1)
that retries a function when it raises an exception.
Use exponential backoff and functools.wraps.
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
which preserves the original function’s metadata such as name and docstring. This is important when using 
decorators in production systems or debugging tools.

The code also implements exponential backoff using `delay * (2 ** attempts)`. This is a good strategy because 
it gradually increases the waiting time between retries, reducing pressure on external systems such as 
APIs or databases.

However, the implementation still has some limitations. The decorator catches all exceptions using 
`except Exception`, which means it cannot distinguish between retryable and non-retryable errors. 
For example, configuration errors or invalid user input should not trigger retries. 
Another limitation is the lack of logging support. In production systems, retry attempts should be logged 
for debugging and monitoring purposes.

Additionally, the decorator does not allow users to specify which exception types should trigger retries. 
A possible improvement would be adding a parameter like `retry_exceptions=(Exception,)` so developers can 
control the behavior more precisely.

Overall, the AI-generated solution is functional but could be improved with better exception filtering, 
logging, and configuration options.
"""

if __name__ == "__main__":
    try:
        print("Running unstable_function with retry decorator...")
        unstable_function()
    except Exception as e:
        print(f"Function failed after max retries: {e}")
