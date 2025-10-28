
# IST105 Assignment 6: Bitwise Calculator

## Project Description
A Django web application that processes five numerical inputs, performs logical and bitwise operations, and stores results in MongoDB.

## Features
- Input validation (numeric, negative warnings)
- Average calculation
- Bitwise operations for even/odd detection
- List filtering and sorting
- MongoDB integration
- Calculation history view

## Local Setup

### Prerequisites
- Python 3.8+
- MongoDB

### Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install django pymongo`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

## Technologies Used
- Python
- Django
- MongoDB
- Bootstrap
