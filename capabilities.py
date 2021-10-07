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


import argparse
import os
import re
import sys
import pylightxl as xl
import lib.csvutil as csvutil
import lib.stringutil as stringutil
import lib.googleapi as googleapi 

# Part to use that script as a command line tool
my_parser = argparse.ArgumentParser(description='extract data from Excel containing the Capabilities')

# Add the arguments
my_parser.add_argument('ExcelFileName',
                       metavar='excelfilename',
                       type=str,
                       help='the name of the excel file containing the capabilities')

# Execute the parse_args() method
args = my_parser.parse_args()

# Initialize program variables after the parameters
excelFileName = args.ExcelFileName

if not os.path.isfile(excelFileName):
    print('The path specified does not exist')
    sys.exit()


# Constants
RELATION_CONTAINS = 'contains'
ABB = 'ARCHITECTURALBUILDINGBLOCK:'
TYPE_ABB = 'ArchitecturalBuildingBlock'

# 
def writeABB(abb : str, outputfiles: list):
    key = ABB + stringutil.cleanName(abb, True, True, 'uppercase', False)
    nameEN = stringutil.cleanName(abb, False, False, 'noChange', False)
    name = googleapi.translate_text('fr', nameEN)
    type = TYPE_ABB
    toWrite= csvutil.initArtefact(key=key, name=name, nameEN=nameEN, type=type)
    outputfiles[1].writerow(toWrite)
  

#####################
# main
#####################

#init
db = xl.readxl(fn=excelFileName)
outputfiles = csvutil.createfiles(['ABBArtefacts.csv', 'ABBrelations.csv'])
outputfiles[1].writerow(csvutil.initArtefactHeader())
outputfiles[3].writerow(csvutil.initRelationsHeader())

#collecte des données
zones = db.ws(ws='ABB').col(col=1)
quartiers = db.ws(ws='ABB').col(col=2)
ilots = db.ws(ws='ABB').col(col=3)

# ecriture des artefacts & relations

for items in zip(zones, quartiers, ilots):
    # traitement zone
    writeABB(items[0], outputfiles)
    # traitement quartier
    writeABB(items[1], outputfiles)
    # traitement ilot
    writeABB(items[2], outputfiles)
    # traitement des relations
    for i in [0, 1]:
        parentKey = ABB + stringutil.cleanName(items[i], True, True, 'uppercase', False)
        childKey = ABB + stringutil.cleanName(items[i+1], True, True, 'uppercase', False)
        relationType = RELATION_CONTAINS
        toWrite = csvutil.initRelations(parentKey=parentKey, childKey=childKey, relationType=relationType)
        outputfiles[3].writerow(toWrite)

outputfiles[0].close()
outputfiles[2].close()