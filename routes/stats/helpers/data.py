def get_func_distribution(all_txns):
    func_dict = {}
    methodId_dict = {}
    # print("all txns", all_txns)
    try:
        for i in all_txns:
            if i["functionName"].split("(")[0] not in func_dict.keys():
                func_dict[i["functionName"].split("(")[0]] = 1
            else:
                func_dict[i["functionName"].split("(")[0]] += 1

            if i["methodId"] not in methodId_dict.keys():
                methodId_dict[i["methodId"]] = 1
            else:
                methodId_dict[i["methodId"]] += 1

        return func_dict, methodId_dict
    except Exception:
        return "Not available"


def get_tag(verified, tx_len):

    if verified == 0 and tx_len >= 2500:
        tag = "Safe"
    elif verified == 0 and tx_len < 500:
        tag = "Unsafe"
    elif verified == 1 and tx_len >= 2500:
        tag = "Verified Safe"
    elif verified == 1 and tx_len < 2500:
        tag = "Unknown"
    else:
        # verified and tx len between 500 and 2500
        tag = "Unknown"
    return tag
