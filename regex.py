import re
# returns digits only
phoneNumberRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('His contact is 0805-161-8695')
print('Sofwan contact: ' + mo.group())


meRegex = re.compile(r' (Ro)+biat')
mo = meRegex.search('My name is Robiat')
print(mo.group())


# returns first matching object
nameRegex = re.compile(r'Robiat|Azeez')
mo1 = nameRegex.search('My name is Robiat Azeez.')
print(mo1.group())
mo2 = nameRegex.search('My name is Azeez Robiat.')
print(mo2.group())


