author_name=input("Enter the author's name: ")

def search_books(author_name):
    try:
        with open("book.txt", "r") as file:
            found_books=[]
            
            for line in file:
                lines=line.strip().split(":")
                if len(lines)>=2 and lines.strip()==author_name:
                    found_books.append(lines)
            
            if not found_books:
                print("No books found by the required author name: ", author_name)
            else:
                print("Books found by the required author name: ", author_name, ": ")
                
                for book in found_books:
                    print("Title: ", book[0].strip())
                    print("Author: ", book[1].strip())
                    print("Genre: ", book[2].strip())
                    print("Year: ", book[3].strip())
                    
    except FileNotFoundError:
        print("book.txt file not found.")
        
        
        
search_books(author_name)
    
            
            