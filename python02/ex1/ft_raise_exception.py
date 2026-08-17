#!/bin/urs/env python3

def input_temperature(temp_str) -> None:
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Input data is '{temp_str}'")
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'\n")
        return

    print(f"Input data is '{temperature}'")

    if temperature < 0:
        print(f"Caught input_temperature error: {temperature}°C is too cold for plants (min 0°C)\n")

    elif temperature > 40:
        print(f"Caught input_temperature error: {temperature}°C is too hot for plants (max 40°C)\n")

    else:
        print(f"Temperature is now {temperature}*C\n")


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")

    test_temperature()
    print("All tests completed - program didn't crash!")
