def flatten():
    if isinstance(llst, list):
        temp = []
        for _ in llst:
            temp.extend(flatten())
        return temp
    else:
        return [llst]


llst = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

lst_l = flatten()

print("The List after flattening : " + str(lst_l))
