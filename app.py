from flask import Flask, request, Response
import mariadb
import json
import random 


app = Flask(__name__)

animal_list1 =[{"snake, horse, turtle, bear, wolf"}]

animal_list2 =[{"snake, buffalo, frog, cat, musk ox, caribou, moose"}]

@app.route("/getAnimal", methods=["GET", "POST", "PATCH","DELETE"])

def animals():
    if request.method == "GET":
        return Response(json.dumps(animal_list1, default=str), mimetype="application/json", status=201,)
   
    elif request.method == "POST":
        return Response(json.dumps(animal_list2, default=str), mimetype="application/json", status=205,)
    
    elif request.method == "PATCH":
        return Response("the snake turned into a toad", mimetype="json/application", status=205,)
    
    elif request.method == "DELETE":
        return Response("the snake is gone", mimetype="json/application", status=205,)

    
    
    
    
   
         

     
