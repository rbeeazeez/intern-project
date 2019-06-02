# A programme to check for a phone number:Sample 0802_770_1346
def is_phone_number(text):
    if len (text) != 13:
      return False
    for i in range(0, 4):
        if not text[i].isdecimal():
            return False
    if text[4] != '_':
        return False
    for i in range(5, 8):
        if not text[i].isdecimal():
            return False
    if text[8] != '_':
        return False
    for i in range(9, 13):
        if not text[i].isdecimal():
            return False
    return True


print('0812_989_3100 is a phone number: ')
print(is_phone_number('0812_989_3100'))

message = 'My phone number is 0812_989_3100, my father has two contacts 0708_648_6369.'
for i in range (len(message)):
    check = message[i:i+13]
    if is_phone_number(check):
        print('Phone number found: ' + check)
print('Done')

