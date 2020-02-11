from typing import List

from web3 import Web3
from web3.datastructures import AttributeDict

from currency_network_registry_fetcher.constants import (
    CURRENCY_NETWORK_FILTER_EVENT_NAME,
    MINIMAL_REGISTRY_CONTRACT_ABI,
)
from currency_network_registry_fetcher.currency_network import CurrencyNetwork


class RegistryContract:
    def __init__(self, web3: Web3, address: str) -> None:
        self._contract = web3.eth.contract(
            address=address, abi=MINIMAL_REGISTRY_CONTRACT_ABI
        )

    def get_currency_networks(self, from_block: int) -> List[AttributeDict]:
        event_logs = self._contract.events[CURRENCY_NETWORK_FILTER_EVENT_NAME].getLogs(
            fromBlock=from_block
        )
        currency_networks = self._convert_logs_to_currency_network(event_logs)
        return currency_networks

    def _convert_logs_to_currency_network(
        self, event_logs: List[AttributeDict]
    ) -> List[CurrencyNetwork]:
        return [CurrencyNetwork(event_log) for event_log in event_logs]
