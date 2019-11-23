import urllib.request
import re

def GetWordsCount (url:str):
  #res = urllib.request.urlretrieve(url, 'File.txt') 
  data = urllib.request.urlopen(url)
  data = data.read().decode("utf-8").lower().replace("\'", "")
  a = re.search('(\w+(?:-\w+)+|\w+)', data)
  while a:
      print(a.group(0) + ": " + str(len(re.findall(r'\b'+a.group(0)+r'\b', data))))
      data = re.sub(r'\b'+a.group(0)+r'\b', '', data)
      a = re.search('(\w+(?:-\w+)+|\w+)', data)

if __name__ == "__main__":
  words = GetWordsCount("https://raw.githubusercontent.com/dscape/spell/master/test/resources/big.txt")
