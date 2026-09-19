#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    try:
        print("Input data is '25'")
        input_temperature("25")
        print("Input data is 'abc'")
        input_temperature("abd")
    except Exception as e:
        print("Caught input_temperature error:", e)


if __name__ == "__main__":
    test_temperature()
    print("All tests completed- program didn't crash!")
