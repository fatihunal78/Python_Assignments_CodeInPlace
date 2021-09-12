import math

def main():
 	n = int(input("Enter a number: "))
	while n > 1:
		if (n % 2) != 0:
			print(str(n) + " is odd, so I make " + str(3*n + 1) + ": ")
			n = (3*n) + 1
			count += 1
		else:
			print(str(n) + " is odd, so I make " + str(n /2) + ": ")
			n = (3*n) + 1

if __name__ == '__main__':
    main()
