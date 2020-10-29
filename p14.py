class Movie:
  def __init__(self,name,director):
    self.name = name
    self.director = director
  @staticmethod
  def print_info(self):
    return f"<<{self.name}>> by {self.director}."
movie = Movie.print_info("The Matrix","Wachowski")
print(movie)
