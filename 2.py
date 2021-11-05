def isValid(email):
    include_at = '@' in email
    include_dot = '.' in email
    return include_at and include_dot

email = input("Please enter your e-mail: ")

if(isValid(email)):
    print("Your e-mail is valid.")
else:
    print("Your e-mail is not valid.")