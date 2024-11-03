# class Student:
#     userName="Chinmaya17"
#     def __init__(self,rollNo,userId):
#         self.rollNo=rollNo
#         self.userId=userId
#         print(f"{self.userName} and {rollNo} and {userId}")
#     def isOpen(self):
#         print(f"CLose {self.userId}")

# student1=Student("121201",101010)
# student1.isOpen()

# class Account:
#     def __init__(self):
#         self.accountNo=35885078538
#         self.balance=4313
    
#     def credit(self,money):
#         self.balance+=money
#         print(f"{money}Rs Credited to your Account No {self.accountNo}")
#     def debit(self,money):
#         self.balance-=money
#         print(f"{money}Rs Debited to your Account No {self.accountNo}")
#     def totalBal(self):
#         print(f"your {self.accountNo} total balance {self.balance}")

# account1=Account()
# account1.credit(100)
# account1.debit(200)
# account1.totalBal()

class Book:
    library_name="SUPERCHARGED"

    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies
    def borrow_book(self):
        if(self.copies>=1):
            self.copies-=1
            print(f"borrow one book and no of book availabel: {self.copies}")
        else:
            print("Sorry, this book is not available.")
    def return_book(self):
        self.copies+=1
        print(f"one book added and no of book availabel: {self.copies}")
    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies:{self.copies}")

book1=Book("ChinmayaStory","Chinu",34)
book2=Book("NeverGiveUp","Chinmaya",1)
book1.borrow_book()
book2.return_book()
book2.borrow_book()
book2.borrow_book()
book2.borrow_book()
book2.return_book()
book1.book_info()
book2.book_info()
