# Capabilities for MAP
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
RELATION_CONTAINS = 'contains'
ABB = 'ARCHITECTURALBUILDINGBLOCK:'
TYPE_ABB = 'ArchitecturalBuildingBlock'

# 
def writeABB(abb : str, outputfiles: list, l_alreadyAdded, totranslate=False):
    
    if abb not in l_alreadyAdded[0]:
        l_alreadyAdded[0].append(abb)
        key = ABB + cleanName(abb, False, True, 'uppercase', False, True, True)
        nameEN = cleanName(abb, False, False, 'noChange', False, True, True)
        name = cleanName(translate_text('fr', nameEN), False, False, 'noChange', True, False, True) if totranslate else nameEN
        type = TYPE_ABB
        toWrite= initArtefact(key=key, name=name, nameEN=nameEN, type=type)
        outputfiles[1].writerow(toWrite)

def createCapabilities(excelFileName: str, outputfiles: list(), totranslate):
    '''
        create 2 files ready to import in MAP with the capabilities taken from an Excel File
    '''
    db = readxl(fn=excelFileName)
    outputfiles[1].writerow(initArtefactHeader())
    outputfiles[3].writerow(initRelationsHeader())

    #collecte des données
    zones = db.ws(ws='ABB').col(col=1)
    quartiers = db.ws(ws='ABB').col(col=2)
    ilots = db.ws(ws='ABB').col(col=3)
    bar = IncrementalBar('Countdown', max=len(zones)*5)
    # ecriture des artefacts & relations
    alreadyAdded = []
    l_alreadyAdded = [alreadyAdded]
    for items in zip(zones, quartiers, ilots):
        # traitement zone
        writeABB(items[0], outputfiles, l_alreadyAdded, totranslate)
        bar.next()
        # traitement quartier
        writeABB(items[1], outputfiles, l_alreadyAdded, totranslate)
        bar.next()
        # traitement ilot
        writeABB(items[2], outputfiles, l_alreadyAdded, totranslate)
        bar.next()
        # traitement des relations
        for i in [0, 1]:
            parentKey = ABB + cleanName(items[i], False, True, 'uppercase', False, True, True)
            childKey = ABB + cleanName(items[i+1], False, True, 'uppercase', False, True, True)
            relationType = RELATION_CONTAINS
            toWrite = initRelations(parentKey=parentKey, childKey=childKey, relationType=relationType)
            outputfiles[3].writerow(toWrite)
            bar.next()
    outputfiles[0].close()
    outputfiles[2].close()
