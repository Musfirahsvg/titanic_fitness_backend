from fastapi import FastAPI
from routes.workout_routes import workout_routes
from routes.auth_routes import auth_router
from fastapi.middleware.cors import CORSMiddleware #what sevrer communicate with each other, a security measurement 


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    workout_routes,
    prefix = "/workouts",
    tags = ["Workouts"]
)
app.include_router(
    auth_router,
    prefix = "/auth",
    tags = ["Auth"]
    
)



@app.get("/")
def test():
    return{"hello":"World"}