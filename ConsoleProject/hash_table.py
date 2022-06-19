
class Hash_Table:
    def __init__(self):
        self.size=0

    def hash(self,key):
        sum=0
        for l in key:
            sum+=ord(l)
        return sum % self.size





