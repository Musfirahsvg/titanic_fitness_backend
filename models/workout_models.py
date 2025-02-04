from pydantic import BaseModel
from typing import List, Dict 

class NewWorkout(BaseModel):
    exercise_name :str
    date : str
    reps : int
    weight : float
    user_email : str


class GetDay(BaseModel):
    user_email : str
    date : str
    
class ExerciseEntry(BaseModel):
    reps : int
    weight : float
    
    
    
class WorkoutDay(BaseModel):
    entries : Dict[str, List[ExerciseEntry]]
    
    
    
class Workouts(BaseModel):
    entries : Dict[str, List[ExerciseEntry]]
    
    
    
'''
workout : {
    "04/02/2024" : {
        "leg press"[
            {
                reps : 5, weight : 30}, {resp : 4, weight : 20}
        ],
        "chest press" : {
                reps : 5, weight : 30}, {resp : 4, weight : 20}
        }
    },
    203/02/2024" : {
        ...
    }
}
'''