class MoneyBox:
    def __init__(self, capacity):
        # Your code here
        self.total_val = 0
        self.capacity = capacity
        
    def can_add(self, v):
        # True, if you can add v coins, False otherwise
        # Your code here
        if v < 0:
            return False
        if self.total_val + v > self.capacity:
            return False
        else:
            return True
      
    def add(self, v):
        # put v coins to moneybox
        # Your code here
        if self.can_add(v):
            self.total_val += v

