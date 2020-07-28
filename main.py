import json
from os import system, name 
import requests
from bs4 import BeautifulSoup

def clear(): 
  if name == 'nt': 
    _ = system('cls') 
  else: 
    _ = system('clear') 

def getItems():
  clear()
  with open("item.json") as file:
    arr = json.load(file)
    if len(arr) > 0:
      print("\nHere is an list of your items...")
      for i in range(0, len(arr)):
        item = arr[i]
        #print("Nr.", i, " ", item["product"], " ", str(item["price"]), "€ ", item["url"])
        print("Nr.", i, "|", item["product"], "|", str(item["price"]), "€")
    else:
      print("There are no items...")

def addItem():
  clear()
  product = input("\nEnter the product name: ")
  price = input("Enter your desired price: ")
  url = input("Enter the Amazon-URL: ");
  with open("item.json") as file:
    arr = json.load(file)
    arr.append({
      "product": product,
      "price": price,
      "url": url
    })
  with open("item.json", "w") as file:
    json.dump(arr, file)
  clear()
  print("The item were saved!")
  
def delItem():
  clear()
  getItems()
  key = input("\nWhich item do you wanna remove? ")
  key = int(key)
  with open("item.json") as file:
    arr = json.load(file)
    if key <= (len(arr) - 1):
      arr.pop(key)
      clear()
      print("The item was successfully removed!")
    else:
      clear()
      print("This item doesn't exist!")
  with open("item.json", "w") as file:
    json.dump(arr, file)

def checkPrices():
  # I stole this duck from Amazon :D
  # <!--       _
  #        .__(.)< (MEOW)
  #         \___)   
  #  ~~~~~~~~~~~~~~~~~~-->
  clear()
  with open("item.json") as file:
    arr = json.load(file)
    for i in range(0, len(arr)):
      item = arr[i]
      URL = item["url"]
      website = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44"})
      bs = BeautifulSoup(website.content, features="html5lib")
      price = bs.find(id="priceblock_ourprice").get_text()
      price = price.strip()
      price = price[:-5]
      price = int(price)
      if (price <= int(item["price"])):
        print("The price of", item["product"], "is currently at", price, "€\nYour desired price is", item["price"],"€\nYou can buy it here:", item["url"], "\n")

def menu():
  command = input("\nWhat command do you wanna run?\n1. Get a list of all items\n2. Add a new item\n3. Delete an item\n4. Check items\n5. Quit\nCommand: ")
  if command == "1":
    getItems()
    menu()
  elif command == "2":
    addItem()
    menu()
  elif command == "3":
    delItem()
    menu()
  elif command == "4":
    checkPrices()
    menu()
  elif command == "5":
    quit()
  else:
    print("This command doesn't exist!")
    menu()

menu()