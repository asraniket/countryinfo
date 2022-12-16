This is a Django Rest Framework (DRF) API that scrapes information from Wikipedia pages and returns it in JSON format.

Installation Clone the repository:

git clone https://github.com/your-username/country-info-api.git Install the dependencies:

pip install -r requirements.txt Run the migrations:

python manage.py migrate Start the development server:

python manage.py runserver

Usage You can access the API at the following endpoint:

http://localhost:8000/api/country_info/<country_name> Replace <country_name> with the name of the country you want to get information for.

The API will return a JSON object with the following fields:

name: the name of the country capital: the capital city of the country population: the population of the country area: the total area of the country