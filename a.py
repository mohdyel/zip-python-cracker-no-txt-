import zipfile
import itertools
def openZip(file, password=''):
    zip = zipfile.ZipFile(file)
    try:
        if password == '':
            zip.extractall()
        else:
            zip.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except Exception as e:
        return False
#zip file
file = 'File.zip'
def foo(l):
     yield from itertools.product(*([l] * 6)) #here you put how many characters are in the password (i put 6 here)
x = 0
# number or chars you want to add
for x in foo('1234567890'):
    word = (''.join(x))
    result = openZip(file, word)
    if result:
        print('the correct password is',word)
        break
    else:
         print('incorrect:',word) #you can also remove print statement
     



