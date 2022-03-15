import re

string1 = input('Enter the text to censor the names in:')
print('=========================')
print('\n whose names do you want to censor?')
cens_element = input()

regobj = re.compile(f'{cens_element} (\w)\w* (\w)\w*', re.IGNORECASE)
final = regobj.sub('%s ' % (cens_element) + (r'\1.'.upper()
                                             ) + ' ' + (r'\2.'.upper()), string1)
print('\n')
print('='*len(cens_element))
print('\n')
print(final)
