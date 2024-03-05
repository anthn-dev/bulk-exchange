# Bulk Exchange Account App

Account App is a Django-based project designed to manage user accounts. It includes functionalities for saving and updating user details like first name, surname, email, phone, and password.

User can register on this application by giving details of their first name, surname, email, phone number and password. Once their account is created, they can login to their account using their email and password.

User can also update their details like first name, surname, email, phone number and password.


## Prerequisites

Before you start, ensure you have the following installed:

- **Docker**: The project uses `Docker` for containerization.
  - **Linux**: For Mac OS installation instructions [visit this page](https://docs.docker.com/desktop/install/windows-install/).
  - **Mac OS**: For Mac OS installation instructions, [visit this page](https://docs.docker.com/desktop/install/mac-install/).

## Setup

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/anthn-dev/bulk-exchange.git
```

Navigate to the project directory:

```bash
cd bulk-exchange
```

### Run the Application Server

To start the application development server, run:

```bash
docker compose up
```

This command will start the backend server on http://0.0.0.0:8000/ and the frontend server on http://0.0.0.0:3000/, where you can access the API endpoints and the frontend application respectively.

## Using the Project

#### Accessing the Frontend

To access the frontend application, navigate to http://0.0.0.0:3000/ in your web browser.

With the server running, you can access the following pages:

- **Register/Update Profile Page**: http://0.0.0.0:3000/
- **Login Page**: http://0.0.0.0:3000/login/


### Accessing API Endpoints

With the server running, you can access the following API endpoints:

- **Create User**: `POST /api/v1/user/register/`
- **Login User**: `POST /api/v1/user/login/`
- **Retrieve User**: `GET /api/v1/user/` (requires authentication)
- **Update User**: `PATCH /api/v1/user/update/` (requires authentication)


You can use tools like `curl` or Postman to make requests to these endpoints or access them directly from your web browser.

## Testing

To run the automated test suite and ensure everything is working as expected, open shell of backend conatiner and execute:

```bash
python manage.py test
```

This command will discover and run all tests defined in the tests directory of the app.
