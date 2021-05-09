def print_diamond(input):
    height = len(input)
    width = (height * 2) - 1
    mat = [[" " for _ in range(width)] for _ in range(width)]
    for i in range(height - 1):
        mat[i][height - 1] = input[i]
        mat[-i - 1][height - 1] = input[i]
        if i != 0:
            mat[i][height - i - 1] = input[0]
            mat[-i - 1][height - i - 1] = input[0]
            mat[i][height + i - 1] = input[0]
            mat[-i - 1][height + i - 1] = input[0]
    mat[height - 1][:] = input + input[::-1][1:]

    print("\n".join("".join(t) for t in mat))


print_diamond("DIAMOND")
