def duplicates_packing(symbols: str) -> list:
    symbols = ''.join(symbols.split())
    result_list = list()
    previous_symbol = ''
    for i in symbols:
        if i == previous_symbol:
            result_list[-1].append(i)
        else:
            result_list.append([i])
        previous_symbol = i
    return result_list


def main():
    string = input()
    print(duplicates_packing(string))


if __name__ == '__main__':
    main()
