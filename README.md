# 💰 AI-Powered Personal Finance Tracker
### Full-Stack Portfolio Project Plan

---

## 📌 Project Overview

A full-stack web application that helps users track their income and expenses, automatically categorizes transactions using AI, and provides smart monthly summaries and spending insights through an interactive dashboard.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI (Python) |
| **Frontend** | React + Vite |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy + Alembic (migrations) |
| **Auth** | JWT (via `python-jose`) |
| **AI** | Claude API (Anthropic) |
| **Charts** | Recharts |
| **Styling** | Tailwind CSS |
| **API Client** | Axios |
| **Containerization** | Docker + Docker Compose |

---

## 🗂️ Project Structure

```
ai-finance-tracker/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI entry point
│   │   ├── config.py             # Settings & env vars
│   │   ├── database.py           # DB connection & session
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── transaction.py
│   │   │   └── category.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── transaction.py
│   │   │   └── category.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── transactions.py
│   │   │   ├── categories.py
│   │   │   └── insights.py
│   │   ├── services/
│   │   │   ├── ai_service.py     # Claude API integration
│   │   │   └── auth_service.py
│   │   └── utils/
│   │       └── security.py       # Password hashing, JWT
│   ├── alembic/                  # DB migrations
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── api/
│   │   │   └── client.js         # Axios instance
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── TransactionForm.jsx
│   │   │   ├── TransactionList.jsx
│   │   │   ├── CategoryBadge.jsx
│   │   │   └── charts/
│   │   │       ├── SpendingPieChart.jsx
│   │   │       └── MonthlyBarChart.jsx
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Transactions.jsx
│   │   │   └── Insights.jsx
│   │   ├── context/
│   │   │   └── AuthContext.jsx
│   │   └── hooks/
│   │       ├── useTransactions.js
│   │       └── useInsights.js
│   ├── index.html
│   ├── package.json
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🗄️ Database Schema

### `users`
| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| email | VARCHAR | Unique |
| hashed_password | VARCHAR | bcrypt |
| full_name | VARCHAR | |
| created_at | TIMESTAMP | |

### `categories`
| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| name | VARCHAR | e.g. "Food", "Transport" |
| icon | VARCHAR | Emoji or icon name |
| color | VARCHAR | Hex color for UI |
| is_default | BOOLEAN | System vs user-created |

### `transactions`
| Column | Type | Notes |
|---|---|---|
| id | UUID | Primary key |
| user_id | UUID | FK → users |
| category_id | UUID | FK → categories |
| amount | DECIMAL | Positive = income, negative = expense |
| type | ENUM | `income` / `expense` |
| description | VARCHAR | User-provided text |
| ai_note | TEXT | AI-generated insight per transaction |
| date | DATE | Transaction date |
| created_at | TIMESTAMP | |

---

## 🔌 API Endpoints

### Auth
```
POST   /api/auth/register        # Create account
POST   /api/auth/login           # Returns JWT token
GET    /api/auth/me              # Get current user
```

### Transactions
```
GET    /api/transactions         # List all (with filters: month, type, category)
POST   /api/transactions         # Add new transaction (triggers AI categorization)
PUT    /api/transactions/{id}    # Update transaction
DELETE /api/transactions/{id}    # Delete transaction
```

### Categories
```
GET    /api/categories           # List all categories
POST   /api/categories           # Create custom category
```

### AI Insights
```
GET    /api/insights/summary     # Monthly AI-generated summary
GET    /api/insights/anomalies   # Unusual spending alerts
POST   /api/insights/categorize  # Manually re-run AI categorization
```

---

## 🤖 AI Features (Claude API)

### 1. Auto-Categorization
When a transaction is added, send the description to Claude and return a suggested category.

**Prompt template:**
```python
prompt = f"""
You are a finance assistant. Given a transaction description, return the most fitting 
category from this list: {categories}.

Transaction: "{description}"

Respond with ONLY the category name, nothing else.
"""
```

### 2. Monthly AI Summary
At the end of each month (or on demand), generate a plain-English summary.

**Example output:**
> "In March, you spent ₱18,400 — 32% more than February. Your biggest category was Food (₱6,200), followed by Transport (₱3,100). You saved ₱4,000 this month. Consider reviewing your dining out budget."

### 3. Anomaly Detection
Detect transactions that are unusually large compared to historical averages per category.

---

## 📄 Pages & Features

### 🔐 Auth Pages
- Register / Login forms
- JWT stored in `localStorage`
- Protected routes via `AuthContext`

### 📊 Dashboard
- Total income vs expenses (current month)
- Net savings card
- Spending by category — Pie chart
- Monthly overview — Bar chart (last 6 months)
- AI monthly summary card

### 📋 Transactions Page
- Paginated transaction list
- Filter by: date range, type (income/expense), category
- Add transaction form → triggers AI categorization on submit
- Inline edit & delete

### 💡 Insights Page
- Spending trends over time
- Top categories this month vs last month
- AI anomaly alerts ("You spent 3x more on shopping this week")
- Budget suggestions

---

## ⚙️ Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Backend
DATABASE_URL=postgresql://user:password@db:5432/finance_db
SECRET_KEY=your_super_secret_jwt_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# AI
ANTHROPIC_API_KEY=your_anthropic_api_key

# Frontend
VITE_API_BASE_URL=http://localhost:8000
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL (or Docker)

### With Docker (Recommended)
```bash
git clone https://github.com/yourusername/ai-finance-tracker
cd ai-finance-tracker
cp .env.example .env     # Fill in your values
docker-compose up --build
```

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head           # Run migrations
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 📦 Key Dependencies

### Backend (`requirements.txt`)
```
fastapi
uvicorn[standard]
sqlalchemy
alembic
asyncpg
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
anthropic
python-dotenv
pydantic[email]
```

### Frontend (`package.json`)
```json
{
  "dependencies": {
    "react": "^18",
    "react-router-dom": "^6",
    "axios": "^1",
    "recharts": "^2",
    "tailwindcss": "^3",
    "@headlessui/react": "^1",
    "date-fns": "^3"
  }
}
```

---

## 🗓️ Suggested Build Order

| Phase | Tasks | Est. Time |
|---|---|---|
| **1. Setup** | Project structure, Docker, DB connection | Day 1 |
| **2. Auth** | Register, login, JWT, protected routes | Day 2 |
| **3. Transactions CRUD** | Models, API, frontend list + form | Days 3–4 |
| **4. AI Integration** | Claude auto-categorization + summary | Day 5 |
| **5. Dashboard & Charts** | Recharts, stats cards, filters | Days 6–7 |
| **6. Insights Page** | Anomaly detection, trends, AI tips | Day 8 |
| **7. Polish** | Error handling, loading states, responsive UI | Days 9–10 |
| **8. Deploy** | Railway / Render (backend) + Vercel (frontend) | Day 11 |

---

## 🌐 Deployment (Free Tier)

| Service | Platform |
|---|---|
| **Backend (FastAPI)** | [Railway](https://railway.app) or [Render](https://render.com) |
| **Database (PostgreSQL)** | Railway or Supabase |
| **Frontend (React)** | Vercel or Netlify |

---

## ✅ Portfolio Highlights to Mention

- ✔ RESTful API with FastAPI + JWT authentication
- ✔ AI-powered transaction categorization using Claude API
- ✔ PostgreSQL database with Alembic migrations
- ✔ Interactive charts and data visualization (Recharts)
- ✔ Dockerized for easy local development
- ✔ Responsive UI built with React + Tailwind CSS
- ✔ Clean separation of concerns (routers, services, schemas)

---

*Generated for portfolio project planning. Good luck building! 🚀*
