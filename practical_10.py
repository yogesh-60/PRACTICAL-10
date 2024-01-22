file=open("practical-10.txt",'w')
number=int(input("Number: "))
abc=[]
while (number>0):
    temp=number%2
    abc.append(temp)
    number=int(number/2)
abc.reverse()
file.write(str(abc))