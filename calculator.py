# write your code here

def determ_op(string):
    if "+" in string:
        return 1
    elif string.count("-") % 2 == 0:
        return 1
    else:
        return -1


def result(string):
    ops = string.split()
    op = 1
    summ = 0
    if len(ops) == 0:
        return
    for o in ops:
        try:
            summ += int(o) * op
        except ValueError:
            op = determ_op(o)
    print(summ)


def main():
    while True:
        string = input()
        if string == "/exit":
            print("Bye!")
            break
        elif string == "/help":
            print("The program calculates the sum of numbers")
            print("The program calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.")
        else:
            result(string)


if __name__ == "__main__":
    main()
