class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_sum(self):
        return self.x + self.y
        
    def get_difference(self):
        return self.x - self.y
        
    def get_product(self):
        return self.x * self.y
        
    def get_quotient(self):
        return self.x / self.y
        
    def get_remainder(self):
        return self.x % self.y
