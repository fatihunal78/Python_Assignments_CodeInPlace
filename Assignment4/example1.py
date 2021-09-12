def main():
    # TODO write your solution here

    print ("Enter a sequence of non-decreasing numbers.")
    i=0
    before=0
    while True:
         after = float(input("Enter num: "))
         if (after>before):
             i=i+1
             before=after
         else:
             break

    print("Thanks for playing!")
    print("Sequence length! "+ str(i))

if __name__ == '__main__':
    main()
