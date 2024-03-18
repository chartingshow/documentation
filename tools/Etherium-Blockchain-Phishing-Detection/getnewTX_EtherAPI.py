import requests 
import pandas as pd
import numpy as np

def getTxData (address,hash):
    
    url= "http://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=l&offset=10&sort=desc&apikey=YourApiKeyToken" 
    
    response = requests.get(url) 
    address_content = response.json() 
    result = address_content.get("result") 
    for transaction in result:         
        ihash = transaction.get("hash")
        if ihash == hash:
            tx_from = transaction.get("from") 
            tx_to = transaction.get("to") 
            value = float(transaction.get("value")) 
            TimeStamp = int(transaction.get("timeStamp"))
            BlockHeight = int(transaction.get("blockNumber"))    
            imputData = transaction.get("input")   
            contractAddress = transaction.get("contractAddress")             
            if contractAddress == "":
                contractAddress = np.nan            
            value =  value/10**18
                     
    list = [[hash,BlockHeight,TimeStamp,tx_from,tx_to,value,contractAddress,imputData]]
    newtx = pd.DataFrame(list, columns=['TxHash', 'BlockHeight', ' TimeStamp', 'From', 'To', 'Value', 'ContractAddress', 'Input'])
    return newtx

print(getTxData('0x3ddfa8ec3052539b6c9549f12cea2c295cff5296','0x0000000000000000000000000000000000000000000000000000000000000000'))
