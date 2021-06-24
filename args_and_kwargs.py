
def add(a,b,*c,**d):
    c2=str(*c)
    print("The last number is ",**d)
    try:
        print((a+b)+int(c2))   
    except:
        print((a+b))    

print("Start")
a=(int(input("Enter a number :")))
b=(int(input("Enter b number :")))
print("\nDo you wanna add more ")
temp=(input("yes or no: ")).lower()
if temp=="yes":
    c=((input("Enter c number :")))
    print("\nDo you wanna add more ")
    temp2=input("yes or no: ").lower()
    if temp2=="yes":
        d=((input("Enter d number :")))
        add(a,b,*c,**d)
    add(a,b,*c)    
else:
    print(temp)
    add(a,b)

