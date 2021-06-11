# blockchain

import datetime
from block import Block as block


# list for first block
blockchain = [block.create_origin_block()]

print("Origin block created !")
print("Hash: {0}".format(blockchain[-1].hash))

# create 10 blocks, the news block as added
# in lastest block
for i in range(1, 11):
    blockchain.append(block(
        blockchain[-1].hash,
        "DATA !",
        datetime.datetime.now())
    )
    print("Block #{0} is created".format(i))
    print("Block #%d hash : %s" % (i, blockchain[i].hash))
