import numpy as np

class Forward():
    def __init__(self, f):
        self.f = f

    def get_value(self):
        return self.f.real
     
    def get_derivative(self):
        return self.f.dual