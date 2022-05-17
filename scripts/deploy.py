from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_script import getAccount, LOCAL_BLOCKCHAIN_ENVIRONMENT
from scripts.deploy_mocks import deploy_mocks


def deploy_fund_me():
    account = getAccount()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    FundMe.deploy(price_feed_address, {"from" : account}, publish_source=config["networks"][network.show_active()].get("verify", False))


def main():
    deploy_fund_me()