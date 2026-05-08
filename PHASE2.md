# 🎯 Phase 2: Authentication & Authorization

## Objective
Implement a secure, stateless authentication system using JWT. Users can register, login, and access protected routes. Tokens are managed client-side via React Context and persisted in `localStorage`.

---

## 🔙 Backend Implementation

### 1. Database & Migrations
- [ ] Run `alembic revision --autogenerate -m "add users table"`
- [ ] Verify `alembic/versions/xxxx_add_users.py` includes:
  ```python
  op.create_table('users',
    sa.Column('id', sa.String(), primary_key=True),
    sa.Column('email', sa.String(), unique=True, nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
  )
  ```
- [ ] Run `alembic upgrade head`

### 2. Models & Schemas
- [ ] **`backend/app/models/user.py`**
  ```python
  from sqlalchemy import Column, String, DateTime
  from sqlalchemy.sql import func
  from app.database import Base

  class User(Base):
      __tablename__ = "users"
      id = Column(String, primary_key=True, index=True)
      email = Column(String, unique=True, nullable=False, index=True)
      hashed_password = Column(String, nullable=False)
      full_name = Column(String)
      created_at = Column(DateTime, server_default=func.now())
  ```
- [ ] **`backend/app/schemas/user.py`**
  ```python
  from pydantic import BaseModel, EmailStr
  from typing import Optional
  from datetime import datetime

  class UserCreate(BaseModel):
      email: EmailStr
      password: str
      full_name: Optional[str] = None

  class UserLogin(BaseModel):
      email: EmailStr
      password: str

  class UserResponse(BaseModel):
      id: str
      email: str
      full_name: Optional[str]
      created_at: datetime
      class Config: from_attributes = True

  class Token(BaseModel):
      access_token: str
      token_type: str
  ```

### 3. Security & Utilities
- [ ] **`backend/app/utils/security.py`**
  ```python
  from passlib.context import CryptContext
  from jose import JWTError, jwt
  from datetime import datetime, timedelta
  from app.config import settings

  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

  def verify_password(plain: str, hashed: str) -> bool:
      return pwd_context.verify(plain, hashed)

  def get_password_hash(password: str) -> str:
      return pwd_context.hash(password)

  def create_access_token(data: dict) -> str:
      to_encode = data.copy()
      expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode.update({"exp": expire})
      return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
  ```

### 4. Auth Service
- [ ] **`backend/app/services/auth_service.py`**
  - `register_user(email, password, full_name)`: check uniqueness → hash password → save → return user
  - `authenticate_user(email, password)`: verify hash → create token → return `Token`
  - `get_current_user(token: str)`: decode JWT → query DB → raise `HTTPException` if invalid

### 5. Auth Router
- [ ] **`backend/app/routers/auth.py`**
  ```python
  from fastapi import APIRouter, Depends, HTTPException, status
  from fastapi.security import OAuth2PasswordBearer
  from sqlalchemy.orm import Session
  from app.database import get_db
  from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
  from app.services.auth_service import register_user, authenticate_user, get_current_user

  router = APIRouter(prefix="/api/auth", tags=["Auth"])
  oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

  @router.post("/register", response_model=UserResponse)
  def register(payload: UserCreate, db: Session = Depends(get_db)):
      return register_user(db, payload)

  @router.post("/login", response_model=Token)
  def login(payload: UserLogin, db: Session = Depends(get_db)):
      user = authenticate_user(db, payload)
      return user

  @router.get("/me", response_model=UserResponse)
  def get_me(current_user = Depends(get_current_user)):
      return current_user
  ```
- [ ] Update `backend/app/main.py` to include `router` and add CORS middleware for `http://localhost:5173`

---

## 🎨 Frontend Implementation

