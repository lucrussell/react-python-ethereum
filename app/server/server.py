from flask import Flask, render_template
from web3 import Web3, HTTPProvider
import json

from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
'''

app = Flask(__name__, static_folder='../static/dist', template_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return get_info()


@app.route('/deploy_contract')
def deploy_contract():
    return do_deploy_contract()


@app.route('/call_contract')
def call_contract():
    # TODO: accept inputs from page
    return do_call_contract()


def get_info():
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    return web3.eth.coinbase


def do_deploy_contract():
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:Greeter']

    # web3.py instance
    w3 = Web3(HTTPProvider('http://localhost:8545'))

    # Instantiate and deploy contract
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # Get transaction hash from deployed contract
    tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

    # Get tx receipt to get contract address
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']
    print(f'Contract address: {contract_address}')
    abi = json.dumps(contract_interface['abi'])
    print(f'Contract abi: {abi}')

    # TODO: Don't need to call it here
    # Contract instance in concise mode
    contract_instance = w3.eth.contract(contract_interface['abi'], contract_address,
                                        ContractFactoryClass=ConciseContract)

    # Getters + Setters for web3.eth.contract object
    print('Contract value: {}'.format(contract_instance.greet()))
    contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
    print('Setting value to: Nihao')
    return abi


def do_call_contract(address, abi):
    print(address)
    print(abi)


if __name__ == '__main__':
    app.run()
