import requests
import argparse
from Bio import SeqIO
from Bio.PDB import PDBList
import sys
from zipfile import ZipFile

# Load input data
parser = argparse.ArgumentParser()
parser.add_argument('--query', help = 'The query')
parser.add_argument('--t_templates', help = 'Choose type of input if compressed file with PDBs or a list of PDBs IDs')
parser.add_argument('--templates', help = 'The templates')
#parser.add_argument('--aln_engine', help = 'Choose the alignment engine', default = "muscle")
args = parser.parse_args()

# Parse the inputs
def extract_if_zip(zip_filename):
    """Extract the PDB files from a zipfile if input is indeed a zip file."""
    # opening the zip file in READ mode
    with ZipFile(zip_filename, 'r') as zip:
        # printing all the contents of the zip file
        #zip.printdir()
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

def get_PDBs(pdbs):
    """Selecting structures from PDB"""
    if isinstance(pdbs,str):
        return PDBList.retrieve_pdb_file(pdbs, obsolete=False,  file_format="pdb", pdir = 'PDB')
    elif isinstance(pdbs,list):
        pdbl = PDBList()
        for i in pdbs:
            pdbl.retrieve_pdb_file(i, obsolete=False,  file_format="pdb", pdir = 'PDB')
        return pdbl

def get_sequence_from_PDB(PDBFile):
    """Extracts the sequence from each PDB"""
    with open(PDBFile, 'r') as pdb_file:
        for record in SeqIO.parse(pdb_file, 'pdb-atom'):
            print('>' + record.id)
            print(record.seq)

def parse_fasta(filename):
    x = 0




query = args.query
#ID,seq_query = parse_fasta(query)

if args.t_templates == "zip":
    zip_filename = args.templates
    extract_if_zip(zip_filename)

elif args.t_templates == "list":
    templates_IDs = args.templates.split(',')
    # Download PDBs temporarily
    get_PDBs(templates_IDs)
    templates = []
    #templates = {}
    for ID in templates_IDs:
        templates.append(get_sequence_from_PDB("/PDB/pdb"+ID.lower()+".ent"))
else:
    print("There was an error in the type of templates you entered. It was not a file nor a comma-separated PDB ID list ")
    sys.exit(1)

# Get the PDBs if needed



# Produce the alignment



# Output the PIR format alignment



