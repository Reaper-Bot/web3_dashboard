from celery import Celery
from web3_utils import get_contract_balance

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def monitor_contract(contract_address):
    balance = get_contract_balance(contract_address)
    print(f"Contract {contract_address} Balance: {balance} ETH")
