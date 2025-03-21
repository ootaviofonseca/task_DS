
<div align="center">
  <br>
  <h1>CRUD de Usuários</h1>
  <strong>Aplicação full stack com Flask, Vue e MongoDB</strong>
</div>
<br>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white">
  <img src="https://img.shields.io/badge/PrimeVue-333?style=for-the-badge&logo=vue.js&logoColor=white">
</p>

# About
  This project is a full-stack CRUD application for managing users, built with Flask as the backend, Vue.js and PrimeVue for the frontend, and MongoDB for the database. 

  The application allows users to:
  - View a list of all users in a table.
  - Add new users.
  - Edit existing user data.
  - Delete users.
  - Get user data by ID.
    

  The backend is implemented with Flask and provides RESTful API endpoints to perform CRUD operations on a MongoDB database. The frontend is built with Vue.js, utilizing PrimeVue for a modern, responsive interface.

  Additionally, a `parser.py` script is included to populate the database with initial data from a JSON file.

# Sobre
  Este projeto é uma aplicação full stack de CRUD para gerenciamento de usuários, construída com Flask no backend, Vue.js e PrimeVue no frontend, e MongoDB como banco de dados.

  A aplicação permite que os usuários:
  - Visualizem uma lista de todos os usuários em uma tabela.
  - Adicionem novos usuários.
  - Editem os dados dos usuários existentes.
  - Excluam usuários.

  O backend é implementado com Flask e fornece endpoints da API RESTful para realizar operações CRUD em um banco de dados MongoDB. O frontend é construído com Vue.js, utilizando PrimeVue para uma interface moderna e responsiva.

  Além disso, o script `parser.py` é incluído para popular o banco de dados com dados iniciais de um arquivo JSON.

# Backend Setup
### Requirements
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject/backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the `parser.py` script to load the initial data into MongoDB:
   ```bash
   python parser.py
   ```

5. Run the Flask app:
   ```bash
   python app.py
   ```

   The backend will be available at `http://localhost:5000`.

# Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Run the Vue.js application:
   ```bash
   npm run serve
   ```

  
# API Endpoints
The backend exposes the following API endpoints for CRUD operations:

- **GET** `/api/users` - Retrieve a list of all users.
- **POST** `/api/users` - Add a new user. The request body should contain user data.
- **PUT** `/api/users/{id}` - Update an existing user. The request body should contain the updated user data.
- **DELETE** `/api/users/{id}` - Delete a user.
- **GET** `/api/users/{id}` - Retrieve a user by their ID.
