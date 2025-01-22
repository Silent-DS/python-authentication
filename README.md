
### **README.md**

```markdown
Flask Authentication System

A secure login and registration system built with Flask, Flask-SQLAlchemy, Flask-Login, and Flask-WTF. This project demonstrates how to implement user authentication, including registration, login, and logout functionality.



Features

- User Registration: Users can create an account by providing a username, email, and password.
- User Login: Registered users can log in using their credentials.
- Password Hashing: User passwords are securely hashed using `werkzeug.security`.
- Protected Routes: Certain routes (e.g., the home page) are only accessible to authenticated users.
- Flash Messages: Feedback messages are displayed for successful registration, login, and errors.



Technologies Used

- Flask: A lightweight web framework for Python.
- Flask-SQLAlchemy: An ORM for database management.
- Flask-Login: Manages user sessions and authentication.
- Flask-WTF: Handles form validation and rendering.
- SQLite: A lightweight database for development.
- Werkzeug: Provides password hashing and security utilities.



Project Structure


flask_login_system/
│
├── app/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── static/
│   │   └── styles.css
│   └── routes.py
│
├── config.py
├── run.py
├── requirements.txt
└── README.md



Setup Instructions

1. Clone the Repository

bash
git clone https://github.com/SilentDS/flask-authentication-system.git
cd flask-authentication-system


2. Create a Virtual Environment

bash
python -m venv .venv


- On Windows:
   bash
  .venv\Scripts\activate
 
- On macOS/Linux:
   bash
  source .venv/bin/activate
 

3. Install Dependencies

 bash
pip install -r requirements.txt


4. Set Up the Database 

Run the following command to create the SQLite database and tables:

bash
python run.py


This will create an `app.db` file in your project directory.

5. Run the Application

bash
python run.py


The application will be available at `http://127.0.0.1:5000`.



Usage

1. Register a New User
   - Visit `http://127.0.0.1:5000/register`.
   - Fill out the registration form and submit it.

2. Log In
   - Visit `http://127.0.0.1:5000/login`.
   - Enter your credentials to log in.

3. Access the Home Page
   - After logging in, you will be redirected to the home page (`http://127.0.0.1:5000/index`).

4. Log Out
   - Click the "Logout" link to log out.



Configuration

The application uses a `config.py` file for configuration. By default, it uses SQLite for the database. You can modify the `SQLALCHEMY_DATABASE_URI` to use a different database (e.g., PostgreSQL, MySQL).

Example configuration for PostgreSQL:

python
class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




Dependencies

The project dependencies are listed in `requirements.txt`. To install them, run:

bash
pip install -r requirements.txt




Contributing

Contributions are welcome! If you find a bug or want to add a feature, please open an issue or submit a pull request.



License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



Acknowledgments

- Flask Documentation: https://flask.palletsprojects.com/
- Flask-Login Documentation: https://flask-login.readthedocs.io/
- Flask-WTF Documentation: https://flask-wtf.readthedocs.io/


