from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"ФИО": "Бирюк Мария Денисовна"}

@app.get("/users")
async def root_T():
    return {"Телефон": "89831084548"}

@app.get("/tools")
async def root_M():
    return {"Навыки": "Знание языков программирования, таких как Python, C++. Опыт работы с базами данных и SQL."}