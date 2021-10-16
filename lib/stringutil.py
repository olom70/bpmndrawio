import re

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanName(value: str, trimSpace=False, removeDiacritic=False, changeCase=['uppercase', 'lowercase', 'noChange'], removeCR=False):
    '''
        remove specials characters, html elements.
        also remove spaces and diacritics if asked to do
    '''
    diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
    def rd(v):
        cleanstr = ''
        for i, char in enumerate(v):
            if char in diacritics:
                cleanstr = cleanstr + diacritics[char] 
            else:
                cleanstr = cleanstr + v[i] 
        return cleanstr

    if trimSpace: c = re.sub(cleanr,'', value).replace(" ", "")
    if not trimSpace: c = re.sub(cleanr,'', value)
    if removeDiacritic: c = rd(c)    
    if changeCase == 'uppercase': c = c.upper()
    if changeCase == 'lowercase': c = c.lower()
    if removeCR: 
        c = c.replace("\n", "")
        c = c.replace("\r", "")
    if len(c) == 0: c = 'NoName'
    return c

def getNameLastPart(fullName : str, separator=None, trimSpace=False ):
    '''
        get just the name of the file without the path nor the extension and spaces and after a specified character
    '''
    #trimmedFilename = file[file.rfind(os.path.sep)+1:-(len(file)-(file.rfind('.')))].replace(" ", "")
    if (separator is None):
        return fullName[fullName.rfind('-')+1:-(len(fullName)-(fullName.find('.')))].replace(" ", "") 
