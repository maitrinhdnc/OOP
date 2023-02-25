class User:
  def __init__(self, name, birthyear):
    self.name = name
    self.birthyear = birthyear

  def get_name(self):
    return self.name.upper()

  def age(self, current_year):
    return current_year - self.birthyear

if __name__ == '__main__':
  user1 = User('John', 1999)
  print(user1.age(2023))
  print(user1.get_name())