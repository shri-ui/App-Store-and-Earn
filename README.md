# My Django App

## Description

This is a Django web application that allows users to upload screenshots, earn points, and manage their app interactions. The application uses JWT (JSON Web Tokens) for authentication and provides a user-friendly interface for managing app-related tasks.

## Features

- User authentication (signup, login, logout)
- Upload screenshots with drag-and-drop functionality
- View points earned from app interactions
- Protected views that require authentication
- JWT authentication for secure API access

## Technologies Used

- Django 5.1.5
- Django REST Framework
- djangorestframework-simplejwt for JWT authentication
- HTML, CSS, and JavaScript for the frontend
- Dropzone.js for file uploads

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shri-ui/App-Store-and-Earn.git
   cd Evaluation
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Authentication**: Users can sign up, log in, and log out.
- **Upload Screenshots**: Navigate to the upload page to upload screenshots using drag-and-drop functionality.
- **View Points**: Users can view points earned from app interactions.
- **Protected Views**: Certain views require authentication to access.

## API Endpoints

- **Token Obtain**: `POST /api/token/` - Obtain JWT token using username and password.
- **Token Refresh**: `POST /api/token/refresh/` - Refresh the JWT token.
- **Protected View**: `GET /protected-view/` - Access this view only when authenticated.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django and Django REST Framework for building the web application.
- djangorestframework-simplejwt for JWT authentication.
- Dropzone.js for providing a great file upload experience.
