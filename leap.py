jr=int(input())
if(jr%4==0 and jr%100!=0 or jr%400==0):
    print("yes")
else:
    print("no")
