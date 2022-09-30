import inspect
from pprint import pprint
from dataclasses import asdict, astuple, dataclass, field


@dataclass(frozen=True, order=True)
class Comment:
  id: int
  text: str = ""
  author: str = ""
  replies: list[int] = field(default_factory=list)
  
def main():
  comment = Comment(1, "I just subbed!","Slats")
  c2 = Comment(2, "Test of it all","Slats",[1,2])
  
  print(comment)
  print(c2)
  #print(type(comment))
  #print(astuple(comment))
  print(asdict(comment))
  print(asdict(c2))
  
  #pprint(inspect.getmembers(Comment, inspect.isfunction))
  
if __name__ == "__main__":
  main()
