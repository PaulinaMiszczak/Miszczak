class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer():
    book = "" 
    haveBook = False
    def requestBook(self, book): # klient może zapytać o książę
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): # albo zwrócić jeśli posiada
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False

def setup():
    size(220,100)
    global library, Rysiek
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter","Sklepik z niespodzianka"]
    library = Library(books)
    Madzia = Customer()
    Rysiek = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked():  
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Rysiek.requestBook("Naocznosc")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Rysiek.returnBook())
            
        
        
import unittest

class MojeTesty(unittest.TestCase):# nazwy powinny mówić co robią, ale nie  tak ogólnie
    
    def test_liczba_ksiazek(self): # nazwy testó muszą zaczynać się od test, o czym zapomniałam wspomnieć
        ksiazki = ["Naocznosc", "Sens Sztuki", "Harry Potter","Sklepik z niespodzianka"]
        mylibrary = Library(ksiazki)# skoro testujemy kod, to wypadałoby go użyć, zamiast pisać nowy - skorzystać z napisanych klas
        result = len(mylibrary.availableBooks)
        self.assertNotEqual(result, 3)

    def test_kolejnosc_ksiazki(self):
        ksiazki = ["Naocznosc", "Sens Sztuki", "Harry Potter","Sklepik z niespodzianka"]
        mylibrary = Library(ksiazki)
        result = sorted(mylibrary.availableBooks) # tu testujesz funkcję sortującą, nie klasy
        self.assertEqual(result, ["Harry Potter", "Naocznosc", "Sens Sztuki", "Sklepik z niespodzianka"])


if __name__ == '__main__':
    unittest.main()
        
# 1,5pkt    
