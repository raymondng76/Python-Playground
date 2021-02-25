# Given 2 strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If string is longer than the other, append the additional letters onto the end of the merged string.

from rich.console import Console

console = Console()


def main(word1: str, word2: str) -> str:
    l1, l2 = [*word1], [*word2]
    if len(word1) > len(word2):
        diff = len(word1) - len(word2)
        [l2.append("") for _ in range(diff)]
    elif len(word2) > len(word1):
        diff = len(word2) - len(word1)
        [l1.append("") for _ in range(diff)]
    results = []
    for i, j in zip(l1, l2):
        if i:
            results.append(i)
        if j:
            results.append(j)
    return "".join(results)


def main2(word1: str, word2: str) -> str:
    diff = ""
    if len(word1) > len(word2):
        diff += word1[len(word2) :]
    elif len(word2) > len(word1):
        diff += word2[len(word1) :]
    temp = ""
    for i, j in zip(word1, word2):
        temp += i + j
    return temp + diff


if __name__ == "__main__":
    word1 = "abc"
    word2 = "qwerty"
    console.print(main(word1, word2), style="bold green")
    console.print(main2(word1, word2), style="bold red")
