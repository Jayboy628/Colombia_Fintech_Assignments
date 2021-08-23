import subprocess
import json
import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
from bit import PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from constants import *

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# load environment
load_dotenv

# load Mnemonic environment
mnemonic = os.getenv('mnemonic', "ready render hobby seed vendor credit dust slam balance option moon stomach")
print(mnemonic)


# Function create wallet
def derive_wallets(mnemonic, coin, numderive):
    """Use the subprocess library to call the php file script from Python"""
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    keys = json.loads(output)
    return keys


# Create coin for wallet
coins = {"eth", "btc-test", "btc"}
numderive = 3
keys = {}
for coin in coins:
    keys[coin] = derive_wallets(os.getenv('mnemonic'), coin, numderive=3)

eth_priv_key = keys["eth"][0]['privkey']
btc_priv_key = keys['btc-test'][0]['privkey']

print(json.dumps(eth_priv_key, indent=5, sort_keys=True))
print(json.dumps(btc_priv_key, indent=5, sort_keys=True))
print(json.dumps(keys, indent=4, sort_keys=True))


# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin.upper() == 'ETH':
        return Account.privateKeyToAccount(priv_key)
    if coin.upper() == 'BTCTEST':
        return PrivateKeyTestnet(priv_key)

eth_account = priv_key_to_account(ETH, eth_priv_key)
btc_account = priv_key_to_account(BTCTEST, btc_priv_key)
