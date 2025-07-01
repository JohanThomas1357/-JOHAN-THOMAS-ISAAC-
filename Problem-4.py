def count_multiples(numbers: list) -> dict:
    result = {i: 0 for i in range(1, 10)}  # Initialize dictionary for 1 to 9
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result

if __name__ == "__main__":
    input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(input_list)
    print(f"Input: {input_list}")
    print(f"Output: {result}")
