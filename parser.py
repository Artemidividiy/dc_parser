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
        self.items = list()
        for i in range(4):
            self.parse_loc(i)
    def get_items(self): return self.items
    def parse_loc(self, config_line):
        try: 
            with open("config.txt", "r") as config:
                Console().log(f"file: {config.readlines()}, len {len(config.readlines())}")
                self.nw_request = requests.get(url=config.readlines()[config_line])
            Console().print(f"[cyan] request successful [/] {self.nw_request.status_code}")
            data = self.nw_request.json()
            Console().print(len(data)) if data else Console().print("[bold yellow] cannot fetch data[/]")
            for i in data["components"]:
                self.items.append(Item(name=i["vendor"]["name"],
                uses_delivery= "yes" if i["vendor"]["delivery"]["provider"] == 'ddk' else "no"
                ))
            new_items = []
            for i in self.items:
                if i not in new_items: new_items.append(i)
            self.items = new_items
        except:
            Console().print("[bold red]something went wrong[/]")
            self.items = []

if __name__ == "__main__" :
    parser = Parser()
    items = parser.get_items()
    Console().print(items)
    Console().print(len(items))