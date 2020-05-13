import os, shutil, zipfile

sortingDir = r'C:\Users\shubh\Downloads' # directory that is to be sorted
destinationDir = r'C:\Users\shubh\Downloads' #directory where the sorted files are to be saved

print('Do you also want to compress all the sorted files? (y/n) ')
compress = input()

fileTypes = {'.pdf' : 'PDF','.pptx':'Docs','.docx':'Docs','.txt':'Docs','.jpg':'Pictures','.jpeg':'Pictures','.png':'Pictures','.exe':'Executables',
'.msi':'Executables','.xlsx':'Docs','.avi':'Videos','mkv':'Videos','.mp4':'Videos',
'.zip':'Compressed','.7z':'Compressed','.rar':'Compressed','.srt':'Subtitles'} #modify this as you please

def moveFile(fileName, extension): #moves the files to their corresponding folders
    shutil.move(sortingDir + '\\' + fileName, destinationDir + '\\' + fileTypes[extension])
           

def compressFile(): #for making a compressed zip file constituting every file in its respective folder
    uniqueFolders = set(fileTypes.values())
    for folder in uniqueFolders:
        currentDir = destinationDir + '\\' + folder
        os.chdir(currentDir)
        filesInDirectory = os.listdir()
        if len(filesInDirectory) != 0:  # if the directory is empty, no zip file is created
            newZipFile = zipfile.ZipFile(folder + '.zip','a')
            for file in filesInDirectory:
                if not file == folder + '.zip': #making sure the previous zipped folder itself isnt zipped
                    newZipFile.write(file)
                    print('Deleting file.. ' + file)
                    # os.unlink(file)           #deletes the original file after zipping it
            newZipFile.close()

        


for folder in fileTypes.values(): #creates the directories in which the sorted files will be moved
    if not os.path.exists(destinationDir + '\\' + folder):
        os.mkdir(destinationDir + '\\' + folder)   


filesInDir = os.listdir(sortingDir)   
for fileName in filesInDir:  #iterating through every file in the directory being sorted
    for extension in fileTypes.keys():
        if fileName.endswith(extension) :
            moveFile(fileName, extension)

if compress is True or 'y' or 'Y' :
    compressFile()












