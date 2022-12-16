from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serializers import CountrySerializer
from bs4 import BeautifulSoup
import requests

@api_view(['GET'])
def country_info(request, country_name):
    # Scrape the Wikipedia page for the given country
    wikipedia_url = f'https://en.wikipedia.org/wiki/{country_name}'
    page = requests.get(wikipedia_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract the relevant information from the page
    name = soup.find('h1', id='firstHeading').text
    capital_tag = soup.find('span', {'class': 'capital'})
    capital = capital_tag.text if capital_tag else ''
    population_tag = soup.find('span', {'class': 'population'})
    population = int(population_tag.text.replace(',', '')) if population_tag else 0
    area_tag = soup.find('span', {'class': 'area'})
    area = float(area_tag.text.replace(',', '')) if area_tag else 0
    official_language_tag = soup.find('span', {'class': 'official-language'})
    official_language = official_language_tag.text if official_language_tag else ''

    # Create a dictionary with the extracted information
    data = {
        'name': name,
        'capital': capital,
        'population': population,
        'area': area,
        'official_language': official_language
    }

    # Use the serializer to convert the dictionary to JSON format
    serializer = CountrySerializer(data=data)
    serializer.is_valid()
    return Response(serializer.data)
