from Stack import Stack
def reverseString(str):
    myS=Stack()
    for s in str:
        myS.push(s)
    rs=""
    while not myS.isEmpty():
        rs+=myS.pop()
    return rs

def Dec2Bin(n):
    myS=Stack()
    while n!=0:
        b=n%2
        myS.push(b)
        n=int(n/2)
    rs=""    
    while not myS.isEmpty():
        rs+=str(myS.pop())
    return rs    

# S = input("Input a string to reverse: ")
# print("Result after reversing: ", reverseString(S))
n = int(input("Input number: "))
print(f"Binary of {n}: ", Dec2Bin(n)) 
