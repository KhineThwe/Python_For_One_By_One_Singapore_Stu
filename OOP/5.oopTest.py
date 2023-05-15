class myClass:
    def __init__(self,cat1,cat2):
        self.cat1 = cat1
        self.cat2 = cat2
    def mInfo(self):
        print("From mInfo: ",self.cat1,":",self.cat2)

if __name__ == '__main__':
    cat1 = input("Enter cat1: ")
    cat2 = input("Enter cat2: ")
    obj = myClass(cat1,cat2)
    obj.mInfo()
