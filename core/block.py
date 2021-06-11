# blockchain block

import hashlib, datetime


class Block:
    """
    data of block
    """
    def __init__(self, previous_block_hash, data, timestamp):
        super(Block, self).__init__()
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def create_origin_block():
        """
        origin block 
        """
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        """
        get first hash function
        """
        header_bin = (
            str(self.previous_block_hash) + 
            str(self.data) +
            str(self.timestamp)
        ).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
        