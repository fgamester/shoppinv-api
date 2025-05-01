# Simple Inventory App

Hello there!👋🏼

The other day me and my girlfriend were planning the supermarket shopping and it comes up a problem, sometimes we barely remember all the things we need to buy, not because we don't need them, but because somethings are not used frequently and we forget about them. So I thought, why not create a simple inventory app to help us with that?

Yes, this app could be used as an inventory app as well, but the main goal is to help us with the supermarket shopping. At least for now it will be like that, I don't reject the idea of expanding it in the future and probably I will, but for now I just focused on the following features:
- Add/Remove items to the inventory.
- Set a minimum quantity for each item.
- Create a shopping list based on the items that are below the minimum quantity.
- Set alternatives for each item.

>Remember that this is only the API for now, the frontend is in development. As soon as I finish it, I will release it and update this README with the link to the frontend repository and probably the deployed app as well.

## Used Technologies
- **Python:** The main programming language used to build the API.
- **Flask:** A lightweight WSGI web application framework for Python. It is used to build the API.
- **Flask-SQLAlchemy:** An extension for Flask that adds support for SQLAlchemy, an ORM (Object Relational Mapper) for Python. It is used to interact with the database.
- **Flask-Migrate:** An extension for Flask that handles SQLAlchemy database migrations for Flask applications using Alembic. It is used to manage database schema changes.
- **Flask-CORS:** An extension for Flask that allows cross-origin resource sharing (CORS). It is used to enable CORS for the API.
- **Flask-jwt-extended:** An extension for Flask that adds support for JSON Web Tokens (JWT) for authentication. It is used to secure the API endpoints.