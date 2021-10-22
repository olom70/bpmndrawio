import re

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanName(value: str, trimSpace=False, removeDiacritic=False, changeCase=['uppercase', 'lowercase', 'noChange'], removeCR=False, removeSpecialCharacters=False, removeHTMLTags=False):
    '''
        remove specials characters, html elements.
        also remove spaces and diacritics if asked to do
    '''
    def rd(v, toRemove=['diacritics', 'specialCharacters']):
        diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
        specialCharacters = {'%': ' ', '"': ' ', "<": ' ', ">": ' ', "&": '', "\\": ' ', "/": ' ', "'": ' '}
        if (toRemove == 'diacritics'): charactersToRemove = diacritics
        if (toRemove == 'specialCharacters'): charactersToRemove = specialCharacters 
        cleanstr = ''
        for i, char in enumerate(v):
            if char in charactersToRemove:
                cleanstr = cleanstr + charactersToRemove[char] 
            else:
                cleanstr = cleanstr + v[i] 
        return cleanstr

    if trimSpace: c = value.replace(" ", "")
    if removeHTMLTags: c = re.sub(cleanr,'', value)
    if removeDiacritic: c = rd(c, 'diacritics')    
    if removeSpecialCharacters: c=rd(c, 'specialCharacters')
    if changeCase == 'uppercase': c = c.upper()
    if changeCase == 'lowercase': c = c.lower()
    if removeCR: 
        c = c.replace("\n", "")
        c = c.replace("\r", "")
    if len(c) == 0: c = 'NoName'
    return c

def getNameLastPart(fullName : str, separator=' ', trimSpace=False ):
    '''
        If a string is made up several parts separated by a character(s), this function get the last part to the right
    '''
    if trimSpace:
        return fullName[fullName.rfind(separator)+1:-(len(fullName)-(fullName.find('.')))].replace(" ", "") 
    else:
        return fullName[fullName.rfind(separator)+1:-(len(fullName)-(fullName.find('.')))] 
