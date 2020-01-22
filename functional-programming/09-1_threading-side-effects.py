# non-safe threading: threads modifying same global object
"""
https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_synchronizing_threads.htm
"""

import threading

x = 0

def increment_global():
   global x
   x += 1

def task_for_thread():
   for _ in range(50000):
      increment_global()

def main():
    global x

    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        x = 0
        executor.submit(task_for_thread)
        executor.submit(task_for_thread)
   
if __name__ == "__main__":
    for i in range(5):
        main()
        print(f"x = {x} after Iteration {i+1}")

