def print_block(input):
    size = len(input)
    mat = [[" " for _ in range(size)] for _ in range(size)]
    for i in range(size):  # Rows
        if i == 0 or i == size - 1:
            mat[i][:] = input
        else:
            mat[i][0] = input[0]
            mat[i][-1] = input[-1]
            mat[i][i] = input[i]
            mat[i][size - i - 1] = input[size - i - 1]
    print("\n".join("".join(i) for i in mat))


print_block("PINEAPPLE")
print_block("BANANA")
