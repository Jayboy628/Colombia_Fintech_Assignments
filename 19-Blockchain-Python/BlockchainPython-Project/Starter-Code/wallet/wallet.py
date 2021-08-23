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

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_account = priv_key_to_account(ETH,eth_priv_key)
btc_account = priv_key_to_account(BTCTEST,btc_priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient,amount):
    # YOUR CODE HERE
    global tx_data
    if coin.upper() == 'ETH':
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
        )
        tx_data = {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
        return tx_data
    
    if coin.upper() == 'BTCTEST':
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, recipient,amount):
    if coin.upper() == 'ETH':
        tx_eth = create_tx(coin, account, recipient, amount)
        sign = account.signTrasaction(tx_eth)
        result = w3.eth.sendRawTransaction(sign.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        tx_btctest = create_tx(coin, account, recipient, amount)
        sign_tx_btctest = account.sign_transaction(tx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_tx_btctest)
        return sign_tx_btctest