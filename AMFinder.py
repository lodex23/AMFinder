import os


os.system('clear')


print("----------------------------------------------------------------")
print("|  Welcome to AdminFinder an automated nikto tool by Jeffrey   |")
print("----------------------------------------------------------------")

url = input("Enter Host/url: ")

os.system('clear')


print("----------------------------------------------------------------")
print("|  Welcome to AdminFinder an automated nikto tool by Jeffrey   |")
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")
print("|  Set host to: " + url)
print("----------------------------------------------------------------")

input("Press enter to start scanning: " + url)


os.system('clear')

os.system('nikto -host ' + url)
