from Connector import Connector

def main():
    TestTransactionGet()

def TestTransactionGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TransactionGet(5,0))



main()