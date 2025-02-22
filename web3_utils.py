from web3 import Web3
from models import Project

def get_web3_instance(project_id):
    project = Project.query.get(project_id)
    if not project:
        return None
    return Web3(Web3.HTTPProvider(project.rpc_url))

def get_contract_balance(project_id, contract_address):
    w3 = get_web3_instance(project_id)
    if not w3:
        return None
    balance = w3.eth.get_balance(contract_address)
    return w3.from_wei(balance, 'ether')
