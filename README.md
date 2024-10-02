# Tweets Application

This project is a basic Twitter-like web application where users can register, log in, and create, edit, or delete tweets with text and images. This project uses email activation for account verification. You need to configure SMTP settings to send emails.


## App Functionality

- 🔐 User Registration : Users can sign up with a form (username, email, and password)
- 📧 Email Activation : After registration, users receive an email with an activation link
- ✅ Account Activation : Users must verify their account via the activation link before logging in
- 🔓 Login : Registered users can log in with their username and password
- 📝 Tweeting : Authenticated users can create, edit, or delete tweets (up to 200 characters)
- 🖼️ Image Support : Tweets can include images along with text
- 🗒️ Tweet Display : Tweets appear on the homepage in reverse chronological order
- 🔑 Forgot Password : Users can reset their password by clicking "Forgot Password." An email with a reset link is sent to their registered email for easy password change
- 🔓 Change Password: Users can change their password when they are loged in 
- ✉️ SMTP Configuration : Email system setup required for sending Activation/Forgot Password emails


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

