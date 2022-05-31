# Movie-Recommendation-System
With a team of 3 ,Created a user-friendly movie recommendation engine using content-based methods and visualized it by creating a web application
to give our target audience the ability to get a list of movie suggestions based on their movie interests.
Also created a GUI web application where users can enter a movie name they have watched, and the app will suggest the top 5 recommended movies.
# Design Architecture
<img width="412" alt="Screen Shot 2022-05-31 at 3 07 09 PM" src="https://user-images.githubusercontent.com/73665551/171275594-adb37e95-673f-4a35-ac11-9e67c6a1ed9f.png">

# Data Collection
Collected data by scrapping it using the beautifulsoup python library from IMDB webiste.
## Data Storage
After data is scraped from IMBD or load from the local PC, stream that data into  snowflake warehouse. 
Team connected to snowflake using a python connector to read data from our data warehouse and 
insert that data into a pandas data frame for our algorithm training. 
## AI Algorithm
Compared with collaborative filtering algorithms, content-based system reduces the diversity of recommendations, but whether the user has rated the movie does not affect the result. Besides, as collaborative filtering needs user behavior data which we didn’t extract them from the IMDB website, so we choose content-based algorithms in our project.
Our recommendation system works of a movie dataset, the dataset consists of variables such as Title, Director, Genre, Description, and Cast. The data variables are used to create a model that scores each variable and tries to return a list of similar movies based on the input movie.
In our project, based on the Content-based AI Algorithm, we construct the combined features of natural language, calculate the number of occurrences of each word using TfidfVectorizer as feature vector, and build the similarity between all movies using cosine similarity.
## Web App
For our GUI we used Streamlit to create a web application. Streamlit is an open-source framework that runs in python, it helped us create our web application as it allows for compatibility with machine learning and AI libraries (Introduction to Streamlit).
![image](https://user-images.githubusercontent.com/73665551/171276204-5f7fa884-e8da-44df-80db-8afed25eebcd.jpeg)

Python Package to Install
!pip install snowflake
!pip install snowflake-connector-python
Ps: if you met error when installing it, you may try to use:
pip install --user snowflake-connector-python 
!pip install snowflake-sqlalchemy
Ps: if you met error when installing it, you may try to use:
pip install –user snowflake-sqlalchemy
!pip install streamlit
!pip install bs4
Steps to Run Code
1.	Run the web scrapping notebook (scrapecodenew_snowflake_v3.ipynb) line by line to collect data and stream it to snowflake.
a.	Run the AI code line by line to generate pickle files that will be used by the web app.
2.	Run the web app python file (movie_v1.py)
3.	The above step will open up a localhost web page to our recommendation system.


