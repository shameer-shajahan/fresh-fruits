# Fruit Sale Web Application

Welcome to the **Fruit Sale Web Application**! This is a Python Django-based web project designed to provide an online platform for selling fruits. Users can view a list of available products, see details about each product, add products to their cart, and get an order summary.

## Features

- **List Products**: Browse through a variety of fruits available for sale.
- **View Products**: See detailed information about each fruit, including price and description.
- **Add to Cart**: Add selected fruits to your shopping cart for purchase.
- **Order Summary**: View a summary of your selected items before checkout.

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- Django 4.0 or later
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shameer-shajahan/fresh-fruits.git
   cd fresh-fruits
   ```

2. **Set up a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

Open your browser and go to http://127.0.0.1:8000 to access the application.

### Usage

- Home Page: Lists all the available fruits.
- Product Details: Click on a product to view its details.
- Add to Cart: Add items to your shopping cart by clicking the "Add to Cart" button.
- View Cart and Order Summary: Check the items in your cart and the total price.

### Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS, Tailwind
- Database: SQLite (default with Django)
