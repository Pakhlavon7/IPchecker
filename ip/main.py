from tqdm import tqdm
import os
import time
import requests
import database
from art import tprint
from colorama import init, Fore
init()
from colorama import Fore,Back
os.system('cls||clear')



print('Идет проверка ресурсов,подождите...');


for i in tqdm(range(100)):
    time.sleep(0.1);



def location(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")
    result = response.json()
    if result["status"] == "fail":
        return main("Enter the correct IP address")

    record = []

    for key, value in result.items():
        record.append(value)
        print(f"[{key.title()}]: {value}")
    return tuple(record)

os.system('cls||clear')

def main(start: str):
    print(start)
    ip = input(Fore.GREEN + "IP адресс: ")
    


    
    try:
        new_data = location(ip)
        database.base(new_data)
    except ValueError:
        pass


if __name__ == "__main__":
    tprint("IP-checker")
    print("by smilli")
    print()
    main("Введите ваш IP")
input()
