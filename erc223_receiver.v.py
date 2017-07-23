# Solidity-Compatible improved ERC20 Token (ERC223)
# Implements https://github.com/ethereum/EIPs/issues/223
# Bsed on Phil Daian's pull request: https://github.com/ethereum/viper/pull/275

# This contract implements the receiver side (as a contract) of token transfer
# By specifying the tokenFallback function, it enables token transfer from and to
# contract address.

# token_wallet is a map, (key, value) is (tokenAddress, new struct) where struct
# contains infomation about data sent, number of token sent and the sender.
token_wallet: {sender: address, value: num256, data: bytes<= 4096}[address]

# Set up function
def __init__():
    # Do remember to specify payable or not.
    number_of_incoming_token_transfer = 0


def tokenFallback(_from: address, _value: num256, _data: bytes <= 4096):
    self.payable(false, msg.value)
    if num256_lt(_value, as_num256(0)):
        return
    if self.is_overflow_add(_value, self.token_wallet[msg.sender].value):
        return
    self.token_wallet[msg.sender].sender = _from
    self.token_wallet[msg.sender].value = num256_add(_value, self.token_wallet[msg.sender].value)
    self.token_wallet[msg.sender].data = _data

# Utility function for Solidity payable compatibility
def is_overflow_add(a : num256, b : num256) -> bool:
    self.payable(false, msg.value)
    result = num256_add(a, b)
    return num256_lt(result, a)

def is_overflow_sub(a : num256, b : num256) -> bool:
    self.payable(false, msg.value)
    return num256_lt(a, b)

def payable(payable : bool, value : wei_value):
    if ((not payable) and (value > 0)):
        assert(false)
