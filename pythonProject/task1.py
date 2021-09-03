keys=[1,2,3,4]
values=['a','b', 'c']


def make_dictionary(keys,values):
    dictionary = {}
    for i in range(0, len(keys)):
        if ( i < len(values) ):
            dictionary[keys[i]] = values[i]
        else:
            dictionary[keys[i]] = 'None'
    return dictionary


print(make_dictionary(keys, values))
