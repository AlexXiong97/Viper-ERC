# Solidity-Compatible improved ERC20 Token (ERC223)
# Implements https://github.com/ethereum/EIPs/issues/223
# Bsed on Phil Daian's pull request: https://github.com/ethereum/viper/pull/275

# The use of the num256 datatype as in this token is not
# recommended, as it can pose security risks.

# Events are not yet supported in Viper, so events are NOT
# included in this token.  This makes this token incompatible
# with some log-only clients.

# This token is intended as a proof of concept towards
# language interoperability and not for production use.

# To maintain compatibility with both Solidity tokens and the
# existing ERC20 specification, this contract will throw
# only when a non-payable function is attempted to be called
# with some value; otherwise (on conditions like overflow),
# false will be returned.

# Implement tokenFallback Funciton to prevent accidentally
# sending tokens to a contract address by allowing contract
# to handle incoming tokens.

balances: num256[address]
allowances: (num256[address])[address]
num_issued: num256
token_name: bytes32
token_symbol: bytes32
token_decimals: int128


# Setup global variables
def __init__(_token_name: bytes32, _token_symbol: bytes32, _token_decimals: int128):
    self.payable(false, msg.value)
    self.num_issued = as_num256(0)
    self.token_name = _token_name
    self.token_symbol = _token_symbol
    # decimal digits no more than 10
    assert (_token_decimals > 10)
    self.token_decimals = _token_decimals

def deposit() -> bool:
    self.payable(true, msg.value)
    if self.is_overflow_add(self.balances[msg.sender], as_num256(msg.value)):
        return false
    if self.is_overflow_add(self.num_issued, as_num256(msg.value)):
        return false
    self.balances[msg.sender] = num256_add(self.balances[msg.sender], as_num256(msg.value))
    self.num_issued = num256_add(self.num_issued, as_num256(msg.value))
    return true

def withdraw(_value : num256) -> bool:
    self.payable(false, msg.value)
    if self.is_overflow_sub(self.balances[msg.sender], _value):
        return false
    if self.is_overflow_sub(self.num_issued, _value):
        return false
    self.balances[msg.sender] = num256_sub(self.balances[msg.sender], _value)
    self.num_issued = num256_sub(self.num_issued, _value)
    send(msg.sender, as_wei_value(as_num128(_value), wei)) # todo boundary checks
    return true

def totalSupply() -> num256(const):
    self.payable(false, msg.value)
    return self.num_issued

def name() -> bytes32(const):
    return self.token_name

def symbol() -> bytes32(const):
    return self.token_symbol

def balanceOf(_owner : address) -> num256(const):
    self.payable(false, msg.value)
    return self.balances[_owner]

def transfer(_to : address, _value : num256) -> bool:
    self.payable(false, msg.value)
    if self.is_overflow_add(self.balances[_to], _value):
        return false
    if self.is_overflow_sub(self.balances[msg.sender], _value):
        return false
    self.balances[msg.sender] = num256_sub(self.balances[msg.sender], _value)
    self.balances[_to] = num256_add(self.balances[_to], _value)
    return true

def transferFrom(_from : address, _to : address, _value : num256) -> bool:
    self.payable(false, msg.value)
    allowance = self.allowances[_from][_to]
    if self.is_overflow_add(self.balances[_to], _value):
        return false
    if self.is_overflow_sub(self.balances[_from], _value):
        return false
    if self.is_overflow_sub(allowance, _value):
        return false
    self.balances[_from] = num256_sub(self.balances[_from], _value)
    self.balances[_to] = num256_add(self.balances[_to], _value)
    self.allowances[_from][_to] = num256_sub(allowance, _value)
    return true

def approve(_spender : address, _value : num256) -> bool:
    self.payable(false, msg.value)
    if num256_gt(self.allowances[msg.sender][_spender], as_num256(0)) and num256_lt(as_num256(0), _value):
        # Require reset to 0 to mitigate https://docs.google.com/document/d/1YLPtQxZu1UAvO9cZ1O2RPXBbT0mooh4DYKjA_jp-RLM/edit#heading=h.m9fhqynw2xvt
        return false
    self.allowances[msg.sender][_spender] = _value
    return true

def allowance(_owner : address, _spender : address) -> num256:
    self.payable(false, msg.value)
    return self.allowances[_owner][_spender]


# Utility functions for overflow checking
def is_overflow_add(a : num256, b : num256) -> bool:
    self.payable(false, msg.value)
    result = num256_add(a, b)
    return num256_lt(result, a)

def is_overflow_sub(a : num256, b : num256) -> bool:
    self.payable(false, msg.value)
    return num256_lt(a, b)

# Utility function for Solidity payable compatibility
def payable(payable : bool, value : wei_value):
    if ((not payable) and (value > 0)):
        assert(false)
