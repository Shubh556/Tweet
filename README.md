# Twitter Clone Django Application

This project is a basic Twitter-like web application where users can register, log in, and create, edit, or delete tweets with text and images. This project uses email activation for account verification. You need to configure SMTP settings to send emails.


## App Functionality

- **Registration :** Users can register by filling in a form with their username, email, and password. A verification email is sent to the user with an activation link.
- **Account Activation :** The user must activate their account via the email link.
- **Login :** Users can log in using their username and password.
- **Tweeting :** Authenticated users can create, edit, and delete tweets. Tweets can contain text (up to 200 characters) and an image.
- **Tweet Display :** All tweets are displayed in reverse chronological order on the homepage.


## Technologies Used

- **Python**
- **Django**
- **MySQL**


## Setup Instructions

Create a .env file in the project root to store environment variables like the SECRET_KEY and email configuration settings. For example:

- **SECRET_KEY=your-secret-key**
- **EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend**
- **EMAIL_HOST=smtp.your-email-host.com**
- **EMAIL_PORT=587**
- **EMAIL_USE_TLS=True**
- **EMAIL_HOST_USER=your-email@example.com**
- **EMAIL_HOST_PASSWORD=your-email-password**


## Note 

- When you clone or download this repo, simply open Vs code or any editor you like, and in that editor, open the terminal and type **cd the_tweets**

