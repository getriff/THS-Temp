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


# Prompt: write a python script that can extract source code of a particular
# named function from a solidity source file. also handle if multiple functions
# of same name exists
def extract_function(data, function_name):
    ret_dict = {}
    start_index = 0
    counter = 0
    while True:
        start_index = data.find(f"function {function_name}(", start_index)
        print(start_index)
        if start_index == -1:
            break

        # Find the opening and closing braces of the function
        brace_count = 0
        for i, char in enumerate(data[start_index:]):
            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0:
                    end_index = start_index + i + 1
                    break

        # Extract the source code of the function
        counter += 1
        function_code = data[start_index : end_index + 1]

        ret_dict[counter] = function_code

        start_index = end_index
        data = data[start_index:]

    return ret_dict[list(ret_dict.keys())[-1]]


pref = ' """ \n // Below given is a code in solidity language: a curly bracketed language similar to cplusplus \n'

suff = ' """ \n\n Q. Explain this function in simple language for end user to understand and elaborate on it? \n \n A. [insert]'


# write a python script that can combine the above extracted code with a special from above and below it
def compile_prompt(data, prefix=pref, suffix=suff):
    prompt = prefix
    prompt += data
    prompt += suffix
    return prompt
