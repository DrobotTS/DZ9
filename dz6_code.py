from dz_6_class_file import DataInfo

data_result = DataInfo("domains.txt", "names.txt", "authors.txt")
dom_res = data_result.domain_data()
sur_res = data_result.name_data()
print(dom_res, sur_res, data_result, sep="\n")
