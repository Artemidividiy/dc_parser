from requests import Request, Response
import requests
from rich.console import Console
from dataclasses import dataclass

dc_page_to_scrape = "https://www.delivery-club.ru/moscow"
@dataclass
class Item:
    name: str
    uses_delivery: str

class Parser:
    def __init__(self) -> None:
        with open("config.txt", "r") as config:
            self.request = requests.get(url=config.readlines()[0])
        data = self.request.json()
        self.items = list()
        for i in data["components"]:
            self.items.append(Item(name=i["vendor"]["name"],
            uses_delivery= "yes" if i["vendor"]["delivery"]["provider"] == 'ddk' else "no"
            ))
    def get_items(self): return self.items

if __name__ == "__main__" :
    parser = Parser()
    items = parser.get_items()
    Console().print(items)
    Console().print(len(items))