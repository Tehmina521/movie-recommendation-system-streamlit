# 🎬 Movie Recommendation System using Content-Based Filtering

## 📌 Overview
This project builds a **Content-Based Movie Recommendation System** that suggests movies similar to a user-selected movie based on their **genre information**.  

The system uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert textual genre data into numerical vectors and applies **Cosine Similarity** to measure similarity between movies.  

An interactive **Streamlit Graphical User Interface (GUI)** is also developed so users can easily input a movie title and receive recommendations.

---

## 🎯 Problem Statement
With the increasing number of movies available on streaming platforms, users often face difficulty finding movies that match their interests. Manually browsing through thousands of movies is inefficient and time-consuming.

To solve this problem, recommendation systems are used to automatically suggest relevant movies. A **content-based recommendation system** analyzes the features of movies (such as genres) and recommends movies that are most similar to the one selected by the user.

---

## 🚀 Project Objective
The main objectives of this project are:

- Build a **content-based recommendation model** using movie genre information.
- Convert textual genre features into numerical vectors using **TF-IDF**.
- Compute similarity between movies using **Cosine Similarity**.
- Recommend the **top 5 most similar movies** for a given movie.
- Develop a **Streamlit GUI** to allow users to interact with the recommendation system easily.

---

## 📂 Dataset
Dataset used: **movies.csv**  

The dataset contains movie information including:

| Column | Description |
|------|-------------|
| movieId | Unique identifier for each movie |
| title | Movie title |
| genres | Genre categories of the movie |


---

## ⚙️ Technologies Used

- Python
- pandas
- scikit-learn
- Streamlit
- joblib
- Jupyter Notebook

---

## 🧠 Methodology

The following steps were used to build the recommendation system:

1. Load the **movies.csv dataset**.
2. Perform **data exploration and cleaning**.
3. Convert movie genres into **TF-IDF feature vectors**.
4. Compute **cosine similarity matrix** to measure similarity between movies.
5. Build a **recommendation function** that returns the top 5 similar movies.
6. Develop an **interactive Streamlit GUI** for user input and displaying recommendations.

---



---

## 💻 Installation

Clone the repository:

https://github.com/Tehmina521/movie-recommendation-system-streamlit
cd task2
Install dependencies:
pip install -r requirements.txt

---

## ▶️ Running the Application

Run the Streamlit application:
streamlit run app.py


After running the command, the application will open in your browser.

---

## 🖥️ How to Use

1. Enter a **movie title** in the input box.
2. Click the **Recommend** button.
3. The system will display the **Top 5 most similar movies** with similarity scores.

---

## 📊 Example Output

| Movie | Similarity Score |
|------|------------------|
| Toy Story 2 | 0.93 |
| A Bug's Life | 0.89 |
| Monsters, Inc. | 0.86 |
| Shrek | 0.84 |
| Finding Nemo | 0.82 |

---

## Screenshot
<img width="1366" height="687" alt="Screenshot (935)" src="https://github.com/user-attachments/assets/950ab3c2-9e7d-43f3-9dff-75a3be4da455" />

---

<img width="1366" height="691" alt="Screenshot (936)" src="https://github.com/user-attachments/assets/e8295dd4-9fba-4c1c-89fc-b9c6b00ddc15" />

---


## ✅ Conclusion
This project demonstrates how a **content-based recommendation system** can be built using **TF-IDF vectorization** and **cosine similarity**.  

By integrating the model with a **Streamlit GUI**, users can easily interact with the system and receive personalized movie recommendations.  

The system can be further improved by incorporating additional features such as **movie descriptions, user ratings, or hybrid recommendation techniques**.

---

## 👩‍💻 Author

**Tehmina Afzal**-AI & Data Science Intern at ITSOLERA PVT LTD.
