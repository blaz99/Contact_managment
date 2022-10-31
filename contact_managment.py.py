#making contact managmnet just using lists and if else
#next project is contact managment which is connected to mysql base
#blaz99

name_list= [ ]
phone_number_list= [ ]

while(True):
    
    print("Welcome to CONTACT MANAGMENT!!")
    print("Press 0 to Exit!")
    print("Press 1 to add name!!")
    print("Press 2 to add number!!")
    print("Press 3 to delete number from list!!")
    print("Press 4 to see everything!!")


    var1= int(input("Enter your choice: "))
    if var1==0:
        break
    elif var1==1:
        name_list= [x for x in input("Enter name of owner: ").split(" ")]
        print("You enter", name_list[0])
    elif var1==2:
        print("Seperate number with(,) !! ")
        phone_number_list= [x for x in input("Enter the phone number of owner: ").split(",")]
    elif var1==3:
        while(True):
            print("Press 1 to delete by name: ")
            print("Press 2 to delete by number: ")
            print("Press 3 to exit!!")
            var2= int(input("Choose from above: "))
            if var2==1:
                name_list.remove(input("Enter name: "))
            elif var2==2:
                phone_number_list.remove(int(input(("Enter your number: "))))
            elif var2==3:
                break
    elif var1==4:
        for i in name_list, phone_number_list:
            print("Name: {}, Phone number: {}".format(name_list, phone_number_list))
        break

