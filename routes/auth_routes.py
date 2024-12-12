import json
from fastapi import APIRouter, HTTPException

from models.auth_models import RegisterForm


auth_router = APIRouter()

def get_all_users():
    with open("./fake_db/users.json", "r") as file:
        return json.load(file)
        

def save_users(new_users):
    with open(".fake_db/users.json", "w") as file:
        file.write(json.dumps(new_users, indent=4))    #difference between dumps and dump
        
        
@auth_router.post("/register")
def register(Register_data: RegisterForm):
    
    all_users = get_all_users()
    email = Register_data.email
    
    
    if email in all_users:
        raise HTTPException(409, "User already exists")
    
    new_user={
        "email": Register_data.email,
        "username":Register_data.username,
        "password": Register_data.password,    
    }
    
    all_users[email] = new_user
    save_users(all_users)
    return new_user
    


@auth_router.post("/login")
def login():
    return{}