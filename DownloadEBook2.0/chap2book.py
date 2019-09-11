def chap2book(titles,book_name):
    with open(book_name + '.md', 'w', encoding='utf-8') as book:
        book.write("# " + book_name + '  \n')
        for i in range(len(titles)):
            f = open(titles[i] + '.md', encoding='utf-8')
            fs = f.read()
            book.write(fs + '  \n')
