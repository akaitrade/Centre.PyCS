from api.ttypes import Transaction, TransactionId
import sys
from keys import Keys
from clientex import ClientEx
import base58check

import keys



class Connector(object):
    def __init__(self, address):
        self.ip = address

    def TransactionGet(self,PoolSeq, Index):
        """Description of TransactionGet

            Parameters:
            PoolSeq (int): BlockNumber
            Index (int): Transaction number in that block

            Returns:
            Object:TransactionGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).TransactionGet(TransactionId(poolSeq=PoolSeq, index=Index))
        except Exception as e:
            raise e
    
    def WalletGetBalance(self,PubKey):
        """Description of WalletGetBalance

            Parameters:
            PubKey (string): Base58 PublicKey

            Returns:
            Object:WalletGetBalanceResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).WalletGetBalance(base58check.b58decode(PubKey))
        except Exception as e:
            raise e
    
    def WalletTransactionsCountGet(self,PubKey):
        """Description of WalletTransactionsCountGet

            Parameters:
            PubKey (string): Base58 PublicKey

            Returns:
            Object:WalletTransactionsCountGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).WalletTransactionsCountGet(base58check.b58decode(PubKey))
        except Exception as e:
            raise e

    def WalletDataGet(self,PubKey):
        """Description of WalletDataGet

            Parameters:
            PubKey (string): Base58 PublicKey

            Returns:
            Object:WalletDataGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).WalletDataGet(base58check.b58decode(PubKey))
        except Exception as e:
            raise e

    def StatsGet(self):
        """Description of StatsGet
            NOT IMPLEMENTED YET
            Returns:
            Object:StatsGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).StatsGet()
        except Exception as e:
            raise e

    def TransactionsGet(self,PubKey,Offset=0, Index=10):
        """Description of TransactionsGet

            Parameters:
            PoolSeq (int): BlockNumber
            Index (int): Transaction number in that block

            Returns:
            Object:TransactionsGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).TransactionsGet(base58check.b58decode(PubKey),Offset,Index)
        except Exception as e:
            raise e

    def SendTransaction(self,Integeral,fraction,fee,PublicKey,PrivateKey,Target,UserData=None,TxsID=0,Transaction = None):
        """Description of SendTransaction

            Parameters:
            Integeral (int): Amount before the .
            fraction (int): Amount after the .
            fee (int): Amount fee as maximum
            PublicKey (string): PublicKey 
            PrivateKey (string): PrivateKey
            Target (string): Target Address
            UserData(byte[]) Optional
            TxsID(int) Optional
            Transaction(Transaction) Optional
            Returns:
            Object:TransactionFlowResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            keys_ = Keys()
            keys_.public_key = PublicKey
            keys_.private_key = PrivateKey
            keys_.target_public_key = Target
            if(TxsID == 0):
                TxsID = ClientEx(self.ip.split(':')).WalletTransactionsCountGet(keys_.public_key_bytes).lastTransactionInnerId + 1
            return ClientEx(self.ip.split(':')).transfer_coins(Integeral,fraction,fee,keys_,UserData,TxsID,Transaction)
        except Exception as e:
            raise e

    def SyncState(self):
        """Description of SyncState
            Returns:
            Object:SyncStateResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).SyncState()
        except Exception as e:
            raise e

    def ActualFeeGet(self,TransactionSize):
        """Description of SyncState

            Parameters:
            TransactionSize (int): TransactionSize

            Returns:
            Object:ActualFeeGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).ActualFeeGet(TransactionSize)
        except Exception as e:
            raise e

    def WalletIdGet(self,Address):
        """Description of WalletIdGet

            Parameters:
            Address (string): Address of Wallet

            Returns:
            Object:WalletIdGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).WalletIdGet(base58check.b58decode(Address))
        except Exception as e:
            raise e

    def TransactionsListGet(self, OffSet=0, Limit=10):
        """Description of TransactionsListGet

            Parameters:
            OffSet (int): Offset number
            Limit (int): Limit Amount per request

            Returns:
            Object:TransactionsGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).TransactionsListGet(OffSet,Limit)
        except Exception as e:
            raise e

    def PoolListGetStable(self, Sequence=0, Limit=10):
        """Description of PoolListGetStable

            Parameters:
            Sequence (int): Offset number
            Limit (int): Limit Amount per request

            Returns:
            Object:PoolListGetResult

            Detailed Documentation

            https://centr.gitbook.io/netcs/
            """
        try: 
            return ClientEx(self.ip.split(':')).PoolListGetStable(Sequence,Limit)
        except Exception as e:
            raise e




        

        
