# Creating a Full Stack Web Application with Ethereum, Python, NPM, Webpack and React

TODO: This is a work in progress

This project shows you how to build a simple web application which communicates with the Ethereum blockchain. The structure of the project is based on this [full stack template](https://github.com/angineering/FullStackTemplate).

## Walkthrough

You can find a walkthrough of how to build the application from scratch
[here](TODO).


## Prerequisites
After cloning this repository to your computer, you need to perform the following steps to be able to run it:

1) Install Geth in dev mode. Instructions below are for Ubuntu, instructions for other platforms are [here](https://github.com/ethereum/go-ethereum/wiki/Installing-Geth).

    sudo apt-get install software-properties-common
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install ethereum
    $ geth --dev account new (enter passphrases when prompted)
    $ geth --dev --rpc --datadir "~/.ethereum-dev" --mine --minerthreads 1 console 2>> ~/.ethereum-dev.log

2) Set up Python and start `server.py`. One option for managing multiple Python versions and virtual environments is [pyenv](https://github.com/pyenv/pyenv) with the `pyenv-virtualenv` and `pyenv-virtualenvwrapper` plugins. There is a quick reference for how to set this up [here](http://lucrussell.com/pyenv-quick-reference/):

    pyenv versions
    pyenv install 3.6.4
    mkvirtualenv --python=`pyenv which python` react_python_ethereum
    pip install -r requirements.txt
    cd app/server; python server.py

3) [Install Node and npm](https://www.npmjs.com/get-npm)
4) Start the npm watcher:

    cd app/static
    npm install
    npm run watch

5) Go to http://localhost:5000

