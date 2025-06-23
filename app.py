#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from amazon_webscrp import search_amazon

#load dataset
books = pd.read_csv('Data/Books.csv')
users = pd.read_csv('Data/Users.csv')
ratings = pd.read_csv('Data/Ratings.csv')



#layout of the streamlit page

st.set_page_config(layout="wide")

st.header('Welcome to the Book Recommender System! 📚')
st.markdown('''
            ##### This site using colaborative filtering to recommend books from our catalog.
            
            ''')


# Load the model
popular = pickle.load(open('popular.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_score.pkl', 'rb'))


st.sidebar.title("📚Book Recommender System")
# st.sidebar.markdown('---')




st.button('SHOW BOOKS')
st.markdown('''
                ##### We recommend Top 100 Books📚 for everyone as well.
                ''')
num_rows = 20
cols_per_row = 5
for row in range(num_rows):
        cols =st.columns(cols_per_row)
        for col in range(cols_per_row):
            book_idx = row * cols_per_row + col
            if book_idx < len(popular):
                with cols[col]:
                    st.image(popular.iloc[book_idx]['Image-URL-M'])#display image
                    st.text(popular.iloc[book_idx]['Book-Title'])#display title
                    st.text(popular.iloc[book_idx]['Book-Author'])#display author name

st.sidebar.badge('📚Top 100 Books')


#Function to recommend books
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key = lambda x : x [1], reverse = True)[1:11]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return data

#this is giving me names list  of books
book_list = pt.index.values

# #drop to select book
# Sidebar
st.sidebar.markdown('---')
st.sidebar.badge('Similar 📚Books Suggestions')
selected_book = st.sidebar.selectbox('Select a book from the Dropdown', book_list)

# Button to trigger recommendation (set flag and cache data)
if st.sidebar.button('Recommend Me'):
    st.session_state.book_recommendations = recommend(selected_book)
    st.session_state.recommend_triggered = True

# Main content area
if st.session_state.get('recommend_triggered', False):
    st.markdown('### Based on your selection, we recommend the following books:')
    
    book_recommendations = st.session_state.book_recommendations
    
    titles = []
    authors = []

    rows = 2
    cols_per_row = 5

    for row in range(rows):
        columns = st.columns(cols_per_row)
        for col_index in range(cols_per_row):
            book_index = row * cols_per_row + col_index
            if book_index < len(book_recommendations):
                with columns[col_index]:
                    st.image(book_recommendations[book_index][2])
                    st.text(book_recommendations[book_index][0])
                    st.text(book_recommendations[book_index][1])
                titles.append(book_recommendations[book_index][0])
                authors.append(book_recommendations[book_index][1])


    # Summary + Buy link section
    st.markdown("---")
    st.markdown("### Want more about one of the recommended books?")
    selected_book_title = st.selectbox("📕 Select Book Title", titles)
    selected_book_author = st.selectbox("👤 Select Book Author", authors)

    #col1, col2 = st.columns(2)

    # with col1:
    if st.button("📖Generate Summary"):
                from agents import generate_summary
                with st.spinner("Generating summary..."):
                            summary = generate_summary(selected_book_title, selected_book_author)
                            st.success("Summary:")
                            st.write(summary)

    # with col2:
    #     if st.button("🛒🔗 Get Purchase Links"):
    #         from agents import generate_buy_links
    #         with st.spinner("Fetching buying links..."):
    #             links = generate_buy_links(selected_book_title, selected_book_author)
    #             st.success("Purchase Links:")
    # #             st.write(links)
    # with col2:
    #     if st.button("🛒🔗 Get Purchase Link"):
    #         with st.spinner("Searching Amazon..."):
    #             link = search_amazon(selected_book_title, selected_book_author)
    #             st.success("Purchase Link:")
    #             st.markdown(f"[🔗 Buy on Amazon]({link})")


#import data
# books = pd.read_csv('Data/Books.csv') #books data
# users = pd.read_csv('Data/Users.csv') #users data
# ratings = pd.read_csv('Data/Ratings.csv') #users rating data
# @st.cache_data
# def load_data():
#     books = pd.read_csv('Data/Books.csv')
#     users = pd.read_csv('Data/Users.csv')
#     ratings = pd.read_csv('Data/Ratings.csv')
#     return books, users, ratings

# Load data once
#books, users, ratings = load_data()

# # Display the dataset
# st.sidebar.markdown('---')
# st.sidebar.badge('📊 Dataset Overview')
# if st.sidebar.button('Show Dataset'):
#     st.markdown('''
#                 ##### Here is the dataset we used to train our model.
#                 ''')
#     st.subheader("Books Dataset")
#     st.dataframe(books)  # Display the first few rows of the books dataset
#     st.markdown('---')
#     st.subheader("Users Dataset")
#     st.dataframe(users)   # Display the first few rows of the users dataset
#     st.markdown('---')
#     st.subheader("Ratings Dataset")
#     st.dataframe(ratings) # Display the first few rows of the ratings dataset



