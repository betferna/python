#!/bin/usr/env python3

def input_temperature(temp_str) -> None:
    try:
        print(f"Input data is '{int(temp_str)}'")
        print(f"Temperature is now {int(temp_str)}*C\n")
    except ValueError:
        print(f"Input data is '{temp_str}'")
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'\n")


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")

    test_temperature()
    print("All tests completed - program didn't crash!")
