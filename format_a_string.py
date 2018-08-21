# # Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas 
# except for the last two names, which should be separated by an 
# ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

namelist{'name': 'Bart'}, {"name': 'Lisa',
jj
""" """ """ """ """  """ """ """ """ """
 } 

# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''


def namelist(array):
    li = [v['name'] for v in array]
    return ', '.join(li[:-1]) + ' & ' + li[-1] if len(li) >= 2 else (li[0] if li else '')


print(namelist([]))