import urllib.request
import re

def GetWordsCount (url:str):
  #res = urllib.request.urlretrieve(url, 'File.txt') 
  data = urllib.request.urlopen(url)
  data = data.read().decode("utf-8").lower().replace("\'", "")
  data = re.findall('(\w+(?:-\w+)+|\w+)', data)
  res = [[data[0], 1]]
  for i in range(len(data)):
    new = True
    for j in range(len(res)):
      if res[j][0] == data[i]:
        res[j][1] += 1
        new = False
        break
    if new:
      res.append([data[i], 1])

  return res

if __name__ == "__main__":
  words = GetWordsCount("https://www.sample-videos.com/text/Sample-text-file-100kb.txt")
  for item in words:
    print(item[0]+": "+str(item[1])) 
