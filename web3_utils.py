from web3 import Web3

infura_url = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(infura_url))

def get_contract_balance(contract_address):
    balance = w3.eth.get_balance(contract_address)
    return w3.from_wei(balance, 'ether')
