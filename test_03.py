def product(l: list[int]) -> int:
    total = 1
    for val in l:
        total *= val

    return total


def is_spy(n: int) -> bool:
    n_as_string = str(n)
    list_of_strings = list(n_as_string)

    local_aray = []
    for val in list_of_strings:
        local_aray.append(int(val))

    return sum(local_aray) == product(local_aray)


def is_spy_02(n: int) -> bool:

    test_val = n
    local_array = []
    while test_val != 0:
        test_val, rem = divmod(test_val, 10)
        local_array.append(rem)

    return sum(local_array) == product(local_array)


def main() -> None:
    print(is_spy_02(1124))


if __name__ == '__main__':
    main()
