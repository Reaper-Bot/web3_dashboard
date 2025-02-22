from celery import Celery
from web3_utils import get_contract_balance


celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def track_contract_balance(project_id, contract_address):
    balance = get_contract_balance(project_id, contract_address)
    print(f"Balance of {contract_address}: {balance} ETH")
    return balance
