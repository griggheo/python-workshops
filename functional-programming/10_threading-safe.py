# safe threading - no side effects

import threading

def increment_number(x):
   return (x + 1)

def task_for_thread(x):
    for _ in range(50000):
        x = increment_number(x)
    return x

def main():
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        x = 0
        future1 = executor.submit(task_for_thread, x)
        future2 = executor.submit(task_for_thread, x)
        return_value1 = future1.result()
        return_value2 = future2.result()
        print(f"Value returned from thread 1: {return_value1}")
        print(f"Value returned from thread 2: {return_value2}")
        print(f"Final result: {return_value1+return_value2}")


if __name__ == "__main__":
    for i in range(5):
        print(f"Iteration {i+1}")
        main()
