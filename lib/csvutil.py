# useful functions written while manipulating files
import csv

def createfiles(l):
    '''
        create the files for MAP import
        input : a list of filename to create
        output : for each input file : a file named after the input, and a csv.writer to put content in it
    '''
    r = []
    for v in l:
        csvfile = open(v, 'w+', newline='', encoding="utf-8")
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        r += [csvfile, writer]
    return r


def initArtefact(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the artefacts to import in MAP
    '''
    key = ''
    name = ''
    nameEN = ''
    type = ''
    businessID = ''
    ordernumber = ''
    description = ''
    descriptionEN = ''
    serviceLevelAgreement = ''
    frequency = ''
    activityType = ''
    periodicity = ''
    platform = ''
    contractScope = ''

    for k, v in kwargs.items():
        if k == 'key': key = v
        if k == 'name' : name = v
        if k == 'type' : type = v
        if k == 'nameEN' : nameEN = v
        if k == 'businessID' : businessID = v
        if k == 'ordernumber' : ordernumber = v
        if k == 'description' : description = v
        if k == 'descriptionEN' : descriptionEN = v
        if k == 'serviceLevelAgreement' : serviceLevelAgreement = v
        if k == 'contractScope' : contractScope = v
        if k == 'frequency' : frequency = v
        if k == 'activityType' : activityType = v
        if k == 'periodicity' : periodicity = v
        if k == 'platform' : platform = v

    return [key, name, type,  nameEN, businessID, ordernumber, description, descriptionEN, serviceLevelAgreement, contractScope, frequency, activityType, periodicity, platform]

def initArtefactHeader():
    '''
        Initialise the first row of the artefact file : the header
    '''
    return initArtefact(key='key', name='name', type='type',  nameEN='nameEN', businessID='businessID', ordernumber='ordernumber', description='description', descriptionEN='descriptionEN', serviceLevelAgreement='serviceLevelAgreement', contractScope='contractScope', frequency='frequency', activityType='activityType', periodicity='periodicity', platform='platform')

def initRelations(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the relations to import in MAP
    '''
    parentKey = ''
    childKey = ''
    relationType = ''
    metaX = ''
    for k, v in kwargs.items():
        if k == 'parentKey': parentKey = v
        if k == 'childKey': childKey = v
        if k == 'relationType': relationType = v
        if k == 'metaX': metaX = v
    return [parentKey, childKey, relationType, metaX]

def initRelationsHeader():
    '''
        Initialise the first row of the relation file : the header
    '''
    return initRelations(parentKey='parentKey', childKey='childKey', relationType='relationType', metaX='metaX')
