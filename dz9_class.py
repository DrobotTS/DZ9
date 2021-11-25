from datetime import datetime

class DataInfo:

    def __init__(self, domains_text, names_text, authors_text):
        self.domain_text = domains_text
        self.names_text = names_text
        self.authors_text = authors_text
        # self.read_file()
        self.result = self.date_data()

    # def read_file(self):
    #     with open(self.filename, "r") as file:
    #         data = file.readlines()
    #     return data

    def result(self):
        return self.result

    def __repr__(self):
        return f"{self.result}"

    def domain_data(self):
        with open(self.domain_text, 'r', encoding="utf-8") as domain_file:
            data_domains = [domains.replace(".", "")[:-1] for domains in domain_file.readlines()]
            return data_domains


    def name_data(self):
        with open(self.names_text, 'r', encoding="utf-8") as names_file:
            surnames = [surname.split("\t")[1] for surname in names_file.readlines()]
            return surnames


    def date_data(self):
        date_file = open(self.authors_text, "r").read()
        dates = date_file.split("\n")
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


