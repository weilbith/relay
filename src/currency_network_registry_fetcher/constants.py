MINIMAL_REGISTRY_CONTRACT_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_address",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "_registeredBy",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "_name",
                "type": "string",
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "_symbol",
                "type": "string",
            },
            {
                "indexed": False,
                "internalType": "uint8",
                "name": "_decimals",
                "type": "uint8",
            },
        ],
        "name": "CurrencyNetworkAdded",
        "type": "event",
    }
]

CURRENCY_NETWORK_FILTER_EVENT_NAME = "CurrencyNetworkAdded"
