def calculator():
    sum=0.0
    print("enter")
    while(True):
        num=str(input())
        if(num=="stop"):
            break
        elif (num[0] == '*'):
             sum = sum * float(num[1:])
        elif(num[0]=='/'):
            sum=sum / float(num[1:])
        else:
              sum= sum + float(num)
        print("sum is the following")
        print(sum)
    return sum

#driver code
calculator()

