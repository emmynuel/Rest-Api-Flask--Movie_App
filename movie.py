from flask import Flask, request
app = Flask(__name__)
in_memory_datastore = {
   "Blood_Sisters" : {"name": "Blood_Sisters", "released_year": 2022, "rating": 6.5, "genre": "educative"},
   "Alive" : {"name": "Alive", "released_year": 2008, "rating": 9.0, "genre": "crime"},
   "Golden" : {"name": "Golden", "released_year": 2003, "rating": 5.6, "genre": "comedy"},
   "Midnight" : {"name": "Midnight", "released_year": 2004,"rating": 6.0, "genre": "horror"},
   "Gangstar" : {"name": "Gangstar", "released_year": 2003, "rating": 10.0, "genre": "crime"},
   "Dare" : {"name": "Dare", "released_year": 2020, "rating": 7.5, "genre": "comedy"},
   "Our_father" : {"name": "Our_father", "released_year": 2009, "rating": 6.5, "genre": "documentary"},
   "Pray" : {"name": "Pray", "released_year": 2021, "rating": 7.5, "genre": "religion"},
}
@app.get('/movie_store')
def list_movie_store():
   return {"movie_store":list(in_memory_datastore.values())}
@app.route('/movie_store/<movie_desc_name>')
def get_movie_desc(movie_desc_name):
   return in_memory_datastore[movie_desc_name]
    
    
