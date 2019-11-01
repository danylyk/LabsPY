import urllib.request

def GetWordCount (url:str, word:str):
  #res = urllib.request.urlretrieve(url, 'File.txt') 
  res = urllib.request.urlopen(url)
  res = res.read().decode("utf-8")
  res = res.split(word)
  return len(res)-1

if __name__ == "__main__":
  words = GetWordsCount("https://borscht.mobi/SimpleFile.txt", "ipsum")
  print(words)