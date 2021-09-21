# analyse drawio files with BPMN content

'''

10) Open  all the files of a directory
    for each file name ; catch filename

15) catch value of <diagram> ---> non plus necessaire

20) catch all interesting attributes of mxCell :
    - id, value, id_of_parent, style, source, target

30) put all this in a dictionary :
    {id : [inferedtype, genereatedIdforMap, value, id_of_parent, style, source, target]}} 

inferedtype :
       swimlane : {id : [style, value, id_of_parent]} --> style=swimlane
       activity : {id : [style, value, id_of_parent]} --> style=shape=ext or style=html=1
       bpmnartifact : {id : [style, value, id_of_parent]}
       edge : {id : [style, value, id_of_parent, source, destination]} -->  as a source and a target
       note : {id : [style, value, id_of_parent]} --> style=note
       process : {id : [style, value, id_of_parent]}--> style=shape=process
       group : {id : [style, value, id_of_parent]}--> style=group

40) first task of the restitution : generate 2 CSV ready to import into MAP
- link swimlanes and activities

some particularities :
- take into account only swimlanes beginning wtih "Processus"
- do not take into account parent id of swimlanes "Processus"
- if a swimlane "not Processus" has its parent with a name not beginning by processus take the last part of the name of the file
-   example : 13 - BPMN Nextail - WEB - V2-Processus Allocation de stock - Réassort Nextail Web - Génération des fichiers quotidiens.drawio.xml
-           13 - BPMN Nextail - WEB-Processus Allocation de stock - Réassort Nextail - Intégration des Waybills.drawio.xml
- do not take into account swimlanes with no value

goal : 

first CSV : artefacts
------------
csv fields : key;name;type;businessID;orderNumber;description;serviceLevelAgreement;frequency;activityType;periodicity;platform;contractScope

case of processes :
key;name;type;
MACRO_BUSINESS_PROCESS:{filename}{id};value;MacroBusinessProcess;

case of applications :
key;name;type;
APPLICATION:{value};value;Application 


second csv : links
--------------------
parentKey;childKey;relationType;metaX

APPLICATION:{id};MACRO_BUSINESS_PROCESS:{id};serves

50) generate a graphml that show the hierarchy of the content

first pass : create all the nodes
second pass : create the hierarchy between the artefacts. if the Cell has no parents : attach to the name of the file
                which is the top of the hierarchy
                --> hierarchy made by linking nodes with edges (labels "contains")
thrid pass : create link between activities by creating edges  (labels "is before")


'''
import os
import sys
import glob
import argparse
import re
import xml.etree.ElementTree as ET
import pyyed
import filecmp
import csv
import uuid
# Create the parser
my_parser = argparse.ArgumentParser(description='analyse drawio files with BPMN content')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

my_parser.add_argument('FilesExt',
                       metavar='ext',
                       type=str,
                       help='the extensions of files to analyse')

# Execute the parse_args() method
args = my_parser.parse_args()

# Initialize program variables after the parameters
extension = args.FilesExt
input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()


####### Global SCope Variables ##############
listOfFiles = []
dictOfFilesAndDetails = {}
MACROBUSINESSPROCESS = 'MACRO_BUSINESS_PROCESS:'
APPLICATION = 'APPLICATION:'
MACROBUSINESSPROCESSTYPE  = 'MacroBusinessProcess'
APPLICATIONTYPE = 'Application'
RELATION_SERVE = 'serves'


#################### Functions ##################
def getProcessName(fullName):
    '''
        get just the name of the file without the path nor the extension and spaces
    '''
    #trimmedFilename = file[file.rfind(os.path.sep)+1:-(len(file)-(file.rfind('.')))].replace(" ", "")
    return fullName[fullName.rfind('-')+1:-(len(fullName)-(fullName.find('.')))].replace(" ", "") 


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

def parentIsaProcess(myfile, parentID):
    for file, dictWithDetails in dictOfFilesAndDetails.items():
        for id, listOfDetails in dictWithDetails.items():
            (inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target) = listOfDetails
            if (myfile == file and parentID == id):
                if cleanvalue is not None:
                    if (cleanvalue.lower()[0:9] == 'processus'):
                        return [True, generatedIdForMap]
                        break
    return [False, None]

