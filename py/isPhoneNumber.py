# This program will print whether a string is a phnone number.
# Usually, a phone number is a form of xxx-xxx-xxxx, where x is a single number.

def isPhoneNumber(text):
    if len(text) != 12:
        return False 
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

def test2():
    print("Is 415-555-4242 a phone number?")
    print(isPhoneNumber('415-555-4242'))
    print('Mos mos a phone number?')
    print(isPhoneNumber('Mos mos'))

# Test3 can get a string of 12 characters to a chunk and test whether a chunk is a phnone number
def test3():
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i : i + 12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')

def main():
    print("hello")
    test3()

if __name__=="__main__":
    main()