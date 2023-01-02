import time


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


def get_top_transactor(all_txns):
    top_transactors = {}
    try:
        a = time.time()
        for i in all_txns:
            if i["from"] not in top_transactors.keys():
                top_transactors[i["from"]] = 1
            else:
                top_transactors[i["from"]] += 1
        top_transactors = dict(
            sorted(top_transactors.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        b = time.time()
        print("time for transactors:", b - a)
        return top_transactors
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
