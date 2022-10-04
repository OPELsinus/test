import os
import pandas as pd

class DirSearch:

    def __init__(self, root):
        self.root = root
        self.df = pd.DataFrame(columns=('path', 'name', 'extension'))
        self.count = 0

    def __getitem__(self, index):
        self.df = self.search()
        self.save()

        return self.df.iloc[index][0], self.df.iloc[index][1], self.df.iloc[index][2]

    def search(self):
        for path, subdirs, files in os.walk(self.root):
            for name in files:

                pure_name = name.split('.', maxsplit=1)

                if len(pure_name) == 1:
                    self.df.loc[self.count] = [path, pure_name[0], '']
                else:
                    self.df.loc[self.count] = [path, pure_name[0], pure_name[1]]
                self.count += 1
        return self.df

    def save(self):
        self.df.to_excel(self.root + '\\result.xlsx')
        # self.df.to_csv(self.root + '\\test.csv', sep='|', index=False)    To save without index

dir = os.path.dirname(os.path.realpath(__file__))
ds = DirSearch(dir)

print(ds[0])