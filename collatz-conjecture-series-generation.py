import time
num = int(input("Enter a number:"))
print(num,end=" ")
while num!=1:
    if(num%2!=0):
        num = (3*num)+1
        print(int(num),end=" ")
        time.sleep(0.01)
    else:
        num = num/2
        print(int(num),end=" ")
        time.sleep(0.01)
