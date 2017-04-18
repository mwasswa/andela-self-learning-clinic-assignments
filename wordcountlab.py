def words(word):
    if isinstance(word, str):
        if len(word):
            if "\t" in word:
                words_list =word.split("\t")
            elif "\n" in word:
                words_list =word.split("\n")
            else:
                words_list = word.split(" ")

            out_dict = {}
            for _word in words_list:
                if _word.isdigit():
                    out_dict[int(_word)] = words_list.count(_word)
                else:
                    out_dict[_word] = words_list.count(_word)

            if "" in out_dict:
                del out_dict[""]
            return out_dict
