#Global variable
# a list of funders, each of which is a mapping.
funders = {sender: address, value: wei_value}[num]
#
nextFounderIndex: num
beneficiary: address
deadline: timestamp
goal: wei_value
refundIndex: num
timelimit: timedelta

# setup global variables
def __init__(_beneficiary: address, _goal: wei_value, _timelimit: timedelta):
    self.beneficiary = _beneficiary
    self.deadline = block.timestamp + _timelimit
    self.goal = _goal
    self.timelimit = _timelimit

# participate in the crowdfunding campaign
def participate():
    assert block.timestamp < self.deadline
    nfi = self.nextFounderIndex
    self.funders[nfi] = {sender: msg.sender, value: msg.value}
    self.nextFounderIndex = nfi + 1

# enough money was raised, sent money to the beneficiary
def finalize():
    assert block.timestamp >= self.deadline and self.balance >= self.goal
    selfdestruct(self.beneficiary)

# not enough money, refunnd everybody.
# max 30 ppl at a time to avoid gas limit.
def refunnd():
    ind = self.refundIndex
    for i in range(ind, ind+30):
        if i >= self.nextFounderIndex:
            self.refundIndex = self.nextFounderIndex
            return
        temp: num
        temp = self.funders[i]
        self.funders[i].value = 0
        send(self.funders[i].sender, temp)
        self.funders[i] = None
    self.refundIndex = ind + 30
