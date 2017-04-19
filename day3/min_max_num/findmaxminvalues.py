def find_max_min(mylist):
    if(isinstance(mylist,list)):
        is_valid_list = False
        for item in mylist:
            if isinstance(item,int) or isinstance(item,float):
                is_valid_list = True

        if is_valid_list:
            min_value = min(mylist)
            max_value = max(mylist)
            if min_value == max_value:
                return [mylist.count(min_value)]
            else:
                return [min_value,max_value]
