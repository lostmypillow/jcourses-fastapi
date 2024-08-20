from fastapi import FastAPI
from scrapers import *
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "https://jcourses-fastapi-latest.onrender.com",
     "https://lostmypillow.github.io",
     "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/courses/")
async def root(year: int = 0, sem: int = 0, dep_code: str = "", dep_year_code: int = 0 ):
    all_data = {}
    if year == 0:
        all_data["all_years"] = await get_sem()
    if year != 0 and sem != 0:
        all_data["year"] = year
        all_data["sem"] = sem
        all_data["deps"] = await get_departments(year, sem)
    if year != 0 and sem != 0 and dep_code != 0:
         all_data["dep_code"] = dep_code
         all_data["all_dep_year_codes"] = await get_all_dep_year_codes(year, sem, dep_code)
    if dep_year_code != 0:
        all_data["dep_year_code"] = dep_year_code
        all_data["courses"] = await get_courses(year, sem, dep_year_code)
    return all_data