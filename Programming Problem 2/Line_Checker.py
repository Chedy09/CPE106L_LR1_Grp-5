inputFileName = input('Input the file name here: ')

fin = open(inputFileName, "r")

fileList = list()

for line in fin:
    line = line.strip('\n')
    fileList.append(line)

cont = True
while cont:
    print('The file has',len(fileList),'lines.')
    stop = int(input('Enter a line number [0 to quit]: '))
    if stop == 0:
        cont = False
    else:
        print(str(stop)+': '+fileList[stop-1]+'\n')

fin.close()