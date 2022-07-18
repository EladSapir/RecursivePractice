# factorial
def factorial(number):
    if number ==0:
        return 1
    return number*factorial(number-1)

def Fibonacci(n) :
    if n==0 :
        return 0
    elif n ==1 :
        return 1
    else :
        return Fibonacci(n-1) +Fibonacci(n-2)

def SumDigits(number):
    if number==0:
        return number
    return number%10+SumDigits(number//10)


def main():
    print("Checks: ")
    # print("factorial of 0: "+ str(factorial(0)))
    # print("factorial of 1: " + str(factorial(1)))
    # print("factorial of 5: " + str(factorial(5)))
    # print("factorial of 12: " + str(factorial(12)))
    print(Fibonacci(7))
    print(SumDigits(192555))

if __name__ == "__main__":
    main()