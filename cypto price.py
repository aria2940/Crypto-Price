import cryptocompare
from time import sleep
from pygame import mixer
from colorama import Fore
import os
import colorterminal
os.system('cls' or 'clear')
print(colorterminal.ColorText.RED+"Note : Be sure to connect to the internet!")
print(colorterminal.ColorText.YELLOW+"Welcome to my first application Bitcoin price announcement program")

arz = int(input("~Which one to run?  1.BTC  ~~ 2.ETH ~~ 3.BNB ~~ 4.ADA ~~ 5.Next Options "))
if arz == 5 :
    arz = int(input("Which one to run? 6.XRP ~~ 7.Doge ~~ 8 .BTT ~×"))
#crypto_list = cryptocompare.get_coin_list(format=True)
#print(crypto_list)
mixer.init()

if arz == 1 :
    one_show = cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Bitcoin Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Bitcoin
elif arz == 2 :
    one_show = cryptocompare.get_price('ETH', currency='USD')["ETH"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Ethereum Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Ethereum
elif arz == 3 :
    one_show = cryptocompare.get_price('BNB', currency='USD')["BNB"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Binanace Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Binanace
elif arz == 4 :
    one_show = cryptocompare.get_price('ADA', currency='USD')["ADA"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Cardano Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Cardano
elif arz == 6:
    one_show = cryptocompare.get_price('XRP', currency='USD')["XRP"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Rippel Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Rippel
elif arz == 7 :
    one_show = cryptocompare.get_price('DOGE', currency='USD')["DOGE"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Doge coin Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Doge coin
elif arz == 8 :
    one_show = cryptocompare.get_price('BTT', currency='USD')["BTT"]["USD"]
    print(colorterminal.ColorText.GREEN+"Pleas Wait .  .  .")
    print(colorterminal.ColorText.YELLOW +'\t now Bit Tornt Price ⇒ ',one_show, colorterminal.ColorText.YELLOW)
    #Bit Torent

if arz==8 :
    stoped = int(input("Distance between notifications? "))
    while True:
        btt_price = cryptocompare.get_price('BTT', currency='USD')["BTT"]["USD"]
        print(colorterminal.ColorText.YELLOW ,"\t Bit Torent Price : ",btt_price)
        sleep(stoped)
#set valus
thresh_down = int(input("whta's your low thershold? "))
thresh_up = int(input("whta's your high thershold ? "))
thershold = int(input("whta's your thershold? "))
USD_price = int(input("price = USD / Toman : "))
sleeeped = int(input("Distance between notifications? "))
#check the price & prints
if arz == 1 :
    while True :
        btc_price = cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
        if btc_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t BTC went low' , btc_price)
            btc_toman[USD_price*btc_price]
            print(btc_toman)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif btc_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t BTC went high ⇒", btc_price )
            print(btc_price * USD_price)
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Bitcoin Price : ",btc_price)
            print(btc_price * USD_price)
            #price printing
        sleep(sleeeped)
elif arz == 2 :
      while True :
        eth_price = cryptocompare.get_price('ETH', currency='USD')["ETH"]["USD"]
        if eth_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t ETH went low' , eth_price)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif eth_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t ETH went high ⇒", eth_price )
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Ethereum Price : ",eth_price)
            #price printing
        sleep(sleeeped)        
elif arz == 3 :
      while True :
        bnb_price = cryptocompare.get_price('BNB', currency='USD')["BNB"]["USD"]
        if bnb_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t BNB went low' , bnb_price)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif bnb_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t BNB went high ⇒", bnb_price )
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Binanse Price : ",bnb_price)
            #price printing
        sleep(sleeeped)        
elif arz == 4 :
      while True :
        ada_price = cryptocompare.get_price('ADA', currency='USD')["ADA"]["USD"]
        if ada_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t ADA went low' , ada_price)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif ada_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t ADA went high ⇒", ada_price )
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Cardano Price : ",ada_price)
            #price printing
        sleep(sleeeped)        
elif arz == 6 :
      while True :
        xrp_price = cryptocompare.get_price('XRP', currency='USD')["XRP"]["USD"]
        if xrp_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t XRP went low' , xrp_price)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif xrp_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t XRP went high ⇒", xrp_price )
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Rippel Price : ",xrp_price)
            #price printing
        sleep(sleeeped)
elif arz == 7 :
      while True :
        dog_price = cryptocompare.get_price('DOGE', currency='USD')["DOGE"]["USD"]
        if dog_price < thresh_down :
            print(colorterminal.ColorText.RED+'\t DOGE went low' , dog_price)
            mixer.music.load('DOWN.mp3')
            mixer.music.play()
            thresh_up -= thershold
            thresh_down -= thershold
            #for went low price
        elif dog_price > thresh_up :
            print(colorterminal.ColorText.GREEN+"\t DOGE went high ⇒", dog_price )
            mixer.music.load('UP.mp3')
            mixer.music.play()
            thresh_up += thershold
            thresh_down += thershold
            #for went high price 
        else :
            print(colorterminal.ColorText.YELLOW ,"\t Doge coin Price : ",dog_price)
            #price printing
        sleep(sleeeped)
