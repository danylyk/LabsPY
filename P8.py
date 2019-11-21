import os

class FilesInDirectory:
    def __init__ (self, dir:str):
        self.dir = dir

    def files_list (self):
        return [a for a in self.files_from_dir(self.dir)]

    def files_from_dir (self, dir):
        for item in os.listdir(dir):
            if os.path.isdir(dir+item):
                yield from self.files_from_dir(dir+item+"/")
            else:
                yield dir+item

    def get_duplicates (self):
        files = self.files_list()
        res = []
        i = 0
        while i < len(files):
            with open(files[i], 'rb') as file:
                f1 = file.readlines()
            found = False
            j = i+1
            while j < len(files):
                with open(files[j], 'rb') as file:
                    f2 = file.readlines()
                if (str(f1) == str(f2)):
                    if found == False:
                        res.append([])
                        res[len(res)-1].append(files[i])
                        found = True
                    res[len(res)-1].append(files[j])
                    files.pop(j)
                    j -= 1;
                j += 1;
            files.pop(i)
        return res

if __name__ == '__main__':
    dir = FilesInDirectory("C:/Users/webvi/OneDrive/Робочий стіл/P8/")
    print(dir.get_duplicates())
