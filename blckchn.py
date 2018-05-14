#uses Flask and Requests

class blockchain(object):
    def __init__(self):
        self.chain = []
        self.trans = []

    def new_block(self):
        pass

    def new_trans(self,sender,rec,amount):
        self.trans.append
        ({
            'sender': sender,
            'recipient': rec,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

