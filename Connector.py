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




        

        
