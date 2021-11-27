from datetime import datetime

class DataInfo:

    def __init__(self, filename):
        self.filename = filename
        self.read_file()
        self.result = self.date_data()

    def read_file(self):
        with open(self.filename, "r") as file:
            data = file.read().split("\n")
        return data

    def result(self):
        return self.result

    def __repr__(self):
        return f"{self.result}"

    def domain_data(self):
        data_domains = [domains.replace(".", "") for domains in self.read_file()]
        return data_domains


    def name_data(self):
        surnames = [surname.split("\t")[1] for surname in self.read_file()]
        return surnames


    def date_data(self):
        dates = self.read_file()
        num = 0
        while (num < len(dates)):
            if (" - " in dates[num]):
                dates[num] = dates[num].split(" - ")[0].split(' ')
                dates[num][0] = dates[num][0].replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
                dates[num] = " ".join(dates[num])
                num += 1
            else:
                dates.pop(num)
        return [{"date_original": date, "date_modified": datetime.strptime(date, "%d %B %Y").strftime("%d/%m/%Y")} for date in dates]
