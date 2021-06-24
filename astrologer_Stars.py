line=int(input("Enter the number of lines: "))
patern=bool(int(input("Enter pattern type for False 0 / for True 1): ")))

if patern==False:
    while(line>0):
        print(line*"*")
        line-=1
elif patern==True:
   for i in range(1,line+1):
       print(i*"*")