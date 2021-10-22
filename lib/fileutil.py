import glob
import os

def getfiles(input_path, extension):
    '''
        parse all the files of the specified dir that have the specified extension
        for each file, place its name in a dictionary with an empty dictionary for the value
                       (that will get the details later )
        dicOfFiles = {filename : {emptyDictionary}}
    '''
    listOfFiles = []

    for file in (glob.glob(input_path + "*." + extension,recursive=False)):
        listOfFiles.append(file)
    return listOfFiles

def fileExist(fullpath: str, typeExtraction: str, dir=['dir', 'file']) -> list():
    '''
       Check if the specified path exist.
       If so : return head, tail from os.path.split()
       If not : raise an exception
    '''
    if (dir=='file'):
        if not os.path.isfile(fullpath):
            print('arg {v} : The specified file does not exist'.format(v=typeExtraction))
            raise Exception()
    else:
        if not os.path.isdir(fullpath):
            print('arg {v} : The specified path does not exist'.format(v=typeExtraction))
            raise Exception()

    head, tail = os.path.split(fullpath)
    return [head, tail]
