def chunked(instr: str, chunk_size: int) -> list:
    result_lst = list()
    tmp_lst = (
        list()
    )  # for collecting symbols in a chunk; it's placed in result_lst when it's full
    counter = 1  # for counting if chunk is full
    for i in instr:
        if counter % chunk_size != 0:
            # Add a symbol to the chunk while it's not full
            tmp_lst.append(i)
        else:
            # Add the last symbol to the chunk to make it full
            tmp_lst.append(i)
            # Add chunk to result_lst and renew tmp_lst for next iterations
            tmp = tmp_lst
            result_lst.append(tmp)
            tmp_lst = []
        counter += 1
    if len(tmp_lst) > 0:
        # Add last symbols which are not packed to last full chunk
        result_lst.append(tmp_lst)
    return result_lst


def main():
    print(chunked("".join(input().split()), int(input())))


if __name__ == "__main__":
    main()
