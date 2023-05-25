password = input("Enter your password: ")
confirm_password = input('Confirm your password: ')

if password == confirm_password:
    print('Password verified')
while password != confirm_password:
  print('Wrong password')
  confirm_password = input('Please put in a correct password: ')
if password == confirm_password:
  print('Password verified')
  