<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>AI-Powered Book Recommendation System</title>
</head>
<body>
  <h1>📚 AI-Powered Book Recommendation System</h1>
  <p>
    A web-based intelligent book recommendation app built with <strong>Streamlit</strong> that recommends books based on similarity scores and allows users to:
  </p>
  <ul>
    <li>📘 View the dataset used</li>
    <li>📖 Get book summaries via an AI agent</li>
    <li>🛒 Find purchase links on Amazon</li>
  </ul>

  <hr />

  <h2>🚀 Features</h2>
  <ul>
    <li>🔍 <strong>Book Recommendation</strong>: Get top 10 similar books using collaborative filtering.</li>
    <li>🤖 <strong>AI Summary Generator</strong>: Get concise summaries using OpenAI's API.</li>
    <li>🛒 <strong>Amazon Purchase Links</strong>: Automatically fetches an Amazon link for each recommended book.</li>
    <li>📊 <strong>Dataset Viewer</strong>: Inspect books, users, and ratings datasets used to train the model.</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
📁 recommendation-system/
│
├── 📄 app.py                  # Main Streamlit app
├── 📁 pages/
│   └── dataset.py            # Dataset display logic
│
├── 📄 books.pkl              # Pickled DataFrames for recommendation
├── 📄 pt.pkl
├── 📄 similarity_score.pkl
├── 📄 popular.pkl
│
├── 📄 agents.py              # AI functions for summary and purchase links
├── 📄 amazon_scraper.py      # Amazon scraping with BeautifulSoup
│
├── 📁 Data/
│   ├── Books.csv
│   ├── Users.csv
│   └── Ratings.csv
│
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md              # Project documentation
  </pre>

  <h2>⚙️ Installation</h2>
  <ol>
    <li>Clone the repo:<br />
      <code>git clone https://github.com/yourusername/recommendation-system.git</code><br />
      <code>cd recommendation-system</code>
    </li>
    <li>(Optional) Create a virtual environment:<br />
      <code>python3 -m venv .venv</code><br />
      <code>source .venv/bin/activate</code>
    </li>
    <li>Install dependencies:<br />
      <code>pip install -r requirements.txt</code>
    </li>
    <li>Run the app:<br />
      <code>streamlit run app.py</code>
    </li>
  </ol>

  <h2>🧠 AI Agents</h2>
  <ul>
    <li><strong>Summary generation</strong> uses OpenAI's GPT model.</li>
    <li><strong>Purchase link extraction</strong> uses BeautifulSoup to scrape Amazon search results.</li>
    <li>Make sure to configure your API keys properly inside <code>agents.py</code>.</li>
  </ul>

  <h2>📷 Screenshots</h2>
  <p>
    <img src="https://github.com/S-AILAB/Book-Recommender-AI/blob/main/Screenshot%202025-06-13%20at%206.00.00%E2%80%AFPM.png" alt="Book Recommendation UI" width="700" />
  </p>
  <p>
    <img src="https://github.com/S-AILAB/Book-Recommender-AI/blob/main/Screenshot%202025-06-13%20at%206.00.41%E2%80%AFPM.png" width="700" />
  </p>

  <h2>🛠 Tech Stack</h2>
  <ul>
    <li>Python, Pandas, NumPy</li>
    <li>Streamlit for UI</li>
    <li>scikit-learn for similarity engine</li>
    <li>BeautifulSoup for web scraping</li>
    <li>OpenAI API for book summaries</li>
  </ul>

  <h2>🙋‍♂️ Author</h2>
  <p>Made with ❤️ by <strong>Siddharth Jain</strong></p>

  <h2>Contact</h2>
  <p>https://www.linkedin.com/in/siddharth-jain-8b56a2321/</p>
</body>
</html>
