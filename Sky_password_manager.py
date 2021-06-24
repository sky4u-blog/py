secreat={"akash":"Open", "alok":"19143", "sonu":"it's me sonu", "khushi":"kuchh na", "amit":"lol", "dry":"i'm mad"}
def start():
    global temp
    ch=input("\t -------Welcome to SKY password manager-------\n\nPress '1' for View\nPress '2' for Add\nPress '3' for users list\nPress '0' for exit\nEnter your choice: ")

    if (ch=="1"):
        inpt=(input("\n\nEnter your username :")).lower()
        try:
            secreat[inpt]
            print("Your password is :",secreat[inpt])
            temp=input("\nPress any key to exit....")
            start()
        except:
            print("\nYou entred wrong username!!!")
            temp=input("\nPress any key to exit....")
            start() 
    elif (ch=="2"):
                nuser=(input("\n\nEnter new your username :")).lower()  
                try:
                    secreat[nuser]
                    print("\nUsername already avalable, try another!!!")
                    temp=input("\nPress any key to exit....")
                    start()
                except:    
                    npass=(input("Enter new your password :"))
                    secreat[nuser]=npass
                    temp=input("\nPress any key to exit....")
                    start()
    elif (ch=="3"):
        print("\nAll users are :")
        for key in secreat.keys():
            print (key)
        temp=input("\n\nPress any key to exit....")
        start()

    elif (ch=="0"):
        print("\n\n\tThanks to visit Sky password manager \U0001f600 \N{winking face} \N{grinning face with smiling eyes} !")
        print("\tPlease come back soon!!\n\n")
        exit
    else:
        print("\nYou entred wrong key!!!") 
        temp=input("\nPress any key to exit....")
        start()
start()        
                