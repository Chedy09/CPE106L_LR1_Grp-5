#Prompt the user for a file name
inputFileName = input('Input desired file name: ')

#Open reading file
fin = open(inputFileName, "r")

#Create empty list
fileList = list()

#Program enters a loop read state
for line in fin:
    #A new line is stripped
    line = line.strip('\n')
    #Line read is added into list
    fileList.append(line)

cont = True
while cont:
    #Print the total number of lines
    print('The specified file contains',len(fileList),'lines.')
    #Prompt the user for a specific line number
    stop = int(input('Enter a line number [0 to quit]: '))
    if stop == 0:
        cont = False
    else:
        #Print the user's input of line value
        print(str(stop)+': '+fileList[stop-1]+'\n')

#Close
fin.close()
