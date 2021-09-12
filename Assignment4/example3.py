import math


def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.")
    count = 0
    num_before = 0
    num_after = 0
    while num_after >= num_before:
        num_after = float(input("Enter num: "))
        if num_after >= num_before:
            num_before = num_after
            count += 1
        else:
            break

    print("Thanks for playing!")
    print("Sequence length: " + str(count))

if __name__ == "__main__":
    main()