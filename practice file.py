country = input("Enter the name of the country: ")
country = country.strip()
while True:
    match country:
        case 'India':
            print('Namaste')
            break
        case 'USA' :
            print('Hello')
            break
        case 'Germany' :
            print('Hallo')
            break
        case '-':
            print("Wrong input")
            break
print('exit')