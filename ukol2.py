import requests
import json

# Část 1:
ICO = input("Zadej IČO: ")

response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ICO)
subjekt = response.json()

print(subjekt["obchodniJmeno"])
print(subjekt["sidlo"]["textovaAdresa"])

# Část 2:
nazev_subjektu = input("Zadej název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {"obchodniJmeno": nazev_subjektu}

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)
x = res.json()
   
print(f"Počet nalezených subjektů: {x["pocetCelkem"]}")

for firma in x["ekonomickeSubjekty"]:
    nazev = firma["obchodniJmeno"]
    ic = firma["ico"]
    print(nazev + ", " + ic)
    





