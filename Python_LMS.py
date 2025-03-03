from datetime import datetime

#Books Library
Title=['Feu','The Lover','Our Riches','Paris Stories','Tolstory','A Void','Nos richesses']
ISBN=['9782213720784','9375700528','9780811228152','1590170229','9802137687','9781567922967','9782021373806']
Author=['Maria Pourchet','Marguerite Duras','Kaouther Adimi','Mavis Gallant','Henri Troyat','Georges Perec','Kaouther Adimi']


#simple database of this system-Instead of a separable database that can be saved, i kept this as a simple set of list for simple demonstrarion. 
B_details={}
n=0
for line in ISBN:
    B_details.update({line:{'title':Title[n],'ISBN':ISBN[n],'author':Author[n],'status':'Available','date_time':""}})
    n=n+1

#To add a new book
def add_new_book():
    title=input("Enter book title:")
    author=input("Enter book author:")
    isbn=input("Enter book ISBN:")
    B_details.update({isbn:{'title':Title,'author':Author,'status':'Available','date_time':""}})
    print("***New book added successfully.***")

#To borrow a book
def borrow_book():
    ISBN=input("Enter book ISBN:")
    if ISBN in B_details:
        if B_details[ISBN]['status']=='Available':
            B_details[ISBN]['status']='Borrowed'
            B_details[ISBN]['date_time']=datetime.now().strftime("%y-%m-%d, %H:%M:%S")
            print("***Book borrowed successfully.***")

        else:
            print("***This book is not available***")
    else:
        print("***Sorry, this book not found in the book library.***")

#To return book
def return_book():
    isbn=input("Enter book ISBN:")
    if isbn in B_details:
        if B_details[isbn]['status']=='Borrowed':
            B_details[isbn]['status']='Available'
            B_details['date_time']=datetime.now().strftime("%y-%m-%d, %H:%M:%S")
            print("***Book returned successfully.***")

        else:
            print("***This book is currently available.***")
    else:
        print("***Sorry, this book not found in the book library.***")

#This is for display all available books in library.
def view_available_book():    
    for isbn, details in B_details.items():
        if details['status']=='Available':
            print(f"Title:{details['title']},Author:{details['author']},ISBN:{isbn},states:{details['status']},date_time:{details['date_time']}")
            print()
        else:
            print()

#This is for display all borrowed books in library.
def view_borrowed_book():    
    for isbn, details in B_details.items():
        if details['status']=='Borrowed':
            print(f"Title:{details['title']},Author:{details['author']},ISBN:{isbn},states:{details['status']},date_time:{details['date_time']}")
            print()

        else:
            print()

#Format
while True:
    print("------------------------Welcome To Python Library Managment System---------------------------------")
    print("1. Add new book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. View available books")
    print("5. View borrowed bokks")
    print("6. Exit")

    select= input("Select an option:")

    if select =='1':
        add_new_book()

    elif select == '2':
        borrow_book()
    elif select =='3':
        return_book()
    elif select == '4':
        view_available_book()
    elif select == '5':
        view_borrowed_book()
    elif select == '6':
        break
    else:
        print("***Invalide option.please select a valid option.***")
