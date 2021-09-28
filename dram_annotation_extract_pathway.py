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
import networkx as nx
import pandas as pd
import pdb

from mag_annotator.summarize_genomes import make_module_network
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
KEGG_REGEX = r"K\d\d\d\d\d"

# Encode pathways definitions as list of KO identifiers and logical expression
# e.g.
# INPUT: (K00163+K00627,K00169,K03737,K00174,K00656) (K13788,K04020) (K01512,K00925)
# LIST:  [K00163, K00627, K00169, K03737, K00174, K00656, K13788, K04020, K01512, K00925]
# LOGIC: (0 * 1 + 2 + 3 + 4 + 5) * (6 + 7) * (8 + 9)
# with open(pathways_path) as file:
#     pathways_reader = csv.reader(file, delimiter="\t")

#     pathways = {}
#     for line in pathways_reader:
#         if line[0] == "pathway":
#             continue

#         pathway = line[0]
#         definition = line[1].replace(" ", "+")
#         print(definition)

#         network, _ = make_module_network(definition)
#         # add end node
#         no_out = [node for node in network.nodes() if network.out_degree(node) == 0]
#         for node in no_out:
#             network.add_edge(node, 'end')
        
#         pathways[pathway] = network

#         print(pathway)
#         print(network.nodes())

#module_nets = {module: build_module_net(module_df)
#               for module, module_df in module_steps_form.groupby('module') if module in HEATMAP_MODULES}

module_df = pd.read_csv(pathways_path, sep='\t')
annotations = pd.read_csv(annotations_path, sep='\t', index_col=0)

coverage_df = make_etc_coverage_df(module_df, annotations, groupby_column=ANNOTATION_GROUP_COLUMN)
coverage_df = coverage_df.drop(["complex", "complex_module_name"], axis=1)


pdb.set_trace()


