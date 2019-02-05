#! pytest


import pytest
import attr
from tldeploy import identity
from relay.api import schemas


def gen_meta_transactions():
    mt = identity.MetaTransaction(
        from_="0xF2E246BB76DF876Cef8b38ae84130F4F55De395b",
        to="0x51a240271AB8AB9f9a21C82d9a85396b704E164d",
        value=0,
        data=bytes.fromhex(
            "46432830000000000000000000000000000000000000000000000000000000000000000a"
        ),
        nonce=1,
        extra_data=b"",
        signature=bytes.fromhex(
            "6d2fe56ef6648cb3f0398966ad3b05d891cde786d8074bdac15bcb92ebfa722248"
            "9b8eb6ed87165feeede19b031bb69e12036a5fa13b3a46ad0c2c19d051ea9101"
        ),
    )
    return [
        mt,
        attr.evolve(mt, data=b""),
        attr.evolve(mt, extra_data=b"foo"),
        attr.evolve(mt, nonce=0),
        attr.evolve(mt, value=1234),
        attr.evolve(mt, nonce=2 ** 256 - 1),
    ]


@pytest.mark.parametrize("meta_transaction", gen_meta_transactions())
def test_meta_transaction_schema(meta_transaction):
    dumped = schemas.MetaTransactionSchema().dump(meta_transaction).data
    print("DUMPED", dumped)

    loaded = schemas.MetaTransactionSchema().load(dumped).data
    print("LOADED", loaded)

    assert loaded == meta_transaction
