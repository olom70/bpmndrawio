# analyse drawio files with BPMN content
'''

10) Open  all the files of a directory
    for each file name ; catch filename

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
third pass : create link between activities by creating edges  (labels "is before")

'''
import xml.etree.ElementTree as ET
import pyyed
import uuid
from lib.csvutil import initArtefact, initArtefactHeader, initRelations, initRelationsHeader
from lib.stringutil import cleanName, getNameLastPart


####### Global SCope Variables ##############
MACROBUSINESSPROCESS = 'MACROBUSINESSPROCESS:'
BUSINESSPROCESS = 'BUSINESSPROCESS:'
APPLICATION = 'APPLICATION:'
MACROBUSINESSPROCESSTYPE  = 'MacroBusinessProcess'
BUSINESSPROCESSTYPE  = 'BusinessProcess'
APPLICATIONTYPE = 'Application'
RELATION_SERVE = 'serves'


def parentIsaProcess(myfile, parentID, listOfFiles_dictOfFilesAndDetails):
    '''
        In the files that are analysed, processes names are in swimlanes
        and a valid name always begin with "processus"
    '''
    for file, dictWithDetails in listOfFiles_dictOfFilesAndDetails[1].items():
        for id, listOfDetails in dictWithDetails.items():
            (inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target) = listOfDetails
            if (myfile == file and parentID == id): # as I am not sure that ID are UUID I want to make sure that I found the right parent in the right file
                if cleanvalue is not None:
                    if (cleanvalue.lower()[0:9] == 'processus'):
                        return [True, BUSINESSPROCESS+generatedIdForMap]
                        break
    return [False, None]


def appendMapFiles(listOfFiles_dictOfFilesAndDetails: list(), outputfiles: list()):
    '''
        Generate 2 files ready to import in MAP :
        - artefacts : all the artefacts of any type to add in MAP
        - relations : relations between the artefacts
    '''
    listOfDefaultsProcess = []
    listOfProcessedArtefacts = []
    outputfiles[1].writerow(initArtefactHeader())
    outputfiles[3].writerow(initRelationsHeader())
    # begin to fill up the files
    for file, dictWithDetails in listOfFiles_dictOfFilesAndDetails[1].items():
        for id, listOfDetails in dictWithDetails.items():
            (inferedtype, generatedIdForMap, cleanvalue, parentId, style, source, target) = listOfDetails
            if (cleanvalue is None):
                label = ''
            else:
                label = cleanvalue
            if (inferedtype == 'swimlane' and label != ''):
                if (label.lower()[0:9] == 'processus'):
                    key = BUSINESSPROCESS+generatedIdForMap
                    name = label
                    type = BUSINESSPROCESSTYPE
                    businessID = generatedIdForMap
                    toWrite = initArtefact(key=key, name=name, type=type, businessID=businessID)
                else: #it's an application
                    key = APPLICATION+generatedIdForMap
                    name = label
                    type = APPLICATIONTYPE
                    toWrite = initArtefact(key=key, name=name, type=type)
                if (key not in listOfProcessedArtefacts and name != 'NoName'):
                    listOfProcessedArtefacts.append(key)  # the artefact is created only once, so i avoid duplicates by controlling against prvious keys
                    outputfiles[1].writerow(toWrite)
                    # find out if the parent of the current application is a processus and write the relation if its the case.
                    if (parentId is not None and label.lower()[0:9] != 'processus'):
                        [relationtowrite, parentGeneratedIdForMap] = parentIsaProcess(file, parentId, listOfFiles_dictOfFilesAndDetails)
                        # link the current application with the parent swimlane only if it's a valid processus
                        if relationtowrite:
                            outputfiles[3].writerow([APPLICATION+generatedIdForMap, parentGeneratedIdForMap, RELATION_SERVE])
                        else:
                            # create the artefact for a "default process" named after the name of the process in the last part of the filename
                            defaultArtefactKey = BUSINESSPROCESS+getNameLastPart(file, '-')+parentId
                            if not getNameLastPart(file, '-') in listOfDefaultsProcess:
                                listOfDefaultsProcess.append(getNameLastPart(file, '-'))
                                key = defaultArtefactKey
                                name = getNameLastPart(file, '-')
                                type = BUSINESSPROCESSTYPE
                                businessID=getNameLastPart(file, '-')+parentId
                                toWrite= initArtefact(key=key, name=name, type=type, businessID=businessID)
                                outputfiles[1].writerow(toWrite)
                            # create the relation between the current application and the default process
                            toWrite = initRelations(parentKey=APPLICATION+generatedIdForMap, childKey=defaultArtefactKey, relationType=RELATION_SERVE)
                            outputfiles[3].writerow(toWrite)
    outputfiles[0].close()
    outputfiles[2].close()

def appendYedFile(what: str, dictWithDetails: dict(), YedObject: list()):
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
                        YedObject[0].add_node(id, label=label, font_size=font_size, font_style=font_style)
        if (what == 'yed_hierarchy'):
            if (source is None and inferedtype == 'swimlane'):
                if (parentId is not None and parentId != '0' and parentId != '1'):
                    src = parentId
                    tgt = id
                        # I write a node only for swimlanes because other are harder. maybe later
                        # so the indentation is good. To write all nodes unindent 1 time next line
                    YedObject[0].add_edge(src, tgt, label="contains")
        if (what == 'yed_edges'):
            if (source is not None):
                YedObject[0].add_edge(source, target, label="is before")

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

def analysefiles(listOfFiles: list()):
    '''
        parse the input list.
        For each file in the list : get the details of mxCell
        append in a dictionary {filename : {id : [inferedtype, genereatedIdForMap, value, id_of_parent, style, source, target]}}} 
    '''
    has_attribute = lambda mxcell, attribute : attribute in mxcell
    # regex to clean up html tags and special character (e.g. &nbsp;)
    # main dict {filename : {dictwithdetails}}
    mainDict = {}
    for file in listOfFiles:
        # detailsDict {id : [inferedtype, genereatedIdForMap, value, parentId, style, source, target]}} 
        detailsDict = {}
        listOfdetails = []
        processName = getNameLastPart(file, '-')
        with open(file, encoding='utf-8') as xmltoanalyse:
            data = xmltoanalyse.read()
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
                    if ('id' in mxCell.attrib and 'value' in mxCell.attrib): generatedIdForMap = cleanName(mxCell.attrib['value'], False, True, 'uppercase', True, True, True)
                    if ('id' in mxCell.attrib and 'value' not in mxCell.attrib): generatedIdForMap = mxCell.attrib['id']
                    if 'value' in mxCell.attrib: cleanvalue = cleanName(mxCell.attrib['value'], False, False, 'noChange', True, False, True)
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

def createYedFiles(lisOfFiles_dictOfFilesAndDetails):
 # generate the file for Yed (Graphml file)
    for file, dictWithDetails in lisOfFiles_dictOfFilesAndDetails[1].items():
        g = pyyed.Graph()
        for what in ('yed_nodes', 'yed_hierarchy'): #, 'yed_edges'):
            appendYedFile(what, dictWithDetails, [g])
        g.write_graph(file+'.graphml', pretty_print=True)