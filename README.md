# UCI Enduro World Cup Race Management

## 🎯 Objective

This project is a simplified system for managing a Mountain Bike race. It serves as the digital nerve center for organizing the event—minus the mud, crashes, and mid-race mechanicals. In this system, each **Rider** races for a **Team** in a given age bracket, and the following data is stored:

- **Rider**
- **Team**
- **Qualifying Race Result**
- **Main Race Result**

## 🛠️ What You’ll Be Doing

- **Modeling Race Data:**  
  Design models to represent riders, teams, qualifying times, race order, and race results.
- **Data Management:**  
  Provide a way for privileged users to perform CRUD operations on all data via Django Admin.  
  Create test data (via fixtures or the admin interface) and offer instructions for loading that data.

- **Public Front-End:**  
  Build a minimal front-end using Django templates for members of the public to view records and, optionally, to self-register as riders.
- **Race Day Functionality:**

  - Display qualifying results sorted fastest first.
  - Generate the main race start order (slowest qualifier starts first).
  - Show podium finishes (top three per age category).

- **Bonus (Extra Mile):**
  - Docker setup with a Dockerfile and docker-compose.yml.
  - Enhanced rider profiles with photos and race history.
  - Polished UI using Bootstrap 5 and custom CSS.

> _Note: The focus is on Django and back-end architecture, so functionality is prioritized over advanced UI design._

---

## 🚀 Getting Started

### Prerequisites

- **Python:** 3.10.0 or higher
- **Django:** As specified in `requirements.txt` (e.g., Django 5.x)
- **SQLite:** Used as the default database
- **Docker:** (Optional) If you prefer containerized deployment

### Setting Up the Virtual Environment

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd bike-race
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate

   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

3. **Run Migrations:**
   Generate and apply the database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```

4. **Load Test Data:**
   A sample fixture file (test_data.json) is provided to load test data. To load the data into your SQLite database, run:

   ```bash
   python manage.py loaddata test_data.json

   ```

5. **Create a Superuser:**
   To create an admin (superuser) account for accessing the Django Admin interface:

   ```bash
   python manage.py createsuperuser

   Follow the interactive prompts to set a username(admin), email(admin@example.com), and password(admin123).

   ```

6. **Run the Application:**

   ```bash
   python manage.py runserver
   ```

After completing these steps, open your browser and navigate as per below to view the application.
**Django Admin Interface:**
http://127.0.0.1:8000/admin/

Access the application in your browser at:

**Public Front-End:**

    •	Rider Roster: http://127.0.0.1:8000/world-cup/list-riders/
    •	Qualifying Results: http://127.0.0.1:8000/world-cup/qualifying-results/
    •	Race Start Order: http://127.0.0.1:8000/world-cup/race-start-order/
    •	Podium Finishes: http://127.0.0.1:8000/world-cup/podium/

### using Docker

If you prefer to run the application inside a Docker container, follow these steps:

**Build and run the Docker Image:**

```bash
docker compose up --build
```

** Access the Application:**

Open http://127.0.0.1:8000/ in your browser.
Docker will use the same SQLite database file (mounted via volumes), so data remains consistent between local and Docker environments.
