# from dataclasses import replace
from logging import exception
from pathlib import Path

# from turtle import update
class Library():
    def __init__(self,Listofbooks,libName):
        self.Name=libName
        # # folder=open(f'libraries', "r")
        # # path=f'libraries/{libName}.txt'
        # if Path(f'libraries/{libName}.txt').is_file():
        #     print(f"There is already a library with the name-{libName} you entered try a different name Or open the same library if it is yours.")

        #     # opena = open(f'libraries/{libName}.txt', "a")
        #     # for key,value in Listofbooks.items():
        #     #     opena.write(f'\n%s:%s' %(key,value))
        #     # # opena.write(f"{Listofbooks}")
        #     # opena = open(f'libraries/{libName}.txt', "r")
        #     # openr = opena.read()
        #     # print(f"Here is the list of Books you entered:-->\n{openr}")
        # else:
            # print(f'{libName}\n {Listofbooks}')
        open(f'libraries/{libName}.txt', "x")
        opena=open(f'libraries/{libName}.txt', "a")
        for key,value in Listofbooks.items():
            opena.write(f'%s:%s\n' %(key,value))
        # opena.write(f"{Listofbooks}")
        opena = open(f'libraries/{libName}.txt', "r")
        # openr = opena.read()
            
        index= -1
        for line in opena:
            index+=1
            linee=line.title()
            # opena=open(f'libraries/{libName}.txt', "a")
            # opena.write(f"{linee}\n")
            filehand=open(f'libraries/{libName}.txt', "r")
            listofline=filehand.readlines()
            newline=line.replace(line,linee)
            listofline[index]=newline
            filehand=open(f'libraries/{libName}.txt',"w")
            filehand.writelines(listofline)
            filehand.close()
        # outw = open(f'libraries/{libName}.txt', "w")
        # outw.write(output)
        f=open(f'libraries/{libName}.txt', "r")
        priread=f.readlines()
        print(f"Here is the list of Books you entered:-->\n{priread}")
        # f1.close()

    def Display(namel):
        searchr = open(f'libraries/{namel}.txt', "r")
        key = input("give the name of a Book\n")
        key= key.title()
        # for key in searchr
        index = 0
        opt = False
        for line in searchr:
            index += 1
            # checking string in present line
            if key in line:
                print("[Name of book : Holders name OR Availability details]\n", line)
                opt = True
        if opt == False:
            print("There is no book with this name\n")
        searchr.close()
    def Issue(Namebook, namel):
        searchr = open(f'libraries/{namel}.txt', "r")
        # print
        opts=False
        index= -1 
        for line in searchr:
            index += 1
            # checking string in present line
            if Namebook in line:
                print("[Name of book : Holders name]\n",line)
                avva="Available"
                if avva in line:
                    print("Book is available give 1 for issue and 2 for discard the process ")
                    ava=int(input())
                    if ava==1:
                        while(True):
                            iname=input("Enter your Good-name\n")
                            if not iname.isalpha():
                                print("Invalid entry name should be only in alphabets.")
                                continue
                            if len(iname)<4:
                                print("Name should contain atleat 4 alphabets")
                                continue
                            break
                        # try:
                        #     intname = int(iname)
                        #     flname=float(iname)
                        #     print("Invalid entry name should be only in alphabets.")
                        # except:
                        #     pass
                        iname=iname.title()
                        filehand=open(f'libraries/{namel}.txt', "r")
                        listofline=filehand.readlines()
                        newline=line.replace(line,f"{Namebook}:{iname}\n")
                        listofline[index]=newline
                        filehand=open(f'libraries/{namel}.txt',"w")
                        filehand.writelines(listofline)
                        print("Your book has been successfully issued-->",newline,"\n")

                    elif ava== 2:
                        print("Book issue process has ben discarded")
                elif avva not in line:
                    print("Opps, This book is not available right now.\n")
                opts = True
                if opts == False:
                    print("There is no book with this name\n")
    def addbook(numberb, nameb):
        dica={}
        print("Add more name of books and current holder names example:\n book=holder\n life life=holder2....")
        for i in range(numberb):
            text= input().split("=")
            dica[text[0]]=text[1]
        # searchr = open(f'libraries/{nameb}.txt', "a")
        # searchr.write(f"{dica}")
        opena = open(f'libraries/{nameb}.txt', "a")
        for key,value in dica.items():
            opena.write(f'\n%s:%s' %(key,value))
        # opena.write(f"{Listofbooks}")
        print("Your new books record has been successfully added to your Library.\n")
        opena.close()
        index= -1
        opena = open(f'libraries/{nameb}.txt', "r")
        for line in opena:
            index+=1
            linee=line.title()
            # opena=open(f'libraries/{libName}.txt', "a")
            # opena.write(f"{linee}\n")
            filehand=open(f'libraries/{nameb}.txt', "r")
            listofline=filehand.readlines()
            newline=line.replace(line,linee)
            print(newline)
            listofline[index]=newline
            filehand=open(f'libraries/{nameb}.txt',"w")
            filehand.writelines(listofline)
            filehand.close()
        opena = open(f'libraries/{nameb}.txt', "r")
        openr = opena.read()
        print(f"Here is the list of Books present in your library.-->\n{openr}")
        

    def retbook(retb,namer):
        searchr = open(f'libraries/{namer}.txt', "r")
        retb= retb.title()
        # for key in searchr
        index = -1
        opt = False
        for line in searchr:
            index += 1
            # checking string in present line
            if retb in line:
                print("[Name of book : Holders name OR Availability details]\n", line)
                print("Press 1 to return the book and 2 to quit the process.")
                repl=int(input())
                if repl == 1:
                    print(index)
                    filehand=open(f'libraries/{namer}.txt', "r")
                    listofline=filehand.readlines()
                    newline=line.replace(line,f"{retb}:Available\n")
                    listofline[index]=newline
                    filehand=open(f'libraries/{namer}.txt',"w")
                    filehand.writelines(listofline)
                    print("Your book has been successfully returned-->",listofline,"\n")
                
                elif repl==2:
                    break
                opt = True

        if opt == False:
            print("There is no book with this name\n")
        searchr.close()

        
