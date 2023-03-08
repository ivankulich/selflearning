def sublists_of_list(input_string: str) -> list:
    result_list = list()
    input_string = ''.join(input_string.split())

    result_list.append([])
    for i in range(1, len(input_string) + 1):
        for j in range(0, len(input_string) - i + 1):
            result_list.append(list(input_string[j:j+i]))

    return result_list


def main():
    print(sublists_of_list(input()))

if __name__ == "__main__":
    main()