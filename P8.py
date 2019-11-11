import os

class Directory:
    def __init__ (self, dir:str):
        self.dir = dir

    def files_list (self):
        return os.listdir(self.dir)

    def get_duplicates (self):
        files = self.files_list()
        res = []
        i = 0
        while i < len(files):
            with open(self.dir+files[i], 'rb') as file:
                f1 = file.readlines()
            found = False
            j = i+1
            while j < len(files):
                with open(self.dir+files[j], 'rb') as file:
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

dir = Directory("C:/Users/webvi/OneDrive/Робочий стіл/P8/")
print(dir.get_duplicates())