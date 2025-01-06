from fastapi import FastAPI, Depends
from app.dependencies import container
from app.routers import main_router
from app.services.my_service import MyService

app = FastAPI()

def get_my_service() -> MyService:
    return container.get(MyService)

@app.get("/")
async def read_root(my_service: MyService = Depends(get_my_service)):
    result = my_service.do_something()
    return {"message": result}

app.include_router(main_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
