def tree_create_childs(tree_lst: list):
    """
    Transforms representation of tree.
    :param tree_lst: Tree represented as list where index of element is name of node and value of element is name of parent node
    :return: Tree represented as list of lists where index of element is name of node and value of element is list with names of child nodes
    """
    result_lst = [[] for _ in range(len(tree_lst) + 1)]
    for i in range(len(tree_lst)):
        if tree_lst[i] != -1:
            result_lst[tree_lst[i]].append(i)
    return result_lst


def tree_height_from_root(lst: list, root: int):
    """
    Calculates height of tree starting from exact root.
    :param lst: Tree represented as list of lists where index of element is name of node and value of element is list with names of child nodes
    :param root: Index of root in tree which is presented in lst
    :return: height of tree
    """
    tmp = lst[root]
    height = 1
    for i in tmp:
        height = max(height, 1 + tree_height_from_root(lst, i))
    return height


def tree_height(lst: list):
    """
    Calculates height of tree.
    Union of functions tree_create_childs and tree_height_from_root.
    :param lst: Tree represented as list where index of element is name of node and value of element is name of parent node
    :return: height of tree
    """
    if lst.count(-1) != 1:
        return False
    if len(lst) < 2:
        return len(lst)
    if max(lst) > len(lst):
        return False
    return tree_height_from_root(tree_create_childs(lst), lst.index(-1))


def main():
    while True:
        n = int(input())
        v = input().split()
        if len(v) != n:
            raise ValueError(
                f"Incorrect number of arguments. You should enter {n} arguments in second line."
            )
        else:
            break
    v = [int(i) for i in v]
    print(tree_height(v))


if __name__ == "__main__":
    main()
