from dz_6_class_file import DataInfo

data_result = DataInfo("domains.txt", "names.txt", "authors.txt")
dom_res = data_result.domain_data()
sur_res = data_result.name_data()
date_res = data_result.date_data()
print(data_result, dom_res, sur_res, date_res, sep="\n")
