#Reverse the string except the special characters (@,#)
import re

str = input('Enter the string to be reversed:')
string_list = re.findall('[a-zA-Z]', str)
string_list.reverse()

for i in range(len(str)):
    if str[i] == '#' or str[i] == '@':
        string_list.insert(i, str[i])
print(''.join(string_list))
