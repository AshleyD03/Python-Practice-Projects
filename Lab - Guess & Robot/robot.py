class Robot:
  def __init__(self):
    self.info = ""
    self.guess = 50
    self.factor = 100

  def make_guess(self):
    self.factor = self.factor / 2
    if self.info == "HIGHER":
      self.guess = int(self.guess + self.factor)

    if self.info == "LOWER":
      self.guess = int(self.guess - self.factor)

    print(self.guess)
    return self.guess
  
  def tell(self, info):
    print(info)
    self.info = info