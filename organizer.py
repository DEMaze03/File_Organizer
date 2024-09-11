import os
import shutil

homeDir = os.path.expanduser('~')

downloadsDir = os.path.join(homeDir,"Downloads")
documentsDir = os.path.join(homeDir,"Documents")
photosDir = os.path.join(homeDir,"Photos")
videosDir = os.path.join(homeDir,"Videos")

targetDirs = [downloadsDir,documentsDir,photosDir,videosDir]

def organize_files(path):
    if not os.path.exists(path):
        return
    
    files = []
    for name in os.listdir(path):
        if not name.startswith('.'):
            files.append(name)


    for file in files:
        fileName,extension = os.path.splitext(file)
        extension = extension[1:]
        
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    
for dir in targetDirs:
    organize_files(dir)