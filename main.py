import streamlit as st
import json

# load & save library data
def load_library():
    try:
        with open("library.json", "r") as file:  # r for read
            return json.load(file)       
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:  # w for write       
        json.dump(library, file, indent=4)

 #initialized library
library = load_library()

st.title("personal Library Manager 📚")
menu = st.sidebar.radio("Select an option", ["View Library", "Add Book", "Remove Book", "Search Book", "Save and Exit"])
if menu == "View Library":
    st.sidebar.title("Your Library")

    if library:
        st.table(library)
     
    else:
        st.write("😔 No Books in your library. Add some book 📗")

#add book
elif menu == "Add Book":
    st.sidebar.title("Add a new book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("year", min_value = 2022, max_value = 2100, step = 1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        library.append({"title":title, "author":author, "year":year, "genre":genre, "read_status": read_status})
        save_library()
        st.success("Book added sucessfully!")
        st.rerun()

#remove book
elif menu == "Remove Book":
    st.sidebar.title("Remove a book")
    book_titles = [book["title"] for book in library] 

    if book_titles:
        Selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != Selected_book] 
            save_library()
            st.success("Book remove suceesfully!")
            st.rerun()



#search book
elif menu == "Search Book":
    st.sidebar.title("Search a book")
    search_term = st.text_input("Enter title and author name")

    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book ["title"].lower() or search_term.lower() in book["author"].lower()]
        
        if results:
            st.table(results)

        else:
            st.warning("No book found! 😌")


#save and exit
elif menu == "Save and Exit":
     save_library() 
     st.success("Library saved successfully! 📗")               