# dictForharsh={"book1":"Available","book2":"ram","book3":"Sham"}
# harsh=Library(dictForharsh,"Harshpreet")
# # print(harsh)
while (True):
    print("----------------------------- Welcome To Library Management System -----------------------------")
    choice = input("Choose 1 for Creating Library , 2 for Opening a library and perform various funtion and 3 for quit.\n")
        # input("Choose 1 for Creating Library , 2 for Search for a book in library,"
        #         " 3 for update, 4 for quit and print the Contact Book\n"))
    if choice == "1":
        while(True):
            print("Give the Name for your Library only in alphabets.")
            name = input()
            if not name.isalpha():
                print("Invalid Library name should be only in alphabets.")
                continue
            if len(name)<4:
                print("Libray name should contain atleat 4 alphabets")
                continue
            break
       
        name=name.title()
        if Path(f'libraries/{name}.txt').is_file():
            print(f"There is already a library with the name - '{name}' try a different name Or open the same library if it is yours.\n")
        else:
            dictfile = {}
            n=int(input("Enter the number of Books in your library\n"))
            print("Make a file for name of book and current holder names example:\n book=holder\n life life=holder2....\n")
            dic={}
            for i in range(n):
                text= input().split("=")
                dic[text[0]]=text[1]
            
            newLibrary = Library(dic, f'{name}')
            # print(newLibrary)1

    elif choice=="2":
        names=input("Enter the name of your library\n")
        names=names.title()
        # D:\Library System\libraries
        if Path(f'libraries/{names}.txt').is_file():
            searchr = open(f'libraries/{names}.txt', "r")
            print(f'------------------------------{names} Libarary---------------------------------')

            while(True):

                print("Choose 1 to Search a Book,2 for issue process, 3 for adding more books in your library,4 for "
                      "returning a book, 5 for closing Library.")
                choose=input()
                # --------------------display or search a boook------------
                if choose=="1": 
                    print(f"-------------------------- {names} Library ( Display ) ----------------------------")
                    Library.Display(f'{names}') #--line number 26
                 # --------------------for issue proocess of a book------------
                elif choose=="2":
                    print(f"-------------------------- {names} Library ( Issue ) ----------------------------")
                    print("Give the name of a Book you want to issue or check its availability")
                    Namebookk = input()
                    Namebookk=Namebookk.title()
                    Library.Issue(f"{Namebookk}",names)
                elif choose=="3":
                    print(f"-------------------------- {names} Library ( Add Books ) ----------------------------")
                    print("Give the numbers of new books you want to add to the library")
                    numbern=int(input())
                    Library.addbook(numbern,f"{names}")
                elif choose=="4":
                    print(f"-------------------------- {names} Library ( Return Books ) ----------------------------")
                    print("Give the name of book you want to return to the Library.")
                    retname=input()
                    Library.retbook(f'{retname}',names)
                elif choose=="5":
                    print(f"Thank you for using {names} Library")
                    break
                else:
                    print("wrong input Give again")

        else:
            print("There is no Library with this name create one first.")
    elif choice=="3":
        print("Thankyou for using the Library Management System !!!!!!")
        break
    else:
        print("Wrong input check again.\n")