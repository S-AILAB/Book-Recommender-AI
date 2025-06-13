# 📚 AI-Powered Book Recommendation System

A web-based intelligent book recommendation app built with **Streamlit** that recommends books based on similarity scores and allows users to:

- View the dataset used
- Get book summaries via an AI agent
- Find purchase links on Amazon

---

## 🚀 Features

- 🔍 **Book Recommendation**: Select a book and get top 10 similar recommendations using collaborative filtering.
- 🤖 **AI Summary Generator**: Get concise summaries using OpenAI's API.
- 🛒 **Amazon Purchase Links**: Auto-fetches a direct Amazon purchase link for each recommended book.
- 📊 **Dataset Viewer**: Inspect books, users, and ratings datasets used to train the model.

---

## 📂 Project Structure

📁 recommendation-system/
│
├── 📄 app.py # Main Streamlit app
├── 📁 pages/ # Contains multipage Streamlit views
│ └── dataset.py # Dataset display logic
│
├── 📄 books.pkl # Pickled DataFrames for recommendation
├── 📄 pt.pkl
├── 📄 similarity_score.pkl
├── 📄 popular.pkl
│
├── 📄 agents.py # AI agent functions for summary and purchase links
├── 📄 amazon_scraper.py # Function to fetch Amazon URLs using BeautifulSoup
│
├── 📁 Data/
│ ├── Books.csv
│ ├── Users.csv
│ └── Ratings.csv
│
├── 📄 requirements.txt # List of Python dependencies
└── 📄 README.md # Project documentation



---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/recommendation-system.git
   cd recommendation-system
Create a virtual environment (optional but recommended)


python3 -m venv .venv
source .venv/bin/activate
Install dependencies


pip install -r requirements.txt
Run the app


streamlit run app.py
🧠 AI Agents
Summary generation uses OpenAI's GPT model.

Purchase link extraction uses BeautifulSoup to scrape Amazon for search results.

Make sure to configure your API keys properly inside agents.py.

📷 Screenshot
![Book Recommendation Screenshot](/Users/siddharthjain/Desktop/SJ/cuvette/python ML program/Add On Projects/📚Recommendation System by me/Screenshot 2025-06-13 at 6.00.00 PM.png)

![AI Summary](/Users/siddharthjain/Desktop/SJ/cuvette/python ML program/Add On Projects/📚Recommendation System by me/Screenshot 2025-06-13 at 6.00.41 PM.png)

🛠 Tech Stack
Python, Pandas, NumPy

Streamlit for UI

scikit-learn for similarity engine

BeautifulSoup for web scraping

OpenAI API for book summaries

🙋‍♂️ Author
Made with ❤️ by Siddharth Jain

📜 License
This project is licensed under the MIT License