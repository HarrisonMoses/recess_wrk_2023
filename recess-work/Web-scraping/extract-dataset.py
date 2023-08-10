"""from bs4 import BeautifulSoup
import requests
url='http://xeno-canto.org'
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
title=soup.find('title')
print(title)"""
import csv

"""
assignment 
Extract all bird species from this website 'http://xeno-canto.org' and generate the csv file for the bird species,family 
and more
Extract all bird songs for this website. 'http://xeno-canto.org'
use this api to get data. the endpoint for this webservice is at http://xeno_canto.org/api/2/recordings.


import requests
from bs4 import BeautifulSoup
import csv

def extract_bird_species():
    url = 'http://xeno-canto.org'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        bird_list = []
        for row in soup.select('table.list tbody tr'):
            species = row.select_one('td:nth-child(1)').text.strip()
            family = row.select_one('td:nth-child(2)').text.strip()
            bird_list.append({'Species': species, 'Family': family})
        return bird_list
    else:
        print("Failed to fetch data.")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Species', 'Family']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    bird_data = extract_bird_species()
    if bird_data:
        save_to_csv(bird_data, 'bird_species.csv')
        print("Data saved to 'bird_species.csv' successfully.")


import requests

def get_bird_songs():
    url = 'http://xeno-canto.org/api/2/recordings'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['recordings']
    else:
        print("Failed to fetch data.")
        return None

if __name__ == "__main__":
    bird_songs = get_bird_songs()
    if bird_songs:
        # Now you can process the 'bird_songs' data as needed.
        for song in bird_songs:
            print(f"Species: {song['en']}")  # English name of the species
            print(f"Family: {song['family']}")
            print(f"Recording URL: {song['file']}")
            print("----------")
            
            """

import requests
from bs4 import BeautifulSoup

def get_bird_species(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    scientific_name = soup.find("span", class_="scientific-name").text.strip()
    english_name = soup.find("span", class_="english-name").text.strip()
    family = soup.find("span", class_="family-name").text.strip()
    order = soup.find("span", class_="order-name").text.strip()
    distribution = soup.find("span", class_="distribution-name").text.strip()
    habitat = soup.find("span", class_="habitat-name").text.strip()
    conservation = soup.find("span", class_="conservation-name").text.strip()

    return {"scientific_name": scientific_name,
            "english_name": english_name,
            "family": family, "order": order,
            "distribution": distribution,
            "habitat": habitat,
            "conservation": conservation}


def main():
    url = "http://xeno-canto.org/species"
    species_list = []

    for page in range(1, 100):
        url = f"{url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.find_all("a", class_="species-link"):
            url = link["href"]
            species = get_bird_species(url)
            species_list.append(species)

    csv_file = open("bird_species.csv", "w")
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["scientific_name", "english_name", "family", "order", "distribution", "habitat", "conservation"])
    for species in species_list:
        csv_writer.writerow(species.values())

if __name__ == "__main__":
    main()
