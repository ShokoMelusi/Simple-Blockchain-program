import hashlib
from datetime import datetime


# class to represent a block
class Block: 
    def __init__(self, index, timestamp, data, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
   
   # function to calculate a hash
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.data).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()


# blockchain created using a list
MyBlockChain = []

# function to create a genesis block
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")

# adding a genesis block to the blockchain
MyBlockChain.append(create_genesis_block())

# function to create succeeding blocks
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block {}".format(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# adding 10 blocks to the blockchain
for i in range(0,10):
    MyBlockChain.append(next_block(MyBlockChain[-1]))

# printing data in each block
for item in MyBlockChain:
    print(item.data)