# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

def main():
    gautam_lib=library(["Harry Potter","Think and grow rich","a","abcd defg","Attack on titan","Rich dad poor dad","Atomic habits"],"Gautam Library")

    print("Welcome to Gautam Library\nPress 1 to display books availabe.\nPress 2 to lend the book.\nPress 3 to add the book.\nPress 4 to return the book.\nPress e for exit.")

    while(True):
        # print(library.temp(gautam_lib))
        inp_inloop=str(input())

        if(inp_inloop=="1"):
            print(library.display_book(gautam_lib))

        elif(inp_inloop=="2"):
            print(library.lend_book(gautam_lib))

        elif(inp_inloop=="3"):
            library.add_book(gautam_lib)

        elif(inp_inloop=="4"):
            print(library.return_book(gautam_lib))

        elif(inp_inloop=="5"):
            print(library.reference_for_listofbooks)
            
        elif(inp_inloop=="e"):
            exit()
        else:
            print("Enter valid input\n")

class library():
    dict_to_rem={"Name":[],"Name of book":[]}
    reference_for_listofbooks=[]
    def __init__(self,listofbooks,library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name
        # library.list_of_books.append(self.listofbooks)
        library.reference_for_listofbooks = (self.listofbooks).copy()

    def display_book(self):
        return self.listofbooks
    
    # This function will remember the name of person that borrow books
    def borrow_remember(str1,str2):
        library.dict_to_rem["Name"].append(str1)
        library.dict_to_rem["Name of book"].append(str2)
        # print(dict_to_rem)
        return library.dict_to_rem

    def lend_book(self):
        lend= input("Enter the name of book you want\n")
        # Note: make such that lower case upper case dont matter
        for a in self.listofbooks:
            if lend in self.listofbooks:
                name_of_person=str(input("Enter your name\n"))
                library.borrow_remember(name_of_person,lend)
                self.listofbooks.remove(lend)
                return "Here you go"
        for b in library.reference_for_listofbooks:
            if lend not in library.reference_for_listofbooks:
                print(library.reference_for_listofbooks)
                return "Book not available in library"
        else:
            # library.borrow_remember(name_of_person,lend)
            print("Book not available. Given below is the info about who borrow it.\n")
            return  library.dict_to_rem
            

    # def temp(self):
    #     library.reference_for_listofbooks= (self.listofbooks).copy()
    #     return library.reference_for_listofbooks

    def add_book(self):
        add=str(input("Enter the name of book you want to donate\n"))
        self.listofbooks.append(add)
        for a in library.reference_for_listofbooks:
            if add not in library.reference_for_listofbooks:
                library.reference_for_listofbooks.append(add)

    
    def return_book(self):
        inp_return=str(input("Enter the name of book you want to return\n"))
        for book in library.reference_for_listofbooks:
            # print(self.listofbooks)
            # print("inside for loop of return")
            if inp_return in library.reference_for_listofbooks:
                self.listofbooks.append(inp_return)
                return "Thank you"
        else:
            return "some error"


main()