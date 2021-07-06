def inputTwoNum():
    a = int(input())
    b = int(input())
    return a, b


def sumOfTwo(a, b):
    return a + b


def output(op1, op2, result):
    print("{0} + {1} = {2}".format(op1, op2 ,result))


def main():
    a, b = inputTwoNum()
    result = sumOfTwo(a, b)
    output(a, b, result)


if __name__ == "__main__":
    main()    
