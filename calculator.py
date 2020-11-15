# write your code here

def result(string):
    num = [int(x) for x in string.split()]
    if len(num) == 0:
        return
    print(sum(num))


def main():
    while True:
        string = input()
        if string == "/exit":
            print("Bye!")
            break
        result(string)


if __name__ == "__main__":
    main()
