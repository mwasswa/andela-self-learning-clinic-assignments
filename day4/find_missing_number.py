def find_missing(list_one,list_two):
    if isinstance(list_one,list) and isinstance(list_two, list):
        len_list_one = len(list_one)
        len_list_two = len(list_two)
        if len_list_one == 0 and len_list_two == 0:
            return 0
        else:
            if len_list_one > len_list_two:
                return list(set(list_one) - set(list_two)).pop()
            elif len_list_two > len_list_one:
                return list(set(list_two) - set(list_one)).pop()
            else:
                if list(set(list_two) - set(list_one)) == []:
                    return 0
                elif list(set(list_two)| set(list_one)) == list_two and list(set(list_two)| set(list_one)) == list_one:
                    return 0

