# ERC20 Smart Contract.
#### Deploy your own ERC721 Collection easily!

Created using [OpenZeppelin](https://openzeppelin.com/)'s [ERC721](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol) and its extensions Smart Contracts.

### Features:

1. Mint
1. Whitelist Mint - Using Merkle Root
1. Reveal
1. Free mint for owner
1. Pause/Unpause
1. Set Price
1. Set URIs
1. Set maximum mint per transaction
1. Withdraw funds after sale
1. Compatible with any NFT Marketplace



### Prerequisites:

##### Rinkeby deployment
- [Python](https://www.python.org/downloads/)
- Brownie
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart terminal
pipx install eth-brownie
```
- A free [Infura](https://infura.io/) Project Id key for Rinkeby Network

### Instalation 

Clone this repo:

```
git clone https://github.com/andreitoma8/ERC721-Collection
cd ERC721-Collection
```

### Deploy to Rinkeby

- Add a `.env` file with the same contents of `.env.example`, but replaced with your variables.

- In `scripts/deploy.py` change the value of `NAME`, `SYMBOL`, `COST`, `MAX_SUPPLY` and `MAX_MINT_AMOUNT_PER_TX` to custom ones for your Collection.

- Run the command:
```
brownie run scripts/deploy.py --network rinkeby
```
The script will deploy your Smart Contract and verify it on Etherscan.

To deploy to any other network change rinkeby in the command with the name of the network:

```
brownie run scripts/deploy.py --network [network name]
```
and your `WEB3_INFURA_PROJECT_ID` in the `.env` file with a Project Id for that network.

### More info on how to set-up the Merkle Root whitelisting [here](https://medium.com/@ItsCuzzo/using-merkle-trees-for-nft-whitelists-523b58ada3f9).

##### Any feedback is much apreciated! 
##### If this was helpful please consider donating: 
`0xA4Ad17ef801Fa4bD44b758E5Ae8B2169f59B666F`

# Happy hacking!