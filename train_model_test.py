#!/usr/bin/env python

# Do *not* edit this script. Changes will be discarded so that we can train the models consistently.

# This file contains functions for training models for the Challenge. You can run it as follows:
#
#   python train_model.py -d data -m model -v
#
# where 'data' is a folder containing the Challenge data, 'model' is a folder for saving your model(s), and , and -v is an optional
# verbosity flag.

import argparse
import sys

from helper_code import *
from team_code import train_digitization_model, train_dx_model

# Parse arguments.
# def get_parser():
#     description = 'Train the Challenge model(s).'
#     parser = argparse.ArgumentParser(description=description)
#     parser.add_argument('-d', '--data_folder', type=str, required=True)
#     parser.add_argument('-m', '--model_folder', type=str, required=True)
#     parser.add_argument('-v', '--verbose', action='store_true')
#     return parser

data_folder = '/home/vinayaka/physionet/sample_train_data/'
model_folder = '/home/vinayaka/physionet/model/'
verbose = '--verbose'

#train_digitization_model(data_folder, model_folder, verbose) ### Teams: Implement this function!!!
train_dx_model(data_folder, model_folder, verbose) ### Teams: Implement this function!!!
