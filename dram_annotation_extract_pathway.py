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
import pandas as pd

from mag_annotator.summarize_genomes import make_etc_coverage_df

parser = argparse.ArgumentParser(description='Search DRAM annotation to find if pathway present.')
parser.add_argument('--pathways', type=str, metavar='<PATH>', help='path to pathways definition file (tsv)')
parser.add_argument('--annotation', type=str, metavar='<PATH>', help='path to genome annotation file (tsv)')
parser.add_argument('--output', type=str, metavar='<OUTPUT>', help='path to output file (tsv)')

args = parser.parse_args()
pathways_path = getattr(args, 'pathways')
annotations_path = getattr(args, 'annotation')
ANNOTATION_GROUP_COLUMN = "fasta"
output_path = getattr(args, 'output')
OUTPUT_DELIM = "\t"


module_df = pd.read_csv(pathways_path, sep='\t')
annotations = pd.read_csv(annotations_path, sep='\t', index_col=0)

coverage_df = make_etc_coverage_df(module_df, annotations, groupby_column=ANNOTATION_GROUP_COLUMN)
coverage_df = coverage_df.drop(["complex", "complex_module_name"], axis=1)

coverage_df.to_csv(output_path, sep = OUTPUT_DELIM, index=False)


