from electrumx.lib.coins import Bitgesell, BitgesellTestnet, Coin
from electrumx.lib.tx import DeserializerSegWit


def test_bitgesell_mainnet_params_match_core():
    coin = Coin.lookup_coin_class("Bitgesell", "mainnet")

    assert coin is Bitgesell
    assert coin.SHORTNAME == "BGL"
    assert coin.DESERIALIZER is DeserializerSegWit
    assert coin.GENESIS_HASH == (
        "00000018cdcfeeb4dfdebe9392b855cf"
        "ea7d6ddb953ef13f974b58773606d53d"
    )
    assert coin.P2PKH_VERBYTE == bytes([10])
    assert coin.P2SH_VERBYTES == (bytes([25]),)
    assert coin.WIF_BYTE == bytes([128])
    assert coin.RPC_PORT == 8332


def test_bitgesell_testnet_params_match_core():
    coin = Coin.lookup_coin_class("Bitgesell", "testnet")

    assert coin is BitgesellTestnet
    assert coin.SHORTNAME == "TBGL"
    assert coin.GENESIS_HASH == Bitgesell.GENESIS_HASH
    assert coin.P2PKH_VERBYTE == bytes([34])
    assert coin.P2SH_VERBYTES == (bytes([50]),)
    assert coin.WIF_BYTE == bytes([239])
    assert coin.XPUB_VERBYTES == bytes.fromhex("043587cf")
    assert coin.XPRV_VERBYTES == bytes.fromhex("04358394")
    assert coin.RPC_PORT == 18332
