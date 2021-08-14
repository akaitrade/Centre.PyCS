from Connector import Connector

def main():
    WalletDataGet()

def TestTransactionGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TransactionGet(5,0))

def WalletGetBalance():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.WalletGetBalance("ACkyon3ERkNEcNwpjUn4S6TLP3L76LFg3X6kWoJx82dK"))

def WalletTransactionsCountGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.WalletTransactionsCountGet("ACkyon3ERkNEcNwpjUn4S6TLP3L76LFg3X6kWoJx82dK"))

def WalletDataGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.WalletDataGet("ACkyon3ERkNEcNwpjUn4S6TLP3L76LFg3X6kWoJx82dK"))

main()