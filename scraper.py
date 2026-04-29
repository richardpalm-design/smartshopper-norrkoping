import requests
import json

# Butiks-ID:n för Norrköping (Exempelvärden)
STORES = {
    "willys": "https://www.willys.se/c/norrkoping",
    "ica_maxi": "https://www.ica.se/butiker/maxi/norrkoping/",
    "lidl": "https://www.lidl.se/reklamblad"
}

def get_prices():
    # Denna funktion "låtsas" vara en webbläsare och läser av priserna
    # I en full version använder vi 'Playwright' för att läsa bakom inloggningar
    new_data = [] 
    # ... Logik för att extrahera priser ...
    return new_data

# Sparar ner till din databas-fil så appen uppdateras
with open('data.json', 'w') as f:
    json.dump(get_prices(), f)
