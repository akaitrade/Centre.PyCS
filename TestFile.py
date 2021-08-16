from Connector import Connector
from general.ttypes import Amount, ByteCodeObject
from api.ttypes import TransactionId, TokenHoldersSortField, TokensListSortField, TokenFilters
def main():
    TrustedGet()

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
    print(Connect_.TransactionsStateGet("EoPibFsGPE4xqXH2tYTBQUeJqSMMFvCZUdqAW9Bnh3nd",None))

def ContractAllMethodsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    t = Connect_.SmartContractGet("12DHXQ8rzYUawD6VSD6WuVaTQ4uen7fStWsTmZASnDv1")
    print(Connect_.ContractAllMethodsGet(t.smartContract.smartContractDeploy.byteCodeObjects))

def SmartMethodParamsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SmartMethodParamsGet("EoPibFsGPE4xqXH2tYTBQUeJqSMMFvCZUdqAW9Bnh3nd",1))

def SmartContractDataGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SmartContractDataGet("12DHXQ8rzYUawD6VSD6WuVaTQ4uen7fStWsTmZASnDv1"))

def SmartContractCompile():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.SmartContractCompile("import com.credits.scapi.annotations.*; import com.credits.scapi.v0.*; public class MySmartContract extends SmartContract { public MySmartContract() {} public String hello2(String say) { return \"Hello\" + say; } }"))

def TokenBalancesGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenBalancesGet("4SFfA1S2xfA3BdgkTn2tK14yDhLuD11RVz78kqx35jct"))

def TokenTransfersGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenTransfersGet("4SFfA1S2xfA3BdgkTn2tK14yDhLuD11RVz78kqx35jct",0,10))

def TokenTransferGet():
    Connect_ =  Connector("165.22.212.253:9090")
    txsid = TransactionId()
    txsid.poolSeq = 5000
    txsid.index = 1
    print(Connect_.TokenTransferGet("4SFfA1S2xfA3BdgkTn2tK14yDhLuD11RVz78kqx35jct",txsid))

def TokenTransfersListGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenTransfersListGet(0,10))

def TokenWalletTransfersGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenWalletTransfersGet("12DHXQ8rzYUawD6VSD6WuVaTQ4uen7fStWsTmZASnDv1","12DHXQ8rzYUawD6VSD6WuVaTQ4uen7fStWsTmZASnDv1",0,10))

def TokenInfoGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenInfoGet("13T1JhxF614ZKT6L2Kh8wtpE5xoZLGdFxnXbFiWKFih1"))

def TokenHoldersGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TokenHoldersGet("4SFfA1S2xfA3BdgkTn2tK14yDhLuD11RVz78kqx35jct", TokenHoldersSortField.TH_Balance, True,0 ,10))
    
def TokensListGet():
    Connect_ =  Connector("165.22.212.253:9090")
    Ftr = TokenFilters()
    print(Connect_.TokensListGet(TokensListSortField.TL_HoldersCount,Ftr,True,0,10))

def WalletsGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.WalletsGet(0,10,None,True))

def TrustedGet():
    Connect_ =  Connector("165.22.212.253:9090")
    print(Connect_.TrustedGet(0))

main()