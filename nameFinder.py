import re
first_names = open("namefinder/all.txt", "r").read().split("\n") # Extract data from firstname database
first_names = {x:x for x in first_names} # Make a dictionary out of the firstname database 
def get_potential_names(text):
	"""Obtain potential names from a file.
	Just finds words where both the first and second word are capitalized."""
   	names = []
   	exp = "[A-Z]\w+\s[A-Z]\w+"
        names = re.findall(exp,text)

	return names

def check_names(potential_names):
	"""Checks the potential names against a first name database."""
        d = {}
	for i in potential_names:
                first = i.split(" ")[0]
		if first in first_names:
                        if i in d.keys():
                                d[i] = d[i] + 1
                        else:
                                d[i] = 1                    
	return d

def no_dupe(name_list):
	single = []
	for i in name_list:
		if i not in single:
			single.append(i)
	return single

