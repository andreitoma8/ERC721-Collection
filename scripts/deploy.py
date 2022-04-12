from lib2to3.pgen2.token import NAME
from brownie import accounts, config, ERC721Collection

DECIMALS = 10 ** 18

NAME = "Bored Ape Yacht Club"
SYMBOL = "BAYC"
COST = 0.01 * DECIMALS
MAX_SUPPLY = 10000
MAX_MINT_AMOUNT_PER_TX = 5


def main():
    account = accounts.add(config["wallets"]["from_key"])
    nft = ERC721Collection.deploy(
        NAME,
        SYMBOL,
        COST,
        MAX_SUPPLY,
        MAX_MINT_AMOUNT_PER_TX,
        {"from": account},
        publish_source=True,
    )
