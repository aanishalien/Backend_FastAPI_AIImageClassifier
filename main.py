from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase_client import supabase
from models import User
from routes.predicts import router
from auth import hash_password,verify_password,pwd_context

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
def get_users():
    result = supabase.table("users").select("*").execute()
    return result.data

@app.post("/api/v1/users")
async def create_user(user: User):
    try:
        result = supabase.table("users").select("*").eq("email", user.email).execute()
        existing_user = result.data or []

        
        if existing_user:
            first_user = existing_user[0]
            if pwd_context.verify(user.password, first_user["password"]):
                return {"message": "Logged in successfully"}
            else:
                return {"error": "Invalid password"}
            
        
        hashed_password = pwd_context.hash(user.password)
        supabase.table("users").insert({
            "email": user.email, 
            "password": hashed_password
        }).execute()
        return {"message": "User created successfully"}
        
        
            
    except Exception as e:
        return {"error": str(e)}


app.include_router(router, prefix="/api/v1/images", tags=["Image Prediction"])
