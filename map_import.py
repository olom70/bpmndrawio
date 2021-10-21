import argparse
import os
import sys

def fileExist(fullpath: str, typeExtraction: str, dir=['dir', 'file'] ):
    '''
       Check if the specified path exist.
       If so : return head, tail from os.path.split()
       If not : exit from the script
    '''
    if (dir=='file'):
        if not os.path.isfile(fullpath):
            print('arg {v} : The specified file does not exist'.format(v=typeExtraction))
            sys.exit()
    else:
        if not os.path.isdir(fullpath):
            print('arg {v} : The specified path does not exist'.format(v=typeExtraction))
            sys.exit()

    head, tail = os.path.split(fullpath)
    return [head, tail]

def exec_bpmn(args):
    bpmnPath = args.BpmnPath
    bpmnFilesExt = args.BpmnFilesExt
    bpmnTypeOfOutput = args.BpmnTypeOfOutput
    head, tail = fileExist(bpmnPath, 'bpmnPath', 'dir')

def exec_bo(args):
    BOExcelFileName = args.BOExcelFileName
    head, tail = fileExist(BOExcelFileName, 'BOExcelFileName', 'file')

def exec_capabilities(args):
    capabilitiesExcelFileName = args.CapabilitiesExcelFileName
    head, tail = fileExist(capabilitiesExcelFileName, 'capabilitiesExcelFileName', 'file')

# Part to use that script as a command line tool
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
parser_businessObject.set_defaults(func=exec_bo)

parser_capabilities = subparsers.add_parser('capabilities', help='capabilities help')
parser_capabilities.add_argument('CapabilitiesExcelFileName',
                       type=str,
                       help='the name of the excel file containing the capabilities')
parser_capabilities.set_defaults(func=exec_capabilities)
# Execute the parse_args() method
args = my_parser.parse_args()
args.func(args)
