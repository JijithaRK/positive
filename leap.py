j=int(input())
if j%4==0:
    if j%100==0:
        if j%400==0:
            print("yes")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")
