import argparse
import os
import logging
from collections import namedtuple
logging.basicConfig(filename="log2.log", encoding="utf8", level=logging.INFO) 
logger = logging.getLogger("log") 



DATA = namedtuple("DATA", "name extension flag parent") 


def get_data(path): 
    filename = os.path.splitext(os.path.basename(path))[0]
    extension = os.path.splitext(os.path.basename(path))[1]
    par = os.path.split(os.path.dirname(path))[1]
    fl = os.path.isdir(path) 
    d = DATA(name=filename, extension = extension, flag=fl, parent=par) 
    logger.info(DATA(d.name, d.extension, d.flag, d.parent)) 
    return d


parser = argparse.ArgumentParser(usage='Не введены значения аргументами')
parser.add_argument(dest='path', type=str)
args = parser.parse_args()

print(get_data(args.path))
