# from routes.user import router as UserRouter
# from routes.project import router as ProjectRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transactions import router as TransactionRouter


app = FastAPI(debug=True)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TransactionRouter, tags=["transaction"], prefix="/transaction")

# app.include_router(ProjectRouter, tags=["Project"], prefix="/project")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Transaction Health Service!"}
