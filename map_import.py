import argparse
from sys import exit
from src.bpmnextract import analysefiles, createYedFiles, appendMapFiles
from src.capabilities import createCapabilities
from src.data import createBusinessObjects
from lib.csvutil import createfiles
from lib.fileutil import getfiles, fileExist
#--------------------------------------------------------------------------------------------
def exec_bpmn(args):
    '''
        Extract Processes names and application names from drawio files containing BPMN
    '''
    try:
        head, tail = fileExist(args.BpmnPath, 'bpmnPath', 'dir')
    except Exception:
        exit()

    listOfFiles = []
    dictOfFilesAndDetails = {}
    listOfFiles_dictOfFilesAndDetails = []

    listOfFiles = getfiles(args.BpmnPath, args.BpmnFilesExt)
    
    dictOfFilesAndDetails = analysefiles(listOfFiles)
    
    # prepare the list that will carry the variables to pass by reference
    listOfFiles_dictOfFilesAndDetails = [listOfFiles, dictOfFilesAndDetails]

    outputfiles = createfiles(head, ['BPMN2018Artefacts', 'BPMN2018relations'])

    if args.BpmnTypeOfOutput in [0,2]:
        createYedFiles(listOfFiles_dictOfFilesAndDetails)

    if args.BpmnTypeOfOutput in [0,1]:
        appendMapFiles(listOfFiles_dictOfFilesAndDetails, outputfiles)
#--------------------------------------------------------------------------------------------
def exec_bo(args):
    '''
        Extract Business Object from an Excel File
    '''
    try:
        head, tail = fileExist(args.BOExcelFileName, 'BOExcelFileName', 'file')
    except Exception:
        exit()

    totranslate = True if args.totranslateB == 'Y' else False
    outputfiles = createfiles(head, ['BOArtefacts', 'BOrelations'])
    createBusinessObjects(args.BOExcelFileName, outputfiles, totranslate)
#--------------------------------------------------------------------------------------------
def exec_capabilities(args):
    '''
        Extract capabilities from an Excel file
    '''
    try:
        head, tail = fileExist(args.CapabilitiesExcelFileName, 'capabilitiesExcelFileName', 'file')
    except Exception:
        exit()
    totranslate = True if args.totranslateC == 'Y' else False
    outputfiles = createfiles(head, ['ABBArtefacts', 'ABBrelations'])
    createCapabilities(args.CapabilitiesExcelFileName, outputfiles, totranslate)


#--------------------------------------------------------------------------------------------
# Main
my_parser = argparse.ArgumentParser(description='Prepare data (bpmn, Business Objects, ABB) to import into CGI Map')

subparsers = my_parser.add_subparsers(help='subparser command help')

parser_bpmn = subparsers.add_parser('bpmn', help='BPMN help')
parser_bpmn.add_argument('BpmnPath',
                       type=str,
                       help='the path containg the bpmn to parse')
parser_bpmn.set_defaults(func=exec_bpmn)

parser_bpmn.add_argument('BpmnFilesExt',
                       type=str,
                       help='the extensions of BPMN files to parse')

parser_bpmn.add_argument('BpmnTypeOfOutput',
                       type=int,
                       choices=[0,1, 2],
                       default=1,
                       help='Generated output : 0 = MAP and Yed ; 1=MAP only; 2=Yed Only')                       

parser_businessObject = subparsers.add_parser('bo', help='Business Object help')
parser_businessObject.add_argument('BOExcelFileName',
                       type=str,
                       help='the name of the excel file containing the business objects')
parser_businessObject.add_argument('totranslateB',
                       type=str,
                       choices=('Y', 'N'),
                       help='If Y translate English to French')
parser_businessObject.set_defaults(func=exec_bo)

parser_capabilities = subparsers.add_parser('capabilities', help='capabilities help')
parser_capabilities.add_argument('CapabilitiesExcelFileName',
                       type=str,
                       help='the name of the excel file containing the capabilities')
parser_capabilities.add_argument('totranslateC',
                       type=str,
                       choices=('Y', 'N'),
                       help='If Y translate English to French')
parser_capabilities.set_defaults(func=exec_capabilities)

args = my_parser.parse_args()
args.func(args)
