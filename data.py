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
import lib.googleapi as googleapi
from progress.bar import IncrementalBar

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
DATA_SPHERE = 'DATASPHERE:'
BUSINESS_OBJECT = 'BUSINESSOBJECT:'
RELATION_CONTAINS = 'contains'
TYPE_DATASPHERE = 'DataSphere'
TYPE_BUSINESS_OBJECT = 'BusinessObject'


#####################
# main
#####################

#init
head, tail = os.path.split(excelFileName)
if not os.path.isdir(head):
    print('The specified path {head} does not exist'.format(head))
    sys.exit()

csvartefactsfile = head + os.path.sep + 'BOArtefacts_' + str(time.time()) + '.csv'
csvrelationsfile = head + os.path.sep + 'BOrelations_' + str(time.time()) + '.csv'


db = xl.readxl(fn=excelFileName)
outputfiles = csvutil.createfiles([csvartefactsfile, csvrelationsfile])
outputfiles[1].writerow(csvutil.initArtefactHeader())
outputfiles[3].writerow(csvutil.initRelationsHeader())

#collecte des donn??es
spheresNames = db.ws(ws='Sphere').col(col=1)
spheresDescription = db.ws(ws='Sphere').col(col=2)

businessObjectsIDs = db.ws(ws='Business Object').col(col=1)
businessObjectsNames = db.ws(ws='Business Object').col(col=2)
businessObjectsDescriptions = db.ws(ws='Business Object').col(col=3)
businessObjectsSpheres = db.ws(ws='Business Object').col(col=4)
bar = IncrementalBar('Countdown', max=(len(spheresNames) + len(businessObjectsIDs)*2))
# ecriture des artefacts data sphere

for items in zip(spheresNames, spheresDescription):
    key = DATA_SPHERE + stringutil.cleanName(items[0], False, True, 'uppercase', True, True, True)
    nameEN = stringutil.cleanName(items[0], False, False, 'noChange', True, True, True)
    name = stringutil.cleanName(googleapi.translate_text('fr', nameEN), False, True, 'noChange', True, True, True)
    type = TYPE_DATASPHERE
    descriptionEN = stringutil.cleanName(items[1],False,False, 'noChange', True, False, True)
    description = stringutil.cleanName(googleapi.translate_text('fr', descriptionEN), False, False, 'noChange', True, False, True)
    toWrite= csvutil.initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
    outputfiles[1].writerow(toWrite)
    bar.next()

#ecriture des Objets m??tiers (artefacts et relations)

for items in zip(businessObjectsIDs, businessObjectsNames, businessObjectsDescriptions, businessObjectsSpheres):
    #artefacts
    key = BUSINESS_OBJECT + stringutil.cleanName(items[1], False, True, 'uppercase', False, True, True)
    nameEN = stringutil.cleanName(items[1], False, False, 'noChange', True, True, True)
    name = stringutil.cleanName(googleapi.translate_text('fr', nameEN), False, True, 'noChange', True, True, True)
    type = TYPE_BUSINESS_OBJECT
    descriptionEN = stringutil.cleanName(items[2],False,False, 'noChange', True, False, True)
    description = stringutil.cleanName(googleapi.translate_text('fr', descriptionEN), False, False, 'noChange', True, False, True)
    toWrite= csvutil.initArtefact(key=key, name=name, nameEN=nameEN, type=type, description=description, descriptionEN=descriptionEN)
    outputfiles[1].writerow(toWrite)
    bar.next()

    #relations
    parentKey = DATA_SPHERE + stringutil.cleanName(items[3], False, True, 'uppercase', True, True, True)
    childKey = key
    relationType = RELATION_CONTAINS
    toWrite = csvutil.initRelations(parentKey=parentKey, childKey=childKey, relationType=relationType)
    outputfiles[3].writerow(toWrite)
    bar.next()

outputfiles[0].close()
outputfiles[2].close()
