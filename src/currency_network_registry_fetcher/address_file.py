import json
from typing import List

from currency_network_registry_fetcher.currency_network import CurrencyNetwork


class AddressFile:
    def __init__(
        self,
        file_name: str,
        currency_networks: List[CurrencyNetwork],
        identity_implementation_address: str,
        identity_proxy_factory_address: str,
    ) -> None:
        self._file_name = file_name
        currency_network_addresses = [
            currency_network.address for currency_network in currency_networks
        ]
        self._content = {
            "networks": currency_network_addresses,
            "identityImplementation": identity_implementation_address,
            "identityProxyFactory": identity_proxy_factory_address,
        }

    def save_to_disk(self) -> None:
        with open(self._file_name, "w") as f:
            json.dump(self._content, f)
