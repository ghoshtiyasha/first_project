
def calculator(sum, num):
    #exp_split(num)
    if (num[0] == '*'):
        sum = sum * float(num[1:])

    elif (num[0] == '/'):
        sum = sum / float(num[1:])
    else:
        sum = sum + float(num)
        #print("sum is the following")
    #print(sum)
    return sum



def exp_split(exp):
  plus= exp.split('+')
  for i in range (len(plus)):
      plus[i]='+'+ plus[i]


  minus=[]
  for s in plus:
      m=s.split('-')
      for i in range(1,len(m)):
          m[i]='+'+m[i]
      minus = minus+m

  into=[]
  for s in minus:
      m=s.split('*')

      for i in range(1,len(m)):
          m[i]="*"+m[i]

      into=into+m


  divi=[]
  for s in into:
      m=s.split('/')

      for i in range(1, len(m)):
          m[i]='/'+m[i]

      divi=divi+m

  return  divi



#driver code
x='2+3*6/4'
sx=exp_split(x)
sum=0
for i in sx:
   sum=calculator(sum,i)
print(sum)



#print(calculator(0,20+4*7))


