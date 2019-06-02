spam = ['apples', 'bananas', 'tofu', 'orange']

def list_to_string(spam):
    text = ""
    for i in range(len(spam)):
       spa = spam[i];
       if(i > 0):
           if(i == len(spam) - 1):
               text += " and " + spa
           else:
               text += " , " + spa
       else:
                text += spa
    return text
print(list_to_string(spam))
