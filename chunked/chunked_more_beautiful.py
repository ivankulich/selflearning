def chunked(instr: str, chunk_size: int) -> list:
    result_lst = list()
    for i in range(0, len(instr), chunk_size):
        result_lst.append(list(instr[i : i + chunk_size]))
    return result_lst


def main():
    print(chunked("".join(input().split()), int(input())))


if __name__ == "__main__":
    main()
