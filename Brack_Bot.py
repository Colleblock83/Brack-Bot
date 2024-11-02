#Askin some stuff
import requests
fl = "Welcome to \033[0;31mBrack Bot!\033[0m"
middle = fl.center(125)
print(middle)
hd2 = "Made by \033[33mColleblock83\033[0m"
middle2 = hd2.center(125)
print(middle2)
hd3 = "Donation on \033[34mPayPal\033[0m: @FabioBaensch"
middle3 = hd3.center(125)
print(middle3)
print()
print("\033[1;36mGet the newest information of the last 24-Hours of a Crypto-Curreny\033[0m")
print()
for list in ["\033[0;31mExamples\033[0m:", "BTCUSDT (BTC in USDT/Theter)", "BTCEUR (BTC in EURO)", "ETHUSDT (Ether in USDT/Theter)", "\033[0;31m...\033[0m"]:
    print(list)
print()
print()
print("For which crypto currency do you want information for?")
lofi = input("Option: ")
#-----------------------------------------------------------------------------------------------------------------------------------
def curreny_status():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + lofi   #URL with 24-Hour statistics (10k usages)
    request_send = requests.get(url)


    if request_send.status_code == 200:
        saved_informations = request_send.json()
        #Print out the List (available somewhere on their website)
        print(f"""
        Information about \033[0;31m{lofi}:\033[0m
        \033[0;31mSymbol\033[0m : {saved_informations['symbol']}
        
        \033[0;31mCurrent Price\033[0m : {saved_informations['lastPrice']}$
        
        \033[0;31mOpening Price of the Day\033[0m: {saved_informations['openPrice']}$
        
        \033[0;31mPrice-Change (Example: +500 USDT in the last 24 Hours)\033[0m: {saved_informations["priceChange"]}$
        
        \033[0;31mChanged-Percentage\033[0m: {saved_informations['priceChangePercent']}%
        
        \033[0;31mPrevious-Close Price\033[0m: {saved_informations['prevClosePrice']}$
        
        \033[0;31mHighest Price (Rounded)\033[0m: {saved_informations['highPrice']}$
       
        \033[0;31mLowest Price (In the last 24 Hours)\033[0m: {saved_informations['lowPrice']}$
       
        \033[0;31mVolume (Amount of trades in the last 24 Hours)\033[0m: {saved_informations['volume']}
    
        \033[0;31mHighest Buying-Price\033[0m: {saved_informations['lastPrice']}$ 
            """)
        print()
        print(f"Or: You can see the results for yourself on Binance: {url}.")
    else:
        print(f"CRITICAL ERROR! ERROR CODE: {request_send.status_code}")
        return
#-----------------------------------------------------------------------------------------------------------------------------
while True:
    curreny_status()
    print()
    lofi = input("Option: ")

