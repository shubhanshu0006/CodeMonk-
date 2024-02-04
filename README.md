# Project Title

REST API for Paragraphs - README

## Overview

This Django Rest Framework (DRF) application provides a REST API for storing paragraphs and their associated words in a PostgreSQL database. It also allows users to search for paragraphs containing a specific word. The application uses a custom user model for authentication and follows RESTful API design patterns. Has a signup as well as login functionality. You cannot access the store and save APIs without the access token.

## Tech Stack

**Server:** Python, Django Rest Framework,
PostgreSQL (Relational Database)

## Installation

Clone the Repository

bash
git clone [https://github.com/your-username/your-repository.git](https://github.com/shubhanshu0006/CodeMonk-.git)
cd your-repository

2. Create a Virtual Environment

bash
python -m venv venv

3. Activate the Virtual Environment

On Windows:
bash
venv\Scripts\activate

On Unix or MacOS:
bash
source venv/bin/activate

4. Install Dependencies
   bash
   pip install -r requirements.txt

5. Apply Database Migrations
   bash
   python manage.py migrate
   Usage

## Usage/Examples

1. Run the Development Server

bash
python manage.py runserver

2. API Endpoints

User Registration API
Endpoint: /api/signup/
Method: POST

Payload Example:

json

{
"email": "john@website.com",
"name": "John Doe",
"password": "your_password"
}

Response Example:

json
{
"status": true,
"status_code": 201,
"message": "Successfully Registered.",
"data": {
"email": "john@website.com",
"name": "John Doe"
}
}

User Login API
Endpoint: /api/login/
Method: POST
Payload Example:
json
{
"email": "john@website.com",
"password": "your_password"
}
Response Example:
json

{
"token": "your_auth_token",
"success": true,
"message": "Login successful"
}

#Store Paragraphs API

Endpoint: /api/store/paragraphs/
Method: POST
Authentication: Token-based authentication required
Payload Example:
json
{
"paragraphs": [
"Lorem ipsum dolor sit amet.",
"Consectetur adipiscing elit."
]
}

Response Example:
json

{
"message": "Paragraphs and words stored successfully"
}

#Search Paragraphs API

Endpoint: /api/search/paragraphs/
Method: GET
Authentication: Token-based authentication required
Query Parameter: word (word to search)

Response Example:

json
[
{
"paragraph_id": 1
},
{
"paragraph_id": 2
}
]

## Documentation

[Documentation](https://cloudy-eclipse-33226.postman.co/workspace/SkillBadgeApp~45e72fbb-c4a3-427d-8fc7-054ef942adc3/collection/31959875-edd156d8-6d2b-4f0f-a430-436b490ce3d1?action=share&creator=31959875)

