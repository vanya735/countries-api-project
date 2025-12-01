import requests

# ===== ЧАСТИНА 1 =====
print("*** ІНФОРМАЦІЯ ПРО КРАЇНУ ***")
country_name = input("Введіть назву країни англійською (наприклад: ukraine, japan, canada): ")

url = f"https://restcountries.com/v3.1/name/{country_name}"
response = requests.get(url)

try:
    data = response.json()[0]

    official_name = data["name"]["official"]
    capital = data.get("capital", ["Немає даних"])[0]
    flag = data["flag"]
    population = data["population"]
    formatted_population = f"{population:,}".replace(",", " ")
    lat, lng = data["latlng"]

    print(f"\nОфіційна назва: {official_name}")
    print(f"Столиця: {capital}")
    print(f"Прапор: {flag}")
    print(f"Населення: {formatted_population} осіб")
    print(f"Географічне положення: {official_name} розташована приблизно на широті {lat} та довготі {lng}.")

except Exception as e:
    print("Помилка при отриманні даних про країну:", e)

# ===== ЧАСТИНА 2 =====
print("\n=== ВИПАДКОВИЙ ФАКТ ДЛЯ РОЗВАГИ ===")
try:
    fact1 = requests.get("https://catfact.ninja/fact").json()["fact"]
    fact2 = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

    print(fact1)
    print(fact2)

except Exception as e:
    print("Помилка при отриманні випадкового факту:", e)

# Щоб програма не закривалася одразу
input("\nНатисни Enter, щоб закрити програму...")
