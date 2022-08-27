company_dict = dict()

while True:
    info = input()
    if info == "End":
        break
    info = info.split(' -> ')
    company = info[0]
    ident = info[1]
    if company not in company_dict:
        company_dict[company] = [ident]
    else:
        if ident not in company_dict[company]:
            company_dict[company].append(ident)
for company in company_dict:
    print(company)
    id_list = ["-- "+string for string in company_dict[company]]
    spisak = "\n".join(id_list)
    print(spisak)
