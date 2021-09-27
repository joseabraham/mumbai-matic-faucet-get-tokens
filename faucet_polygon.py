#!/usr/bin/python
import argparse
import requests
import json
import sched, time
import os
from dotenv import load_dotenv

load_dotenv()
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

url = "https://api.faucet.matic.network/transferTokens"
s = sched.scheduler(time.time, time.sleep)

def callFaucet():
    payload = json.dumps({
            "network": "mumbai",
            "address": WALLET_ADDRESS,
            "token": "maticToken"
            })
    headers = {
            'Content-Type': 'application/json'
        }
        
    success = False
    while not success:
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            print("RESPONSE OF FAUCET CALL", response.text)
            respJson = response.json()
            print("respJson", respJson['error'])
            if(respJson['error'] == 'Returned error: replacement transaction underpriced'):
                success = False
            else:
                success = True   
                s.enter(50, 1, callFaucet) 
        except Exception as e:   
            success = False                     
            s.enter(50, 1, callFaucet)    
            print('Error! re-trying...', e)

def __main__():
    try:        
        print("STARTING FAUCET REQUEST")
        s.enter(50, 1, callFaucet)
        s.run()

    except Exception as e:        
        print("exception catched", e)
        pass

if __name__ == '__main__':
    __main__()