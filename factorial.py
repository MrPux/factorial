#   factorial(5)  # Should return 120 
def factorial(num):
    answer = 1
    for i in list(range(1, num + 1)):
        amswer *= i
    return answer
print(factorial(5)) # prints 120