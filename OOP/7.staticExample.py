class Dates:
    def __init__(self,date):
        self.date = date

    def getData(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")

if __name__ == '__main__':
    date = Dates("15-12-2023")
    date1 = "15/12/2023"
    dateWithDash = Dates.toDashDate(date1)

    dateWithObj = date.getData()

    if dateWithDash == dateWithObj:
        print("They are equal")
    else:
        print("They are not equal")

