from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# We'll import routers here later (auth, transactions, categories, insights)
# from app.routers import auth, transactions, categories, insights

# --- Create the FastAPI app ---
app = FastAPI(
    title="AI Finance Tracker",
    description="Track income & expenses with AI-powered categorization",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows your React frontend (running on a different port) to talk to this backend.
# Without this, the browser will block requests from the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default dev port
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allow all headers (including Authorization for JWT)
)

# --- Register Routers ---
# Each router handles a group of related endpoints.
# We'll uncomment these one by one as we build each module.

# app.include_router(auth.router,         prefix="/api/auth",         tags=["Auth"])
# app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])
# app.include_router(categories.router,   prefix="/api/categories",   tags=["Categories"])
# app.include_router(insights.router,     prefix="/api/insights",     tags=["Insights"])


# --- Health Check ---
# A simple endpoint to confirm the server is running.
# Visit http://localhost:8000/ in your browser to test it.
@app.get("/")
def root():
    return {"message": "AI Finance Tracker API is running 🚀"}
