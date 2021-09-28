##########################################
### dram_annotation_extract_pathway.py ###
##########################################
# Author: Samuel Aroney
# Search DRAM annotation to find if pathway present

# Manual test:
# python dram_annotation_extract_pathway.py \
#   --pathways carbon_pathways.tsv \
#   --annotation annotations.tsv \
#   --output test_output.tsv

import argparse
import csv

parser = argparse.ArgumentParser(description='Search DRAM annotation to find if pathway present.')
parser.add_argument('--pathways', type=str, metavar='<PATH>', help='path to pathways definition file (tsv)')
parser.add_argument('--annotation', type=str, metavar='<PATH>', help='path to genome annotation file (tsv)')
parser.add_argument('--output', type=str, metavar='<OUTPUT>', help='path to output file (tsv)')

args = parser.parse_args()
pathways_path = getattr(args, 'pathways')
annotations_path = getattr(args, 'annotation')
output_path = getattr(args, 'output')

print(f"pathways: {pathways_path}; annotations: {annotations_path}; output: {output_path}")