### 1. API Client Setup
- [ ] **`frontend/src/api/client.ts`**
  ```typescript
  import axios from 'axios';

  const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE_URL });

  api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  });

  api.interceptors.response.use(
    res => res,
    err => { if (err.response?.status === 401) localStorage.removeItem('token'); return Promise.reject(err); }
  );

  export default api;
  ```

### 2. Auth Context
- [ ] **`frontend/src/context/AuthContext.tsx`**
  - State: `user`, `token`, `isAuthenticated`
  - Actions: `login(email, password)`, `register(data)`, `logout()`
  - Persistence: Read/write `localStorage` on mount
  - Export: `useAuth()` hook

### 3. Pages & Routing
- [ ] **`frontend/src/pages/Login.tsx`**
  - Form: email, password
  - Submit → `auth.login()` → store token → redirect to `/dashboard`
  - Error handling & loading states
- [ ] **`frontend/src/pages/Register.tsx`**
  - Form: full_name, email, password, confirm_password
  - Submit → `auth.register()` → auto-login → redirect to `/dashboard`
- [ ] **`frontend/src/App.tsx`**
  - Wrap app in `AuthProvider`
  - Define routes:
    ```tsx
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
    <Route element={<PrivateRoute />}>
      <Route path="/dashboard" element={<Dashboard />} />
      {/* future routes */}
    </Route>
    <Route path="*" element={<Navigate to="/dashboard" />} />
    ```
  - Implement `PrivateRoute` wrapper checking `isAuthenticated`

### 4. Styling
- [ ] Apply Tailwind classes for form inputs, buttons, error messages, and loading spinners
- [ ] Ensure consistent spacing, focus states, and responsive layout

---

## 🧪 Testing & Validation

| Area | Checklist |
|------|-----------|
| **Backend** | ✅ Register with valid/invalid email<br>✅ Login with correct/incorrect credentials<br>✅ `GET /api/auth/me` with/without token<br>✅ Password hashing verified (stored hashed, not plain)<br>✅ CORS allows `localhost:5173` |
| **Frontend** | ✅ Form validation (required, email format, password match)<br>✅ Token stored on login/register<br>✅ Protected routes redirect to `/login` if unauthenticated<br>✅ Logout clears token & redirects<br>✅ Axios interceptor attaches token automatically |
| **Security** | ✅ JWT expiration matches `ACCESS_TOKEN_EXPIRE_MINUTES`<br>✅ No sensitive data in `localStorage`<br>✅ Backend validates email uniqueness before hashing |

---

## ✅ Phase 2 Deliverables Checklist
- [ ] `users` table exists & migrated
- [ ] `backend/app/models/user.py` & `schemas/user.py` complete
- [ ] `backend/app/utils/security.py` implements bcrypt & JWT
- [ ] `backend/app/services/auth_service.py` handles business logic
- [ ] `backend/app/routers/auth.py` exposes 3 endpoints
- [ ] CORS configured in `main.py`
- [ ] `frontend/src/api/client.ts` with JWT interceptor
- [ ] `frontend/src/context/AuthContext.tsx` manages state & persistence
- [ ] `Login.tsx` & `Register.tsx` pages built & styled
- [ ] `App.tsx` routing with `PrivateRoute` protection
- [ ] All endpoints tested via Postman/cURL & UI

---

## 💡 Pro Tips for Execution
1. **JWT Secret**: Use `openssl rand -hex 32` to generate a secure `SECRET_KEY` for `.env`
2. **Password Policy**: Enforce minimum length (e.g., 8 chars) in both frontend validation and backend schema
3. **Error Mapping**: Standardize API errors to `{ detail: string }` so frontend can display them uniformly
4. **Dev CORS**: Keep `origins=["http://localhost:5173"]` in FastAPI's `CORSMiddleware` during dev
5. **Token Refresh**: For Phase 2, keep it simple with `localStorage`. Plan refresh logic in Phase 5+ if needed.

---

Once Phase 2 is complete, you'll have a secure foundation to build authenticated transactions, AI categorization, and the dashboard in subsequent phases.