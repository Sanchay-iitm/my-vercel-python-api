# tds_q9.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS for all origins (Allows any frontend to access this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load CSV file
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    """
    Fetch student data from the CSV. If 'class' query parameters are provided,
    filter students by those classes.
    """
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    # Convert to dictionary list
    students = filtered_df.to_dict(orient="records")
    return {"students": students}
