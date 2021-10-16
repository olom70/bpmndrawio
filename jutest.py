   
# %%
tel = {'jack': '', 'sape': 4139}
if ('value' in tel):
    print(tel['value'])
if ('jack' in tel):
    print('0') if len(tel['jack']) == 0 else print(1)
tel['sape']
'value' in tel


# %%
import csv
artefactscolumns = ["key", "name", "type", "businessID", "orderNumber", "description", "serviceLevelAgreement", "frequency", "activityType", "periodicity", "platform", "contractScope"]
relationscolums = ["parentKey" ,"childKey","relationType", "metaX"]
with open('artefacts.csv', 'w+', newline='') as artefactscsvfile:
    artefactswriter = csv.writer(artefactscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    artefactswriter.writerow(artefactscolumns)


  # %%
def addt(a):
  a = a + 2
  return a

a = 1
addt(a)
print(a)


# %%
# initialise the file that will contains all the artefacts (processes & applications)
artefactscolumns = ["key", "name", "type", "businessID", "orderNumber", "description", "serviceLevelAgreement", "frequency", "activityType", "periodicity", "platform", "contractScope"]
with open('artefacts.csv', 'w+', newline='') as artefactscsvfile:
    artefactswriter = csv.writer(artefactscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

# initialise the file that will contains all the relations (processes & applications)
relationscolumns = ["parentKey" ,"childKey","relationType", "metaX"]
with open('relations.csv', 'w+', newline='') as relationscsvfile:
    relationswriter = csv.writer(relationscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

def writecsv():
    artefactswriter.writerow(artefactscolumns)
    relationswriter.writerow(relationscolumns)

writecsv()
# %%
file = 'Vendre - Ventes Wholesales & Partenaires BPMN Commande web DW avec OMS (1)-process commande web sous Demandware.drawio.xml'
filename = file[file.rfind('-')+1:-(len(file)-(file.find('.')))]
print(filename)
# %%
v = 'a'
listt = ['a', 'b', 'c']
'd' in listt
# %%
not ('aa' == 'bb')
# %%
var = [0, 1]
varb = var

varb[0] = 2
print(var)
# %%
import csv
def createfile(l):
  r = []
  for v in l:
    csvfile = open(v, 'w+', newline='')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    r += [csvfile, writer]
  return r

w = createfile(['names3.csv', 'names4.csv'])
print(w)
w[1].writeheader()
w[1].writerow({'first_name': 'Baked', 'last_name': 'Beans'})
w[1].writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
w[1].writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
w[3].writeheader()
w[3].writerow({'first_name': 'Baked', 'last_name': 'Beans'})
w[3].writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
w[3].writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
w[0].close()
w[2].close()
# %%
a = []
a = a + [1, 0]
a = a + [2, 3]
print(a)
# %%
import pylightxl as xl
db = xl.readxl(fn='C:/work/EDL.xlsx')
db.ws_names
spheresNames = db.ws(ws='Sphere').col(col=1)
spheresDescription = db.ws(ws='Sphere').col(col=2)
for items in zip(spheresNames, spheresDescription):
  print('name : {name}, desc : {desc}'.format(name=items[0], desc=items[1]))

# %%
import re
cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanName(value: str, trimSpace=False, removeDiacritic=False, changeCase=['uppercase', 'lowercase', 'noChange']):
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
    if len(c) == 0: c = 'NoName'
    return c


v = 'é a bonjour è '
print(cleanName(v, True,True, 'lowercase'))

# %%
v = 'é a bonjour è '
diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
cleanstr = ''
for i, char in enumerate(v):
    if char in diacritics:
      cleanstr = cleanstr + diacritics[char] 
    else:
      cleanstr = cleanstr + v[i] 
print(cleanstr)

# %%
diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
'à' in diacritics
# %%
PROJECT_ID = 'storied-chariot-328315'
GOOGLE_APPLICATION_CREDENTIALS="~olom/.local/share/gcp/storied-chariot-328315-f1183300239e.json"
def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

translate_text('fr', 'hello')
# %%
import lib.stringutil as stringutil
v=''' dfdf\n fdf\nf
'''
c = stringutil.cleanName(v, False, False, 'noChange', True)
print(c)
# %%
import lib.stringutil as stringutil
v=''' dfdf\n fdf\nf
'''
print(v.replace("\n", ''))
# %%
