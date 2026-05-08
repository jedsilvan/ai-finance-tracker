```markdown
# CONTINUE.md

## Project Overview
#### Purpose:
This project is a financial management application that allows users to track transactions, categorize them, and gain insights into spending habits.

#### Key Technologies Used:
- **Backend:** Python (Flask framework)
- **Frontend:** TypeScript (React library), Vite for build tooling, Tailwind CSS for styling
- **Database:** PostgreSQL (via SQLAlchemy ORM)
- **Docker** for containerization
- **CI/CD:** GitHub Actions

#### High-Level Architecture:
- **Backend Services:**
  - Authentication and authorization
  - Transaction management
  - Category management
  - AI-driven insights generation

- **Frontend Components:**
  - User interface for transaction input, viewing, and analysis
  - Navigation bar
  - Charts for spending visualization

## Getting Started
#### Prerequisites:
1. Docker installed on your machine.
2. Python 3.8 or higher (for backend development).
3. Node.js with npm (for frontend development).

#### Installation Instructions:
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ````
2. **Backend Setup:**
   - Create a virtual environment and install dependencies:
     ```bash
     ./setup-venv.sh
     source venv/bin/activate
     pip install -r backend/requirements.txt
     ```
   - Set up the database:
     ```bash
     export DATABASE_URL=postgresql://user:password@localhost/dbname
     python backend/app/database.py init
     ````
3. **Frontend Setup:**
   - Install dependencies:
     ```bash
     cd frontend
     npm install
     ```
   - Start the development server:
     ```bash
     npm run dev
     ````
4. **Docker Containers:**
   - Build and run containers using Docker Compose:
     ```bash
     docker-compose up --build
     ````

#### Basic Usage Examples:
- **Backend API Endpoints:"
  - Authentication (POST /auth/login)
  - Transaction creation (POST /transactions)
  - Category listing (GET /categories)

- **Frontend Features:**
  - User login and registration
  - Adding new transactions
  - Viewing transaction history
  - Generating spending insights

#### Running Tests:
- **Backend Tests:**
  ```bash
  pytest backend/
  ````
- **Frontend Tests:**
  ```bash
  npm run test
  ````

## Project Structure
#### Overview of Main Directories and Their Purpose:
- **backend/**: Contains the backend code written in Python using Flask.
- **frontend/**: Contains the frontend code built with TypeScript and React.
- **.continue/rules/**: Stores the CONTINUE.md file for project documentation.

#### Key Files and Their Roles:
- **backend/requirements.txt**: Lists all Python dependencies.
- **backend/app/main.py**: Entry point of the backend application.
- **frontend/package.json**: Manages frontend dependencies.
- **frontend/vite.config.ts**: Configuration for Vite build tooling.
- **frontend/src/App.tsx**: Main React component.

#### Important Configuration Files:
- **.env.example**: Example environment variables for configuration.
- **backend/config.py**: Backend configuration settings.
- **frontend/.gitignore**: Git ignore rules for frontend files.

## Development Workflow
#### Coding Standards or Conventions:
- Follow PEP 8 style guide for Python code.
- Use TypeScript's type system effectively.
- Adhere to React component lifecycle and state management best practices.

#### Testing Approach:
- Backend: Unit tests using `pytest`.
- Frontend: Integration tests using Jest and React Testing Library.

#### Build and Deployment Process:
- **Local Development:**
  - Run backend with Flask development server.
  - Use Vite for frontend development server.

- **Production:**
  - Containerize the application using Docker.
  - Deploy to a Kubernetes cluster or cloud service like AWS, Azure, or Google Cloud.

#### Contribution Guidelines:
1. Fork the repository and create a new branch.
2. Make changes and commit them with descriptive messages.
3. Write tests for your changes.
4. Open a pull request with a clear description of what was changed.

## Key Concepts
#### Domain-Specific Terminology:
- **Transaction:** A record of financial activity, including amount, category, and date.
- **Category:** A classification for transactions (e.g., groceries, entertainment).

#### Core Abstractions:
- **User Authentication:** Secure login and registration processes.
- **Database Management:** CRUD operations for transactions and categories.

#### Design Patterns Used:
- MVC architecture for separation of concerns.
- Dependency Injection to manage dependencies.

## Common Tasks
#### Step-by-step Guides for Frequent Development Tasks:
1. **Adding a New Category:**
   - Update the `backend/app/models/category.py` with new fields if necessary.
   - Create a new route in `backend/app/routers/categories.py`.
   - Implement validation and business logic in the corresponding service.

2. **Creating a New Transaction:**
   - Add a form component in `frontend/src/components/TransactionForm.jsx`.
   - Update the backend to handle POST requests at `/transactions`.

#### Examples of Common Operations:
- **Updating User Profile:**
  ```typescript
  // frontend/src/api/client.js
  export async function updateUserProfile(userId, profileData) {
    const response = await fetch(`/users/${userId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profileData),
    });
    return response.json();
  }
  ````

## Troubleshooting
#### Common Issues and Their Solutions:
- **Backend API Not Responding:**
  - Check the Flask server logs for errors.
  - Ensure all dependencies are installed.

- **Frontend Build Fails:**
  - Verify that Node.js and npm are correctly installed.
  - Clear `node_modules` and reinstall dependencies.

#### Debugging Tips:
- Use `print()` statements in Python for debugging backend issues.
- Utilize browser developer tools for frontend debugging.
- Enable detailed logging in both frontend and backend code.

## References
#### Links to Relevant Documentation:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

#### Important Resources:
- **Docker Compose File**: `docker-compose.yml`
- **Backend Configuration**: `backend/app/config.py`
- **Frontend Build Configuration**: `frontend/vite.config.ts`
```