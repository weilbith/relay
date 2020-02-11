from typing import List

import click
from deploy_tools.cli import connect_to_json_rpc

from currency_network_registry_fetcher.address_file import AddressFile
from currency_network_registry_fetcher.cli_options import (
    address_file_name_option,
    from_block_option,
    identity_implementation_address_option,
    identity_proxy_factory_address_option,
    jsonrpc_option,
    registrar_address_option,
    registry_address_option,
    save_to_file_option,
)
from currency_network_registry_fetcher.currency_network import CurrencyNetwork
from currency_network_registry_fetcher.registry_contract import RegistryContract


@click.command()
@jsonrpc_option
@registry_address_option
@from_block_option
@registrar_address_option
@save_to_file_option
@address_file_name_option
@identity_implementation_address_option
@identity_proxy_factory_address_option
def main(
    jsonrpc: str,
    registry_address: str,
    from_block: int,
    registrar_address: str,
    save_to_file: bool,
    address_file_name: str,
    identity_implementation_address: str,
    identity_proxy_factory_address: str,
) -> None:
    web3 = connect_to_json_rpc(jsonrpc)
    registry_contract = RegistryContract(web3, registry_address)
    currency_networks = registry_contract.get_currency_networks(from_block)
    filtered_currency_networks = filter_currency_network_by_registrar(
        currency_networks, registrar_address
    )

    if save_to_file:
        address_file = AddressFile(
            address_file_name,
            filtered_currency_networks,
            identity_implementation_address,
            identity_proxy_factory_address,
        )
        address_file.save_to_disk()
        click.echo(f"Address file saved at '{address_file_name}'")

    else:
        for currency_network in filtered_currency_networks:
            click.echo(currency_network)


def filter_currency_network_by_registrar(
    currency_networks: List[CurrencyNetwork], registrar_address: str
) -> List[CurrencyNetwork]:
    if registrar_address:
        return [
            currency_network
            for currency_network in currency_networks
            if currency_network.registered_by == registrar_address
        ]

    else:
        return currency_networks
