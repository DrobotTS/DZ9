from dz_6_class_file import DataInfo

filename = "domains.txt"
data_result = DataInfo(filename)
dom_res = data_result.domain_data()
print(dom_res, sep="\n")

filename = "names.txt"
data_result = DataInfo(filename)
sur_res = data_result.name_data()
print(sur_res, sep="\n")

filename = "authors.txt"
data_result = DataInfo(filename)
date_res = data_result.date_data()
print(date_res, sep="\n")
