# GET MATIC - POLYGON FAUCET TOKENS

This script will add fetch MATIC - POLYGON Tokens from the Mumbai Faucet, the faucet graylists every successfull request for 60sec, the script will run and retry to get tokens after the graylist expires and also retry if there's an error in the request as sometimes the faucet returns errors. It gets 0.1 MATIC on every successful request.

## USE VENV
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## ADD WALLET ADDRESS TO .env FILE
```
WALLET_ADDRESS="XXXX"
```

## DISCLAIMER
Please don't abuse this script, I use it to automate getting some MATIC tokens in Mumbai for testing purposes. 