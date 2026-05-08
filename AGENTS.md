# Agent Guidelines

## Project Overview
A financial management application allowing users to track transactions, categorize them, and gain insights into spending habits.

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy, PostgreSQL
- **Frontend:** TypeScript, React, Vite, Tailwind CSS
- **DevOps:** Docker, GitHub Actions

## Directory Structure
- `backend/app/`: Core application logic, models, routers, and database configuration.
- `frontend/src/`: React components, API client, and TypeScript types.
- `docker-compose.yml`: Container orchestration for the app and database.

## Essential Commands

### Backend
```bash
# Setup
./setup-venv.sh
source venv/bin/activate
pip install -r backend/requirements.txt

# Database
python backend/app/database.py init

# Testing
pytest backend/
```

### Frontend
```bash
# Setup & Run
cd frontend
npm install
npm run dev

# Testing
npm run test
```

### Docker
```bash
docker-compose up --build
```

## Development Guidelines

### Backend (Python/Flask)
- Follow PEP 8 style guide.
- Use SQLAlchemy for ORM interactions.
- Structure routes in `backend/app/routers/`.
- Use dependency injection where appropriate.

### Frontend (React/TypeScript)
- Use TypeScript strictly for all components and utilities.
- Adhere to React component lifecycle and state management best practices.
- Use Tailwind CSS for styling.
- API calls should be centralized in `frontend/src/api/client.ts`.

### Database
- PostgreSQL is the primary database.
- Migrations are handled via the database initialization scripts in the backend.

## Common Tasks

### Adding a New Category
1. Update `backend/app/models/category.py` if new fields are needed.
2. Create or update routes in `backend/app/routers/categories.py`.
3. Implement validation and business logic in the corresponding service.

### Creating a New Transaction
1. Update the backend to handle POST requests at `/transactions`.
2. Update `frontend/src/components/TransactionForm.tsx` to include the new input fields.
3. Update the API client in `frontend/src/api/client.ts`.

## Troubleshooting
- **Backend API Not Responding:** Check Flask server logs; ensure dependencies are installed.
- **Frontend Build Fails:** Verify Node.js version; clear `node_modules` and reinstall.

## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)