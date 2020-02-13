from dataclasses import dataclass


@dataclass
class DefaultValues:
    registry_address: str = ""
    identity_implementation_address: str = ""
    identity_proxy_factory_address: str = ""


_LAIKA_DEFAULT_VALUES = DefaultValues(
    identity_implementation_address="0x8BEe92893D3ec62e5B3EBBe4e536A60Fd9AFc9D7",
    identity_proxy_factory_address="0x8D2720877Fa796E3C3B91BB91ad6CfcC07Ea249E",
)

_TLBC_DEFAULT_VALUES = DefaultValues(
    registry_address="0x02c3cA67cF3310295195173cb654cfd61f4c849D"
)

_CHAIN_ID_TO_DEFAULTS_MAPPING = {
    18538: _LAIKA_DEFAULT_VALUES,
    4660: _TLBC_DEFAULT_VALUES,
}


def get_default_values_by_chain_id(chain_id: int) -> DefaultValues:
    return _CHAIN_ID_TO_DEFAULTS_MAPPING.get(chain_id, DefaultValues())
