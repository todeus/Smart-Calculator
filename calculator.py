# write your code here
from collections import deque
variables = {}


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def split_to_deque(string):
    global variables

    if split_assign(string):
        deq = deque()
        op = string.split()

        for x in op:
            deq.append(x)

        return deq
    return "EXP"


def split_assign(string):
    global variables
    expr_list = string.split("=")
    a = ''.join(expr_list[0].split())

    if expr_list.__len__() == 2:
        if a.isalpha() or is_num(a):
            try:
                variables[a] = calculate(expr_list[1])
            except MyError as mr:
                #  print(mr)
                print("Invalid assignment")
            return False
        else:
            print("Invalid identifier")
            return False
    elif expr_list.__len__() > 2:
        print("Invalid assignment")
        return False

    return True


def operate(x, y, op):
    if not is_num(x):
        x = variables[x]
    if not is_num(y):
        y = variables[y]
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


def recurrent_calc(a):
    if len(a) == 1:
        if is_num(a[0]):
            return int(a[0])
        else:
            try:
                return variables[a[0]]
            except KeyError:
                raise MyError("Unknown variable")
                return
    if len(a) == 3:
        return operate(a[0], a[2], a[1])
    x = a.popleft()
    op = determinate_operation(a.popleft())
    y = a.popleft()
    a.appendleft(operate(x, y, op))
    return recurrent_calc(a)


def calculate(a):
    deq = split_to_deque(a)
    if deq == "EXP":
        return
    elif len(deq) % 2 == 0:
        return "Invalid expression"
    else:
        try:
            return recurrent_calc(deq)
        except ValueError:
            return "Invalid expression"



def is_num(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


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
            try:
                result = calculate(string)
            except MyError as mr:
                result = mr
            if result is not None:
                print(result)


if __name__ == "__main__":
    main()
