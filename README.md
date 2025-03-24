# Django Blog

A simple and fully functional blog built with Django.
This project allows users to create, edit, and delete blog posts, as well as comment on posts and interact with the content.
The blog includes user authentication and an admin panel for managing posts and users.

## Features

- **User Authentication**: Allows users to register, log in, and manage their account.
- **Create & Manage Posts**: Authenticated users can create, edit, and delete blog posts.
- **Category System**: Posts can be categorized for better organization.
- **Order Management**: Customers can place orders, and administrators can manage orders.

## Admin Dashboard

Here’s a screenshot of the admin dashboard where administrators can manage blog posts and users:

![Admin Dashboard](images/Screenshot%202025-03-24%20170737.png)

## Website Screenshot

Here’s a screenshot of the homepage where users can browse blog posts:

![Website Homepage](images/Screenshot%202025-03-24%20170705.png)

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/amine466/Django-Blog.git
```
### 2. Navigate into the project directory
```bash
cd Django-Blog
```
### 3. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Run the development server
```bash
python manage.py runserver
```
You can now visit the site at http://127.0.0.1:8000/ in your browser.

## Usage
- Visit the homepage to browse blog posts.


- Use the admin panel (http://127.0.0.1:8000/admin/) to manage posts and users.

## Technologies Used

- Django: Web framework for building the application.

- Python: Programming language.

- SQLite: Database for development (you can switch to another database if desired).

- Bootstrap: Frontend framework for styling.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.
