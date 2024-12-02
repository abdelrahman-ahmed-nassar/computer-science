#input : function(5)
#output: 120




























'''

def  factorial(n) :
  sum = 1
  for i in range(1, n+1):
    sum = sum * (i)
  print(sum)

factorial(5)

'''


'''
def factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is:", factorial(number))

'''
