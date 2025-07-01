def generate_odd_series(a: int) -> list:
    if a < 1:
        return []
    return [2 * i + 1 for i in range(a)]


if __name__ == "__main__":
    test_cases = [1, 2, 3, 4]
    for a in test_cases:
        result = generate_odd_series(a)
        print(f"Input a = {a}, Output: {', '.join(map(str, result))}")
