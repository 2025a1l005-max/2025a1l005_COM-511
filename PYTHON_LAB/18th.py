name =  input()
date = input()
letter = '''
Dear <Name>,
You are selected!
<Date>
'''
letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)
print(letter)
