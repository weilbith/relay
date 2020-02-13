from web3.datastructures import AttributeDict


class CurrencyNetwork:
    def __init__(self, event_log: AttributeDict) -> None:
        assert "args" in event_log
        assert "_name" in event_log.args
        assert "_symbol" in event_log.args
        assert "_decimals" in event_log.args
        assert "_registeredBy" in event_log.args
        assert "_address" in event_log.args

        self.name = event_log.args._name
        self.symbol = event_log.args._symbol
        self.decimals = event_log.args._decimals
        self.registered_by = event_log.args._registeredBy
        self.address = event_log.args._address

    def __repr__(self):
        return (
            f"CurrencyNetwork(name={self.name}; symbol={self.symbol}; decimals={self.decimals}; "
            f"registered_by={self.registered_by}; address={self.address})"
        )
