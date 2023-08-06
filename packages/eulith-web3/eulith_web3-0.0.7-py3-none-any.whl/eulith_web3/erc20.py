from enum import Enum
from typing import Union, Optional

from eth_typing import ChecksumAddress, Address
from web3 import Web3

from eulith_web3.contract_bindings.i_e_r_c20 import IERC20


class TokenSymbol(str, Enum):
    USDT = 'USDT'
    BNB = 'BNB'
    USDC = 'USDC'
    BUSD = 'BUSD'
    MATIC = 'MATIC'
    STETH = 'stETH'
    WETH = 'WETH'
    LDO = "LDO"
    CRV = 'CRV'
    CVX = 'CVX'
    BAL = 'BAL'
    BADGER = 'BADGER'
    ONEINCH = '1INCH'
    UNI = 'UNI'
    LINK = 'LINK'
    APE = 'APE'
    GMT = 'GMT'


class EulithERC20(IERC20):
    def __init__(self, web3: Web3, contract_address: Optional[Union[Address, ChecksumAddress]] = None):
        super().__init__(web3, contract_address)
