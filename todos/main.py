from fastapi import FastAPI
import uvicorn

app=FastAPI()

students = [{
    "userName":"Faheem",
    "rollNo": 2521
},
            {
    "userName":"Piaic class",
    "rollNo": 234535
},
            {
    "userName":"Piaic",
    "rollNo": 234535
}
            ]

@app.get("/getstudents")
def getstudents():
    global students
    return students
@app.get("/addstudent")
def addStudent(userName:str, rollNo:str):
   global students
   students.append({"userName":userName, "rollNo":rollNo})
   return students


@app.post("/students")
def getstudents():
    return students
@app.put("/updatestudents")
def updatestudents(userName:str,rollNO:str):
    global students
    
    return students
@app.delete("/deletestudents")
def deletestudents(userName:str):
    global students
    students.pop({userName})

    return students



def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)