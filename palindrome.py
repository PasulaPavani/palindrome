print("I going to be successful one day")
def palindrome(x: int)-> bool:
    if x< 0:
        return False
    number = x
    reverse = 0
    while number:
        reverse = reverse*10+number %10
        number //=10
    return x == reverse
p = [121,56,787,-454,789,1001] 
v=map(palindrome,p)
print(list(v))   
