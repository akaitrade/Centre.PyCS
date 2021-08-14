from api.ttypes import Transaction, TransactionId
import sys
from keys import Keys
from clientex import ClientEx
import base58check



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




        

        
