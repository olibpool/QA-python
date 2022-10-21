books = {
        'JK Rowling': ['Harry Potter & the Philoshopers stone', 'Harry Potter & the Chamber of Secrets', 'Harry Potter & Prisoner of Askaban'],
        'Stephen King': ['IT', 'The Ring'],
        'Stephen Hawking': ['A short history of Time', 'A short history of Time'],
        'JRR Tolkein': ['The Lord of the Rings, The Two Towers', 'The Lord of the Rings, Entrance to Mordor'],
        'Oli': ['Olis big book of cool facts about himself']
    }


def books_function():
    author = input("Input an author's name: ")
    
    output = ''
    
    for book in sorted(books[author]):
        output += book + ', '
    
    return output


print(books_function())
    
    
    