def initArtefact(**kwargs):
    '''
        initialise the row that is about to be written in a file containing the artefacts for MAP
    '''
    key = ''
    name = ''
    type = ''
    businessID = ''
    ordernumber = ''
    description = ''
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
        if k == 'businessID' : businessID = v
        if k == 'ordernumber' : ordernumber = v
        if k == 'description' : description = v
        if k == 'serviceLevelAgreement' : serviceLevelAgreement = v
        if k == 'frequency' : frequency = v
        if k == 'activityType' : activityType = v
        if k == 'periodicity' : periodicity = v
        if k == 'platform' : platform = v
        if k == 'contractScope' : contractScope = v
    return [key, name, type, businessID, ordernumber, description, serviceLevelAgreement, frequency, activityType, periodicity, platform, contractScope]

def initArtefactHeader():
    '''
        Initialise the first row of the artefact file
    '''
    return initArtefact(key='key', name = 'name', type='name', businessID='businessID', ordernumber='ordernumber', description='description', serviceLevelAgreement='serviceLevelAgreement', frequency='frequency', activityType='activityType', periodicity='periodicity', platform='platform', contractScope='contractScope')

def initRelations(**kwargs):
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
        Initialise the first row of the relation file
    '''
    return initRelations(parentKey='parentKey', childKey='childKey', relationType='relationType', metaX='metaX')

def appendMapFiles(dictionary):
    '''
        Generate 2 files ready to import in MAP :
        - artefacts : all the artefacts of any type to add in MAP
        - relations : relations between the artefacts
    '''
    listOfDefaultsProcess = []
    # initialise the file that will contains all the artefacts (processes & applications)
    artefactscsvfile = open('artefacts.csv', 'w+', newline='')
    artefactswriter = csv.writer(artefactscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    artefactswriter.writerow(initArtefactHeader())

    # initialise the file that will contains all the relations (processes & applications)
    relationscsvfile = open('relations.csv', 'w+', newline='')
    relationswriter = csv.writer(relationscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    relationswriter.writerow(initRelationsHeader())
    # begin to fill up the files
    for file, dictWithDetails in dictionary.items():
        ProcessName = file[file.rfind('-')+1:-(len(file)-(file.find('.')))]
        for id, listOfDetails in dictWithDetails.items():
            (inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target) = listOfDetails
            if (cleanvalue is None):
                label = ''
            else:
                label = cleanvalue
            if (inferedtype == 'swimlane' and label != ''):
                if (label.lower()[0:9] == 'processus'):
                    key = MACROBUSINESSPROCESS+generatedIdForMap
                    name = cleanvalue
                    type = MACROBUSINESSPROCESSTYPE
                    businessID = generatedIdForMap
                    toWrite = initArtefact(key=key, name=name, type=type, businessID=businessID)
                else: #it's an application
                    key = APPLICATION+generatedIdForMap
                    name = cleanvalue
                    type = APPLICATIONTYPE
                    toWrite = initArtefact(key=key, name=name, type=type)
                artefactswriter.writerow(toWrite)
                # find out if the parent is a processus and write the relation if its the case.
                if parentId is not None:
                    [relationtowrite, parentGeneratedIdForMap] = parentIsaProcess(file, parentId)
                    if relationtowrite:
                        relationswriter.writerow([parentGeneratedIdForMap, generatedIdForMap, RELATION_SERVE])
                    else:
                        # create the artefact for a default the process (named after the name of the process in the last part of the filename)
                        defaultArtefactKey = MACROBUSINESSPROCESS+file+parentId
                        if not(getProcessName(file) in listOfDefaultsProcess):
                            listOfDefaultsProcess.append(getProcessName(file))
                            key = defaultArtefactKey
                            name = getProcessName(file)
                            type = MACROBUSINESSPROCESSTYPE
                            businessID=file+parentId
                            toWrite= initArtefact(key=key, name=name, type=type, businessID=businessID)
                            artefactswriter.writerow(toWrite)
                        # create the relation
                        toWrite = initRelations(parentKey=defaultArtefactKey, childKey=generatedIdForMap, relationType=RELATION_SERVE)
                        relationswriter.writerow(toWrite)    
    artefactscsvfile.close()
    relationscsvfile.close()

def appendYedFile(what, dictionary):
    '''
        generate the yed file in 3 pass
        1) nodes creation
        2) hierachy creation
        3) edge creation
    '''
    for id, listOfDetails in dictWithDetails.items():
        (inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target) = listOfDetails
        if (cleanvalue is None):
            label = ''
        else:
            label = cleanvalue
        font_style = "plain"
        font_size = "12"
        if (what == 'yed_nodes'):
            if (source is None):
                if (id != '0' and id != '1'):
                    if (inferedtype == 'generic'):
                        label = label#+"\n---\nstyle="+style
                    if (inferedtype == "swimlane"):
                        font_style="bold"
                        font_size = "14"
                        # I write a node only for swimlanes because other are harder. maybe later
                        # so the indentation is good. To write all nodes unindent 1 time next line
                        g.add_node(id, label=label, font_size=font_size, font_style=font_style)
        if (what == 'yed_hierarchy'):
            if (source is None and inferedtype == 'swimlane'):
                if (parentId is not None and parentId != '0' and parentId != '1'):
                    src = parentId
                    tgt = id
                        # I write a node only for swimlanes because other are harder. maybe later
                        # so the indentation is good. To write all nodes unindent 1 time next line
                    g.add_edge(src, tgt, label="contains")
        if (what == 'yed_edges'):
            if (source is not None):
                g.add_edge(source, target, label="is before")

def getInferedType(style, has_a_source):
    '''
       inferedtype :
       swimlane : {id : [style, value, id_of_parent]} --> style=swimlane
       activity : {id : [style, value, id_of_parent]} --> style=shape=ext or style=html=1
       bpmnartifact : {id : [style, value, id_of_parent]}
       edge : {id : [style, value, id_of_parent, source, destination]} -->  as a source and a target
       note : {id : [style, value, id_of_parent]} --> style=note
       process : {id : [style, value, id_of_parent]}--> style=shape=process
       group : {id : [style, value, id_of_parent]}--> style=group
    '''
    if (style == 'swimlane'):
        return 'swimlane'
    elif (style == 'html=1' or style == 'shape=ext'):
        return 'activity'
    elif (has_a_source):
        return 'edge'
    elif (style == 'note'):
        return 'note'
    elif (style == 'shape=process'):
        return 'process'
    elif (style == 'group'):
        return 'group'
    else:
        return 'generic'


def analysefiles(listOfFiles):
    '''
        parse the list. for each file in the list : get the details of mxCell
        append in a dictionary {filename : {id : [inferedtype, genereatedIdForMap, value, id_of_parent, style, source, target]}}} 
    '''
    has_attribute = lambda mxcell, attribute : attribute in mxcell
    # regex to clean up html tags and special character (e.g. &nbsp;)
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    # main dict {filename : {dictwithdetails}}
    mainDict = {}
    for file in listOfFiles:
        # detailsDict {id : [inferedtype, genereatedIdForMap, value, parentId, style, source, target]}} 
        detailsDict = {}
        listOfdetails = []
        processName = getProcessName(file) 
        with open(file) as xmltoanalyse:
            data = open(file).read()
            # is it an xml file ?
            if data[0:5] == '<?xml':
                myroot = ET.fromstring(data)
                for mxCell in myroot.iter('mxCell'):
                    inferedtype = None
                    generatedIdForMap = None
                    cleanvalue = None
                    parentId = None
                    style = None
                    source = None
                    target = None
                    styleToExamine = None
                    if 'style' in mxCell.attrib:
                        styleToExamine = mxCell.attrib['style'].split(';')[0]
                        ha = has_attribute(mxCell.attrib, 'source')  
                        inferedtype = getInferedType(styleToExamine, ha)
                    if 'id' in mxCell.attrib: generatedIdForMap = processName+mxCell.attrib['id']
                    if 'value' in mxCell.attrib: cleanvalue = re.sub(cleanr,'', mxCell.attrib['value'])
                    if 'parent' in mxCell.attrib: parentId = mxCell.attrib['parent']
                    if 'style' in mxCell.attrib: style = mxCell.attrib['style']
                    if 'source' in mxCell.attrib: source = mxCell.attrib['source']
                    if 'target' in mxCell.attrib: target = mxCell.attrib['target']
                    if 'id' in mxCell.attrib:
                        detailsDict[mxCell.attrib['id']] = inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target
                    else:
                        detailsDict[str(uuid.uuid4())] = inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target
                mainDict[file] = detailsDict
    return mainDict

# ##################################### main ###########################

# parse all files
listOfFiles = getfiles(input_path, extension)

# break down the content of all files into a dictionary
dictOfFilesAndDetails = analysefiles(listOfFiles)

# generate the file for Yed (Graphml file)
for file, dictWithDetails in dictOfFilesAndDetails.items():
    g = pyyed.Graph()
    #g.add_node(file, font_size="14", shape="rectangle3d")
    for what in ('yed_nodes', 'yed_hierarchy'): #, 'yed_edges'):
            appendYedFile(what, dictOfFilesAndDetails)
    g.write_graph(file+'.graphml', pretty_print=True)

# generate the files for MAP
appendMapFiles(dictOfFilesAndDetails)