import click
from deploy_tools.files import InvalidAddressException, validate_and_format_address


def validate_address(ctx, param, value):
    try:
        return value if not value else validate_and_format_address(value)

    except InvalidAddressException as e:
        raise click.BadParameter(
            f"The address parameter is not recognized to be an address: {value}"
        ) from e


jsonrpc_option = click.option(
    "--jsonrpc",
    help="JSON-RPC URL of the Trustlines Blockchain node",
    default="https://tlbc.rpc.anyblock.tools",
    show_default=True,
    metavar="URL",
)

registry_address_option = click.option(
    "--registry-address",
    help=("The address of the CurrencyNetworkRegistry contract."),
    default="0x02c3cA67cF3310295195173cb654cfd61f4c849D",
    type=str,
    required=True,
    callback=validate_address,
)

from_block_option = click.option(
    "--from-block",
    help=("The block number from which to fetch registered currency contracts."),
    default=0,
    type=int,
)

registrar_address_option = click.option(
    "--registrar-address",
    help=("An address to filter currency networks by their registrar property."),
    type=str,
    required=False,
    callback=validate_address,
)

save_to_file_option = click.option(
    "--save-to-file",
    help=(
        "Save fetched currency networks to file in the format as expected by the relay."
    ),
    is_flag=True,
    default=False,
    show_default=True,
)

address_file_name_option = click.option(
    "--address-file-name",
    help=(
        "File name where to store address file in current working directory. See '--save-to-file'."
    ),
    type=click.Path(dir_okay=False),
    default="addresses.json",
    show_default=True,
)

identity_implementation_address_option = click.option(
    "--identity-implementation-address",
    help=(
        "The address of the Identity implementation contract (relevant for the address file)."
    ),
    default="0x8BEe92893D3ec62e5B3EBBe4e536A60Fd9AFc9D7",
    type=str,
    required=True,
    callback=validate_address,
)

identity_proxy_factory_address_option = click.option(
    "--identity-proxy-factory-address",
    help=(
        "The address of the IdentityProxyFactory contract (relevant for the address file)."
    ),
    default="0x8D2720877Fa796E3C3B91BB91ad6CfcC07Ea249E",
    type=str,
    required=True,
    callback=validate_address,
)
