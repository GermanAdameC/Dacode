import requests
import os

url_by_year = {
    "2022": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm",
    "2021": "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm",
    "2020": "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm",
}

output_dir = "bronze"
os.makedirs(output_dir, exist_ok=True)

for year, url in url_by_year.items():
    response = requests.get(url)
    # verificacion de request get
    if response.status_code == 200:
        file_path = os.path.join(output_dir, f"aapl_10k_{year}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Archivo {file_path} descargado")
    else:
        print(f"Error al descargar el archivo {year}: {response.status_code}")
