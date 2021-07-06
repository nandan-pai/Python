def input_two_numbers():
    a = int(input())
    b = int(input())
    return a, b


def add(a, b):
    return a + b


def output(op1, op2, result):
    print("{0} + {1} is {2}".format(op1, op2 ,result))

    
def main():
    a,b=input_two_numbers()
    sum=add(a,b)
    output(a,b,sum)
    
main()
