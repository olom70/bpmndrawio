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

from pylightxl import readxl
from lib.csvutil import initArtefact, initArtefactHeader, initRelations, initRelationsHeader
from lib.stringutil import cleanName
from lib.googleapi import translate_text
from progress.bar import IncrementalBar


# Constants
DATA_SPHERE = 'DATASPHERE:'
BUSINESS_OBJECT = 'BUSINESSOBJECT:'
RELATION_CONTAINS = 'contains'
TYPE_DATASPHERE = 'DataSphere'
TYPE_BUSINESS_OBJECT = 'BusinessObject'


def createBusinessObjects(excelFileName: str, outputfiles: list(), totranslate=False):
    '''
        create 2 files ready to import in MAP with the Business Objets taken from an Excel File
    '''
    db = readxl(fn=excelFileName)

    outputfiles[1].writerow(initArtefactHeader())
    outputfiles[3].writerow(initRelationsHeader())

    #collecte des données
    spheresNames = db.ws(ws='Sphere').col(col=1)
    spheresDescription = db.ws(ws='Sphere').col(col=2)

    businessObjectsIDs = db.ws(ws='Business Object').col(col=1)
    businessObjectsNames = db.ws(ws='Business Object').col(col=2)
    businessObjectsDescriptions = db.ws(ws='Business Object').col(col=3)
    businessObjectsSpheres = db.ws(ws='Business Object').col(col=4)
    bar = IncrementalBar('Countdown', max=(len(spheresNames) + len(businessObjectsIDs)*2))
    # ecriture des artefacts data sphere

    for items in zip(spheresNames, spheresDescription):
        key = DATA_SPHERE + cleanName(items[0], False, True, 'uppercase', True, True, True)
        nameEN = cleanName(items[0], False, False, 'noChange', True, True, True)
        name = cleanName(translate_text('fr', nameEN), False, True, 'noChange', True, True, True) if totranslate else nameEN
        type = TYPE_DATASPHERE
        descriptionEN = cleanName(items[1],False,False, 'noChange', True, False, True)
        description = cleanName(translate_text('fr', descriptionEN), False, False, 'noChange', True, False, True) if totranslate else descriptionEN
        toWrite= initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
        outputfiles[1].writerow(toWrite)
        bar.next()

    #ecriture des Objets métiers (artefacts et relations)

    for items in zip(businessObjectsIDs, businessObjectsNames, businessObjectsDescriptions, businessObjectsSpheres):
        #artefacts
        key = BUSINESS_OBJECT + cleanName(items[1], False, True, 'uppercase', False, True, True)
        nameEN = cleanName(items[1], False, False, 'noChange', True, True, True)
        name = cleanName(translate_text('fr', nameEN), False, True, 'noChange', True, True, True) if totranslate else nameEN
        type = TYPE_BUSINESS_OBJECT
        description = cleanName(translate_text('fr', descriptionEN), False, False, 'noChange', True, False, True) if totranslate else descriptionEN
        description = descriptionEN
        toWrite= initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
        outputfiles[1].writerow(toWrite)
        bar.next()

        #relations
        parentKey = DATA_SPHERE + cleanName(items[3], False, True, 'uppercase', True, True, True)
        childKey = key
        relationType = RELATION_CONTAINS
        toWrite = initRelations(parentKey=parentKey, childKey=childKey, relationType=relationType)
        outputfiles[3].writerow(toWrite)
        bar.next()

    outputfiles[0].close()
    outputfiles[2].close()
