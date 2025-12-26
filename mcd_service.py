import os
import time

from menu import menu_lists
menu_category = list(menu_lists.keys())

def clean():
    if os.name == 'nt':
        os.system('cls')
        pass
    else:
        os.system('clear')
        pass

def clearScreen(status):
  print("")
  if status == 'e':
    print("System : {Input anda salah, mohon ulangi}")
    time.sleep(1)
    clean()
    pass
  elif status == "c":
    print("System : {Proceed}")
    time.sleep(1)
    clean()
    pass

def trackOrder():
  print("Sedang pengembangan")
def report():
  print("Sedang pengembangan")

def menuPage():
  clean()
  print("Menu tersedia di McD")
  for i, category in enumerate(menu_category):
    print(f"{i}.{category}")
  
  userInput = input("> ")
  clean()
  if userInput == "0" or userInput =="1" or userInput == "2" or userInput == "3" or userInput == "4" or userInput == "5":
    for i, submenu in menu_lists[userInput]:
      print(f"{i}.{submenu} - Rp.{menu_lists[userInput]}")

  else:
      clearScreen("e")
      menuPage()

def homepage():
  clean()
  print("Halo, ada yang bisa saya bantu ?")
  print("1. Buka menu McD")
  print("2. Lacak pemesanan")
  print("3. Laporkan kesalahan")
  userInput = input("> ")
  if userInput == "1":
    menuPage()
  elif userInput == "2":
    trackOrder()
  else:
    report()

def logon():
  clean()
  print("Selamat datang di MC Donald Indonesia")
  username = input("Silahkan masukkan username anda: ")
  if username == "admin":
    homepage()
  else:
    clearScreen("e")
    logon()

logon()