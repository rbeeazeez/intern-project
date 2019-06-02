while True:
    print('Who are you?')
    name = input()
    if name != 'Robiat':
        continue
    print('Hello, Robiat. What is the password? (It is a fish.)')
    password = input()
    if password == 'Swordfish':
        break
    print('Access Granted')
