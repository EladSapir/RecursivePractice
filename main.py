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

def Power(number,pow):
    if pow==1:
        return number
    return number*Power(number,pow-1)

def LeastCommonMultiple(first_num,sec_num):
    modulu = first_num % sec_num
    if modulu == 0:
        return first_num
    return first_num * LeastCommonMultiple(sec_num, modulu) / modulu
    if number==1:
        return

def reverseString(str):
    if len(str)==0:
        return ""
    return reverseString(str[1:])+str[0]

def maxOfList(arr,max=-99999999):
    if len(arr)<1:return
    if len(arr)==1:
        if max>arr[0]:
            return max
        return arr[0]
    if arr[0]>max:
        return maxOfList(arr[1:],arr[0])
    return maxOfList(arr[1:], max)

def MinimalWayToTheEnd(arr,i=0):
    if i>=len(arr):
        return 0
    return 1+min(MinimalWayToTheEnd(arr,i+arr[i][0]),MinimalWayToTheEnd(arr,i+arr[i][1]),
                 MinimalWayToTheEnd(arr,i+arr[i][2]),MinimalWayToTheEnd(arr,i+arr[i][3]))

def GCD(x, y):
    if x % y == 0:
        return y
    return GCD(y, x % y)

def MaximumWayToTheEnd(arr,i=0):
    if i>=len(arr):
        return 0
    return 1+max(MaximumWayToTheEnd(arr,i+arr[i][0]),MaximumWayToTheEnd(arr,i+arr[i][1]),
                 MaximumWayToTheEnd(arr,i+arr[i][2]),MaximumWayToTheEnd(arr,i+arr[i][3]))


def main():
    print("Checks: ")
    # print("factorial of 0: "+ str(factorial(0)))
    # print("factorial of 1: " + str(factorial(1)))
    # print("factorial of 5: " + str(factorial(5)))
    # print("factorial of 12: " + str(factorial(12)))
    # print(Fibonacci(7))
    # print(SumDigits(192555))
    # print(Power(2,5)+Power(3,3))
    # print(LeastCommonMultiple(5,2))
    # print(LeastCommonMultiple(5, 9))
    # print(LeastCommonMultiple(16, 2))
    # print(reverseString("abcdef"))
    # print(maxOfList([66,2,3,4,5,6,7,8,9,-7,55,33,22,48]))
    # print(maxOfList([]))
    print(MinimalWayToTheEnd([[1,8,4,2],[5,2,3,6],[2,7,1,8],[3,8,9,4],[7,2,1,6],[3,8,4,9],[6,9,7,10],[4,8,6,3],[5,7,2,9]
        ,[1,4,3,8],[5,9,7,2],[10,2,7,6],[3,5,1,4]]))
    print(MaximumWayToTheEnd([[1, 8, 4, 2], [5, 2, 3, 6], [2, 7, 1, 8], [3, 8, 9, 4], [7, 2, 1, 6], [3, 8, 4, 9],
         [6, 9, 7, 10],[4, 8, 6, 3], [5, 7, 2, 9], [1, 4, 3, 8], [5, 9, 7, 2], [10, 2, 7, 6], [3, 5, 1, 4]]))
    print(GCD(24,9))
if __name__ == "__main__":
    main()