from Connector import Connector

def main():
    SmartContractsListGet()

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

def PoolListGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.PoolListGet(0,5))

def PoolInfoGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.PoolInfoGet(0,5))

def PoolTransactionsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.PoolTransactionsGet(544,0,5))

def SmartContractGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SmartContractGet("12DHXQ8rzYUawD6VSD6WuVaTQ4uen7fStWsTmZASnDv1"))

def SmartContractsListGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SmartContractsListGet("EoPibFsGPE4xqXH2tYTBQUeJqSMMFvCZUdqAW9Bnh3nd",0,10))

def TransactionsStateGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TransactionsStateGet("EoPibFsGPE4xqXH2tYTBQUeJqSMMFvCZUdqAW9Bnh3nd",0,10))

def ContractAllMethodsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.ContractAllMethodsGet("EoPibFsGPE4xqXH2tYTBQUeJqSMMFvCZUdqAW9Bnh3nd",0,10))

    

main()