# write your code here
from collections import deque


def split_to_deque(string):
    deq = deque()
    op = string.split()

    for x in op:
        deq.append(x)

    return deq


def operate(x, y, op):
    if determinate_operation(op) == "+":
        return int(x) + int(y)
    elif determinate_operation(op) == "-":
        return int(x) - int(y)
    else:
        return "Invalid expression"


def determinate_operation(op):
    if op == "+":
        return "+"
    elif op == "-":
        return "-"
    elif len(op) > 1 and (op.count("-") == 1 or op.count("+") == 1):
        return None
    elif len(op) > 1:
        op = op.replace("--", "+")
        op = op.replace("++", "+")
        op = op.replace("+-", "-")
        op = op.replace("-+", "-")
        op = determinate_operation(op)
        return op


def recurent_calc(a):
    if len(a) == 1:
        return int(a[0])
    if len(a) == 3:
        return operate(a[0], a[2], a[1])
    x = a.popleft()
    op = determinate_operation(a.popleft())
    y = a.popleft()
    a.appendleft(operate(x, y, op))

    return recurent_calc(a)


def calculate(a):
    deq = split_to_deque(a)
    if len(deq) % 2 == 0:
        return "Invalid expression"
    else:
        try:
            return recurent_calc(deq)
        except ValueError:
            return "Invalid expression"


def main():
    while True:
        string = input()
        if string == "":
            continue
        if string == "/exit":
            print("Bye!")
            break
        elif string == "/help":
            print("The program calculates the sum of numbers")
            print("The program calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4, and so on.")
        elif string.startswith("/"):
            print("Unknown command")
        else:
            print(calculate(string))




if __name__ == "__main__":
    main()
