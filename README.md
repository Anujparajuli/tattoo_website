# Tattoo Website

A Django-based web application for managing a tattoo studio, including artist profiles, booking system, gallery, and admin dashboard.

## Features
- Artist profiles and portfolio
- Online booking system
- Gallery of tattoo styles and works
- Contact form
- Admin dashboard for managing bookings, artists, and content

## Project Structure
- `booking/` - Handles booking logic and models
- `dashboard/` - Admin dashboard, forms, and management
- `tattoo_admin/` - Django project settings and configuration
- `media/` - Uploaded images and media files
- `static/` - Static files (CSS, JS, images)

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd tattoo_website
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```sh
   python manage.py migrate
   ```
4. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```
6. Access the site at `http://127.0.0.1:8000/`






## Steps

## 1. Check your current branch

#git branch

## 2. Create a new branch

git checkout -b new-branch-name

## Example:
git checkout -b feature-booking-form

## 3. Stage your changes

git add .

## 4. Commit your changes

git commit -m "Your commit message here"

## 5. Push the branch to GitHub

git push origin new-branch-name

Or set upstream for future pushes:
git push -u origin new-branch-name

## 6. Verify on GitHub

Go to your repository on GitHub, and you’ll see the option to create a Pull Request from your new branch.

## License
MIT License



