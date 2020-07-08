import urllib.request
import json
def getStockData(stockSymbol):
	stockUrl = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + stockSymbol + '&apikey=V8FEN1LZQFHS4WFB'
	connection = urllib.request.urlopen(stockUrl)
	return connection.read().decode()

def main():
	while True:
		userInput = input("Enter the symbol of stock('quit' to quit): ")
		if userInput == 'quit':
			break
		stockData = getStockData(userInput)
		print(stockData)
		stockDictionary = json.loads(stockData)
		print("The current price of " + userInput + " is: " + str(stockDictionary['Global Quote']['05. price']))

main()
		