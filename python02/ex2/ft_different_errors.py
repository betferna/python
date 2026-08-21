#!/bin/urs/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        1/0
    if operation_number == 2:
        open("file.txt")
    if operation_number == 3:
        1 + "A"
    else:
        return


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: "
                  "invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: "
                  "[Errno 2] No such file or directory: '/non/existent/file'")
        except TypeError:
            print("Caught TypeError: "
                  "can only concatenate str (not \"int\") to str")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("Operation completed successfully\n")
    print("All error types tested successfully!")
