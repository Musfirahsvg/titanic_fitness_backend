import json
from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.workout_models import GetDay
from .auth_routes import get_all_users


workout_routes = APIRouter()

def get_all_workouts():
    with open("./fake_db/workouts.json", "r") as file:
        return json.load(file)


@workout_routes.get("/")
def all_workouts():
    with open ("./fake_db/workouts.json", "r") as file:
        workouts = json.load(file)
        
    return workouts

class Workout(BaseModel):
    name: str
    exersice: List[str]


@workout_routes.post("/")
def add_workouts(new_workout: Workout):
    all_workouts = get_all_workouts()
    
    
    all_workouts.append(
        new_workout.model_dump()
    )
    
    
    with open("./fake_db/workouts.json", "w" )as file:
        file.write(json.dumps(all_workouts, indent=4))
        
    return all_workouts


@workout_routes.post("/workout_day")
def get_workout_day(data: GetDay):
    #find the user
    all_users = get_all_users()
    
    user = all_users[data.user_email]
    
    #check if the user exists, if not, give error back    
    if user:
        raise HTTPException(404, "No User Found")
    
    #get workout day
    workouts = user["workouts"]
    

    day = workouts.get(data.date, {})
    return day
    #get allows us to specify a default if it doesn't exist
    
    #if workout day doesn't exist, what do we do?
    #we make one and save it
    
    #return the workout object to the user
    
