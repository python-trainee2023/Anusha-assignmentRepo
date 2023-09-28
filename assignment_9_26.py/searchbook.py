

def search_books(author_name):
    try:
        found_books=[]
        with open("book.txt", "r") as file:
            for line in file:
               title, author, genre, year  = line.strip().split(':')
               if author == author_name:
                    # found_books.append(title,author,genre,year)
                     found_books.append(title)
                     found_books.append(author)
                     found_books.append(genre)
                     found_books.append(year)
                    
            if found_books:
                print("Books found by the  author : ", author_name, ": ")
                
                for book in found_books:
                    print(f"title:{book} ")
                    print(f"author:{book} ")
                    print(f"genre:{book} ")
                    print(f"year:{book} ")
                    # print("Title: ", book[0].strip())
                    # print("Author: ", book[1].strip())
                    # print("Genre: ", book[2].strip())
                    # print("Year: ", book[3].strip())
            else:
                print("no books found by the author", author_name)
                    
    except FileNotFoundError:
        print("book.txt file not found.")
        
        
author_name=input("Enter the author's name: ")       
search_books(author_name.lower())
    
            
            