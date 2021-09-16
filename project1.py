class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self. lenDict = {}

    def displayBooks(self):
        print(f"We have following books in our libraray: {self.name}")
        for book in self.bookList:
            print(book)

    def lenBook(self, user, book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("Lender book database has been updated. You can take your book now")
        else:
            print(f"Book is already being used by {self.lenDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to list")

    def returnBook(self, book):
        self.lenDict.pop(book)


if __name__ == '__main__':
    nizam = Library(['Python', 'Cpp', 'React', 'JavaScript'], "Nizamuddin Mondal")

    while(True):
        print(f"Wecome to the {nizam.name} library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()

        if user_choice not in ['1','2','3','4']:
            print("Plz enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice==1:
            nizam.displayBooks()

        elif user_choice==2:
            book = input("Enter the name of book you wnat to lend:")
            user = input("Enter your name")
            nizam.lenBook(user, book)

        elif user_choice==3:
            book = input("Enter the name of book you wnat to add:")
            nizam.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of book you wnat to return:")
            nizam.returnBook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue


