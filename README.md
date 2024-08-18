## ToDO Backend App

This repo contains the source code for the backend of a simple ToDo application

### Functionality

The Backend provides the following functionality
* User creation: New users can create them an account
* User login: I also provide user login for privacy User - Task
* User Deletion: Users can be deleted
* Task Creation: Users can create new tasks with a title, description, and deadline.
* Task Reading: Users can view all their tasks, including their completion status.
* Task Updating: Users can modify the title, description, deadline, and completion status of a task.
* Task Deletion: Users can delete tasks.

### Technologies

* Backend: Python with FastAPI
* Database: PostgreSQL
* Authentication System: JWT (JSON Web Tokens)

### Installation

1. Clone the repository:
  git clone https://github.com/your-username/todoapp-backend.git

2. Install dependencies:
  cd todoapp-backend
   pip install -r requirements.txt

3. Configure the environment:
  * Create a PostgreSQL database and obtain the access credentials.
  * If you have a .env file, create a folder named configs and inside create a .env file, update the .env file with:
  * * DATABSE_URL
    * ALGORITHM
    * SECRET_KEY
  * Else if you want to do it online, just setup the project according the env aerguments 
4. Start the server:
  #### In Development:
    * uvicorn main:app --reload
  #### In Production:
    * fastapi run main.py

### API

The backend API is documented in the file docs or go to the "<app-link>/docs"

### Contributions

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, feel free to create a pull request.

### License

This project is licensed under the MIT License. 

### Contact

If you have any questions, you can contact me at:

* Email: cristiandeleonmonzon@gmail.com.com
* Telegram: https://t.me/TitiLM10
