# Business Objects : extract Business Objects form an excel file and write a CSV that is readable by MAP
# 2 files : 
# - Artefacts creation
# - Relations between the artefacts
#
# Output Formats : 
#                  Artefacts creation
# - CSV file
# - columns
#       key	name	type	nameEN	businessID	orderNumber	description	descriptionEN
#
#                    Relation between the artefacts
# - CSV file
# - columns


import argparse
import os
import re
import sys
import pylightxl as xl
import lib.csvutil as csvutil
import lib.stringutil as stringutil

# Part to use that script as a command line tool
my_parser = argparse.ArgumentParser(description='extract data from EDM Excel File')

# Add the arguments
my_parser.add_argument('ExcelFileName',
                       metavar='excelfilename',
                       type=str,
                       help='the name of the excel file containing the business objects')

# Execute the parse_args() method
args = my_parser.parse_args()

# Initialize program variables after the parameters
excelFileName = args.ExcelFileName

if not os.path.isfile(excelFileName):
    print('The path specified does not exist')
    sys.exit()


# Constants
DATA_SPHERE = 'DATA_SPHERE:'
BUSINESS_OBJECT = 'BUSINESS_OBJECT:'
RELATION_CONTAINS = 'contains'
TYPE_DATASPHERE = 'DataSphere'
TYPE_BUSINESS_OBJECT = 'BusinessObject'
RELATION_CONTAINS = 'contains'
# 

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
    return translate_client.translate(text, target_language=target)['translatedText']

    

#####################
# main
#####################

#init
db = xl.readxl(fn=excelFileName)
outputfiles = csvutil.createfiles(['BOArtefacts.csv', 'BOrelations.csv'])
outputfiles[1].writerow(csvutil.initArtefactHeader())
outputfiles[3].writerow(csvutil.initRelationsHeader())

#collecte des données
spheresNames = db.ws(ws='Sphere').col(col=1)
spheresDescription = db.ws(ws='Sphere').col(col=2)

businessObjectsIDs = db.ws(ws='Business Object').col(col=1)
businessObjectsNames = db.ws(ws='Business Object').col(col=2)
businessObjectsDescriptions = db.ws(ws='Business Object').col(col=3)
businessObjectsSpheres = db.ws(ws='Business Object').col(col=4)

# ecriture des artefacts data sphere

for items in zip(spheresNames, spheresDescription):
    key = DATA_SPHERE + stringutil.cleanName(items[0], True, True, 'uppercase')
    name = stringutil.cleanName(items[0], False, False, 'noChange')
    nameEN = name
    type = TYPE_DATASPHERE
    description = translate_text('fr', stringutil.cleanName(items[1],False,False, 'noChange', True))
    descriptionEN = stringutil.cleanName(items[1],False,False, 'noChange', True)
    toWrite= csvutil.initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
    outputfiles[1].writerow(toWrite)

#ecriture des Objets métiers (artefacts et relations)

for items in zip(businessObjectsIDs, businessObjectsNames, businessObjectsDescriptions, businessObjectsSpheres):
    #artefacts
    key = BUSINESS_OBJECT + stringutil.cleanName(items[1], True, True, 'uppercase')
    name = stringutil.cleanName(items[1], False, False, 'noChange')
    nameEN = name
    type = TYPE_BUSINESS_OBJECT
    description = translate_text('fr', stringutil.cleanName(items[2], False, False, 'noChange', True))
    descriptionEN = stringutil.cleanName(items[2],False,False, 'noChange', True)
    toWrite= csvutil.initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
    outputfiles[1].writerow(toWrite)

    #relations
    parentKey = DATA_SPHERE + stringutil.cleanName(items[3], True, True, 'uppercase')
    childKey = key
    relationType = RELATION_CONTAINS
    toWrite = csvutil.initRelations(parentKey=parentKey, childKey=childKey, relationType=relationType)
    outputfiles[3].writerow(toWrite)

outputfiles[0].close()
outputfiles[2].close()
