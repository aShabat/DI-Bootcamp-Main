// 👩‍🏫 👩🏿‍🏫 What You’ll learn
//
//     How to design and use TypeScript classes and interfaces.
//     How to apply access modifiers to control access to properties and methods.
//     How to use optional and readonly properties in interfaces.
//     How to implement basic inheritance to extend class functionality.
//
//
// Instructions
//
// Create a simple library system with TypeScript:
//
//     Interface Book: Define an interface Book with the following properties:
//         title (string)
//         author (string)
//         isbn (string)
//         publishedYear (number)
//         An optional genre property (string)
//
//     Class Library: Create a class Library with:
//         A private property books (array of Book).
//         A public method addBook to add a new book to the library.
//         A public method getBookDetails that returns details of a book based on the isbn.
//
//     Class DigitalLibrary: Create a class DigitalLibrary that extends Library and adds:
//         A readonly property website (string) for the library’s website.
//         A public method listBooks that returns a list of all book titles in the library.
//
// Create an instance of DigitalLibrary, add some books to it, and then print out the details of the books and the list of all book titles

interface Book {
  title: string;
  author: string;
  isbn: string;
  publishedYear: number;
  genre?: string;
}

class Library {
  protected books: Book[];
  public addBook(book: Book) {
    this.books.push(book);
  }
  public getBookDetails(isbn: string) {
    const book = this.books.find((b) => b.isbn === isbn);
    if (book !== undefined) {
      return `title: ${book.title}; author: ${book.author}; published: ${book.publishedYear};` +
        book.genre !==
        undefined
        ? `genre: ${book.genre};`
        : "";
    } else {
      return "Book Not Found";
    }
  }
}

class DigitalLibrary extends Library {
  readonly website: string;
  public listBooks() {
    return this.books.map((b) => b.title);
  }
}
