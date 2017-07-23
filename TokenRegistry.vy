addressToSymbol: address[bytes32]
addressToName: address[bytes32]
addressToBaseUnit: address[num256]

#def __init()__:
	#nothing to do

#EIP22 assumes msg.sender is the token. not sure why?
def setSymbol(_symbol : bytes32) -> bool:
	self.addressToSymbol[msg.sender] = _symbol
	return true

#returns the symbol of a token address
def symbol(_token : address) -> bytes32:
	return self.addressToSymbol[_token]

#EIP22 assumes msg.sender is the token. not sure why?
def setName(_name : bytes32) -> bool:
	self.addressToName[msg.sender] = _name
	return true

#returns the name of a token address	
def name(_token : address) -> bytes32:
	return self.addressToName[_token]

#EIP22 assumes the msg.sender is the token
def setBaseUnit(_s : num256) -> bool:
	self.addressToBaseUnit[msg.sender] = _s
	return true

#returns the base unit of a token address
def baseUnit(_token : address) -> num256:
	return self.addressToBaseUnit[_token]

