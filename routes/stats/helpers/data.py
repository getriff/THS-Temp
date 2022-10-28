def get_func_distribution(all_txns):
    func_dict = {}
    # print(all_txns)
    for i in all_txns:
        if i["functionName"].split("(")[0] not in func_dict.keys():
            func_dict[i["functionName"].split("(")[0]] = 1
        else:
            func_dict[i["functionName"].split("(")[0]] += 1
    return func_dict
