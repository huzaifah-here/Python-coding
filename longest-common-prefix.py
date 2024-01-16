def longestCommonPrefix(strs):
    check_prefix = ""
    if strs:
        first_element = strs.pop(0)

        first_character = first_element[0]
    index = 0
    for element in strs:
        index = index + 1
        if element[index] == element[index + 1]:
            check_prefix = element[0]
        else:
            return ""
    return check_prefix
    # if check_prefix =="":
    #     check_prefix = element[0]
    # else:
    #     check_prefix = check_prefix + element[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))
