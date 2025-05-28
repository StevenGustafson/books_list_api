from flask import Flask, request
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

my_dict = read_json_file("book_list.json")

@app.route('/')
def info():
    message=my_dict['about']
    return message 

@app.route('/all_books')
def all_books():
    result = [] 
    for b in my_dict['entries']:
       new = {}
       new['title']=b['title'] 
       new['author']=b['author'] 
       result.append(new) 
    return result 

def is_it_true(value):
    return value.lower() == 'true'

@app.route('/books')
def books():
    author = request.args.get('author') 
    read = request.args.get('read',default=False, type=is_it_true) 
    
    result = [] 
    
    for b in my_dict['entries']:
       if author == b['author']: 
          if read == b['read']: 
             new = {}
             new['title']=b['title'] 
             new['author']=b['author'] 
             result.append(new) 
    return result 


