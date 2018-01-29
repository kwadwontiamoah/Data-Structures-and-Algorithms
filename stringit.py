def folding(ID):
    hashes = []
    while len(ID) > 0:
        val = 0
        for item in ID:
            while len(item) > 1:
                str_1 = str(item[0])
                str_2 = str(item[1])
                str_concat = str_1 + str_2
                bifold = int(str_concat)
                val = val + bifold
                item.pop(0)
                item.pop(0)
            else:
                if len(item) > 0:
                    val = val + int(item[0])
                else:
                    pass
            hashes.append(hash_val)
        return hashes
