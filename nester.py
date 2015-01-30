__author__ = 'nklee'


# This is my first module
def print_lol3(the_list, indent=False, level=0):

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol3(each_item, indent, level + 1)
        else:
	        if indent:
	            for num in range(level):
			        print("\t"),

		print(each_item)