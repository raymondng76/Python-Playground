# Print numbers from 1 to 100
# If multiplier of 3, print 'Fizz'
# If multiplier of 5, print 'Buzz'
# If both 3 and 5, print 'Fizz Buzz'
# Otherwise, print the number it self
from rich.console import Console

console = Console()


def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            console.print("Fizz Buzz", style="green")
        elif i % 5 == 0:
            console.print("Buzz", style="blue")
        elif i % 3 == 0:
            console.print("Fizz", style="red")
        else:
            print(i)


if __name__ == "__main__":
    main()
