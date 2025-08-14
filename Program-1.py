class Calculator:
    def __init__(self,a:float,b:float,operation:str):
      self.a=a
      self.b=b
      self.operation=operation
    def calculate(self):
      if self.operation == "add":
        return self.a + self.b
      elif self.operation == "sub":
        return self.a - self.b
      elif self.operation == "mul":
        return self.a * self.b
      elif self.operation == "div":
        return self.a / self.b if self.b != 0 else "Error: Division by zero"
      else:
        return "Invalid operation"
calc = Calculator(10, 5, "div")  
print("Result:", calc.calculate())
