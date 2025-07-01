def generate_odd_series_ceiling(a: int) -> list:
    if a < 1:
        return []
    # Calculate the number of odd numbers needed (ceiling logic)
    n = (a + 1) // 2 if a % 2 == 0 else a // 2 + 1
    return [2 * i + 1 for i in range(n)]

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6]
    for a in test_cases:
        result = generate_odd_series_ceiling(a)
        print(f"Input a = {a}, Output: {', '.join(map(str, result))}")
