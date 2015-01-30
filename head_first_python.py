__author__ = 'nklee'

data_list = ['a', 'b', ['a_1', 'a_2']]
for item in data_list:
    if isinstance(item, list):
        for sub_item in item:
            print "inner loop : " + sub_item
    else:
        print "outer loop : " + item


print("==============================")
import nester
nester.print_lol3(data_list, True, 2)