import glob
import os

path = r'P:\Mapping\Addressing\Work Area\To Be Addressed\0_To Be Mailed'
path1 = r'P:\Mapping\Addressing\Work Area\To Be Addressed\0_To Be Mailed\Oct 2018 through Nov 2019'
fileName = 'Names_of_Files'
type_of_file = '.txt'
fullName = path + '\\' + fileName + type_of_file
print fullName

file = open(fullName, 'w')

list = os.listdir(path1)

print list

for item in list:
    file = open(fullName, 'a')
    def listToString(string):
        string1 = " "
        for element in string:
            string1 += element
        return string1

    string = item

    print(listToString(string))
    file.write(listToString(string +'\n'))
    file.close()


