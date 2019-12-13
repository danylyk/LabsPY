import os
import hashlib
import threading
import math

class FilesInDirectory:
    def __init__ (self, dir:str):
        self.dir = dir
        self.duplicates = {}
        self.duplicates_pos = []
        self.files_list = []

        self.__files_from_dir()

    def __files_from_dir (self):
        for dir in os.walk(self.dir):
            for i in dir[2]:
                self.files_list.append(dir[0]+"/"+i)

    def get_duplicates (self, n):
        shift = math.ceil(len(self.files_list)/n)
        start = -shift
        threades = []

        while True:
            start += shift
            end = start+shift
            if end > len(self.files_list): end = len(self.files_list)
            t = threading.Thread(target=self.__get_duplicates_proccess, args=[start, end])
            t.start()
            threades.append(t)
            if end == len(self.files_list): break

        for t in threades:
            t.join()

        res = []
        for i in self.duplicates_pos:
            res.append(self.duplicates[i])

        return res

    def __get_duplicates_proccess (self, start, end):
        for i in range(start, end):
            file = open(self.files_list[i], 'rb')
            hasher = hashlib.md5()
            buf = file.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(65536)
            file.close()
            data = hasher.hexdigest()
            try:
                self.duplicates[data].append(self.files_list[i])
                if len(self.duplicates[data]) == 2:
                    self.duplicates_pos.append(data)

            except: self.duplicates[data] = [self.files_list[i]]


if __name__ == '__main__':
    dir = FilesInDirectory("C:/Users/webvi/OneDrive/Documents/GitHub/")
    print(dir.get_duplicates(20))