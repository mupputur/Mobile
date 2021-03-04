def each_occurance_of_wovel(s):
      d={}
      v="aeiou"
      for i in s:
            if i in v:
                  if i not in d:
                        d[i]=1
                  else:
                        d[i]=d[i]+1
      return d
print(each_occurance_of_wovel("chaitanya battula"))
