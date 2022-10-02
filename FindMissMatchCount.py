class FindMissMatchCount:

  def __init__(self, str):
      self.str=str

  def getCountOfMismatch(self):
      print(str)
      i=1
      j=2
      counter=0
      while i<=len(self.str)-2:
          a=self.str[:i]
          b=self.str[i:j]
          c=self.str[j:]
          print(f"{a} : {b} : {c}")
          if(a+b!=b+c or a+b!=c+a or b+c!=c+a):
              counter+=1
          if j<len(self.str):
              j+=1
              print(f"j:{j}")
              if j==len(self.str):
                  print(f"i: {i}")
                  i+=1
                  j=i+1
      return counter