num=int(input("enter num:"))

if (num%2!=0):
    print("weird")
elif(num%2==0 and num>=2 and  num<=5):
    print("not weird")
elif(num%2==0 and num>=6 and  num<=20):
    print("weird")
elif( num>20):
    print("not weird")
