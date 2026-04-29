
import requests
import json
import random # Används här för att simulera prisförändringar om sidan är nere

def fetch_norrkoping_prices():
    # Här definierar vi de varor vi vill bevaka i Norrköping
    products = [
        {"id": 1, "name": "Arla Mellanmjölk", "brand": "Arla", "amount": "1.5L", "base_price": 16.50},
        {"id": 2, "name": "Garant Standardmjölk", "brand": "Garant", "amount": "1L", "base_price": 13.50},
        {"id": 3, "name": "Valio Laktosfri", "brand": "Valio", "amount": "1L", "base_price": 22.50},
        {"id": 4, "name": "Arla Smör", "brand": "Arla", "amount": "500g", "base_price": 55.00},
        {"id": 5, "name": "Bananer Eko", "brand": "Eko", "amount": "1kg", "base_price": 24.00}
    ]
    
    scraped_data = []
    
    for p in products:
        # Simulera priskontroll (Här läggs den riktiga requests-logiken för ICA/Willys APIer)
        # För Norrköping-specifik data siktar vi på butiks-ID för t.ex. Willys Norrköping City
        item_entry = {
            "id": p["id"],
            "name": p["name"],
            "brand": p["brand"],
            "amount": p["amount"],
            "img": f"https://source.unsplash.com/200x200/?{p['name'].split()[-1]}",
            "prices": {
                "ica": round(p["base_price"] * random.uniform(0.9, 1.1), 2),
                "willys": round(p["base_price"] * random.uniform(0.85, 1.05), 2),
                "lidl": round(p["base_price"] * random.uniform(0.8, 1.1), 2),
                "citygross": round(p["base_price"] * random.uniform(0.9, 1.1), 2)
            },
            "promo": random.choice([True, False, False]) # Slumpa kampanj för demo
        }
        scraped_data.append(item_entry)
        
    return scraped_data

if __name__ == "__main__":
    data = fetch_norrkoping_prices()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
