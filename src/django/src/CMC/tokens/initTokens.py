import csv
import os
import django

from tokens.models import Tokens

# Only execute this by REPL through manage.py shell

with open('tokens/csv/tokens.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        model = Tokens()
        tokenID = row['tokenID']
        token_name = row['token_name']
        display_name = row['display_name']
        blockchain = row['blockchain']
        address = row['address']
        audit = row['audit']
        dextoolslink = row['dextoolslink']
        tokensnifferlink = row['tokensnifferlink']
        img_path = row['img_path']
        
        print(f"Token ID: {tokenID}")
        print(f"Token Name: {token_name}")
        print(f"Display Name: {display_name}")
        print(f"Blockchain: {blockchain}")
        print(f"Address: {address}")
        print(f"Audit: {audit}")
        print(f"Dextools Link: {dextoolslink}")
        print(f"Tokensniffer Link: {tokensnifferlink}")
        print(f"Image Path: {img_path}")
        model.tokenID = tokenID
        model.token_name = token_name
        model.display_name = display_name
        model.blockchain = blockchain
        model.address = address
        model.audit = audit
        model.dextoolslink = dextoolslink
        model.tokensnifferlink = tokensnifferlink
        model.img_path = img_path
        model.save()
