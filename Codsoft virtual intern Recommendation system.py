# ================================
# BOOK RECOMMENDATION SYSTEM
# ================================

import random

books = {
    "Fantasy": [
        {"name": "Harry Potter", "author": "J.K. Rowling", "rating": 4.9},
        {"name": "The Hobbit", "author": "J.R.R. Tolkien", "rating": 4.8}
    ],

    "Mystery": [
        {"name": "Sherlock Holmes", "author": "Arthur Conan Doyle", "rating": 4.7},
        {"name": "Gone Girl", "author": "Gillian Flynn", "rating": 4.5}
    ],

    "Self-help": [
        {"name": "Atomic Habits", "author": "James Clear", "rating": 4.9},
        {"name": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "rating": 4.6}
    ],

    "Romance": [
        {"name": "Pride and Prejudice", "author": "Jane Austen", "rating": 4.8},
        {"name": "Me Before You", "author": "Jojo Moyes", "rating": 4.6}
    ],

    "Science Fiction": [
        {"name": "Dune", "author": "Frank Herbert", "rating": 4.7},
        {"name": "The Martian", "author": "Andy Weir", "rating": 4.8}
    ]
}

def show_genres():
    print("\nAvailable Genres:")
    
    for genre in books:
        print("-", genre)

def recommend_books():
    
    show_genres()

    genre_choice = input("\nEnter your favorite genre: ")

    if genre_choice in books:

        print("\nRecommended Books For You 📚")
        print("--------------------------------")

        for book in books[genre_choice]:

            print("Book Name :", book["name"])
            print("Author    :", book["author"])
            print("Rating    :", book["rating"], "⭐")
            print()

    else:
        print("\nGenre not found!")

def show_all_books():

    print("\nAll Available Books 📖")
    print("--------------------------------")

    for genre in books:

        print("\n", genre)

        for book in books[genre]:
            print("-", book["name"])

def random_book():

    genre = random.choice(list(books.keys()))
    book = random.choice(books[genre])

    print("\nRandom Book Suggestion 🎲")
    print("--------------------------------")
    print("Book   :", book["name"])
    print("Author :", book["author"])
    print("Genre  :", genre)
    print("Rating :", book["rating"], "⭐")

while True:

    print("\n========== BOOK RECOMMENDATION SYSTEM ==========")
    print("1. Recommend Books By Genre")
    print("2. Show All Books")
    print("3. Random Book Suggestion")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        recommend_books()

    elif choice == "2":
        show_all_books()

    elif choice == "3":
        random_book()

    elif choice == "4":
        print("\nThank you for using the system 😊")
        break
    
    else:
        print("\nInvalid choice! Please try again.")
