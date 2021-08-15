from Connector import Connector

def main():
    TransactionsListGet()

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

def StatsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.StatsGet())

def TestTransactionsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TransactionsGet("ACkyon3ERkNEcNwpjUn4S6TLP3L76LFg3X6kWoJx82dK",0,10))

def SyncState():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SyncState())

def ActualFeeGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.ActualFeeGet(1))

def WalletIdGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.WalletIdGet("ACkyon3ERkNEcNwpjUn4S6TLP3L76LFg3X6kWoJx82dK"))

def TransactionsListGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TransactionsListGet())

def PoolListGetStable():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.PoolListGetStable(5500,5))

main()