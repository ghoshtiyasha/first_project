def calculator():
    sum=0
    print("enter")
    while(True):
        num=str(input())
        if(num=="stop"):
            break
        else:
            #print("Enter the number")
            #num=int(input())
            sum= sum + int(num)
            print("sum is the following")
            print(sum)
    return sum

#driver code
calculator()

