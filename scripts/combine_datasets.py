import os
import sys
from difflib import SequenceMatcher
from tqdm import tqdm

def combine_datasets(p1,p2):
    '''
    Compare two datasets and merge them into one. 

    Args:
        p1 (str): Path to dataset 1. This also is the final dataset.
        p2 (str): Path to dataset 2

    Dataset structure:
        p
        ├── class1
        │   ├── img1.jpg
        │   ├── img2.jpg
        │   └── ...
        ├── class2
        │   ├── img1.jpg
        │   ├── img2.jpg
        │   └── ...
        └── ...
    '''
    classes_p1 = os.listdir(p1)
    classes_p2 = os.listdir(p2)
    classes_p1 = [c.lower() for c in classes_p1]
    classes_p2 = [c.lower() for c in classes_p2]    
    all_classes = list(set(classes_p1).union(set(classes_p2)))
    print(f'Found {len(all_classes)} classes in total')


            


    pbar = tqdm(all_classes, unit='classes', total=len(all_classes))
    for c in pbar:
        if c in classes_p1 and c in classes_p2:
            merge_folders(os.path.join(p1,c), os.path.join(p2,c))

        elif c in classes_p1:
            for c2 in classes_p2:
                if SequenceMatcher(None, c, c2).ratio() > 0.9:
                    merge_folders(os.path.join(p1,c), os.path.join(p2,c2))
                    
        elif c in classes_p2:
            for c2 in classes_p1:
                if SequenceMatcher(None, c, c2).ratio() > 0.9:
                    merge_folders(os.path.join(p1,c2), os.path.join(p2,c))

        elif c in classes_p2 and c not in classes_p1:
            os.rename(os.path.join(p2,c), os.path.join(p1,c))


def merge_folders(p1,p2):
    '''
    Merge two folders into one. 

    Args:
        p1 (str): Path to folder 1. This also is the final folder.
        p2 (str): Path to folder 2

    '''
    files_p1 = os.listdir(p1)
    files_p2 = os.listdir(p2)

    for f in files_p2:
        if f not in files_p1:
            os.rename(os.path.join(p2,f), os.path.join(p1,f))
        else:
            new_p = increment_path(os.path.join(p1,f))
            os.rename(os.path.join(p2,f), new_p)


def increment_path(p):
    if not os.path.exists(p):
        return p
    i = 0
    while os.path.exists(p):
        p = f'{p.split(".")[0]}_{i}.{p.split(".")[1]}'
        i += 1
    return p

if __name__ == '__main__':
    '''
    This script is used to combine two datasets into one. This is especially useful when one has two datasets with intersecting classes.
    Usage: python utils/preprocess.py <path_to_dataset1> <path_to_dataset2>
    '''
    p1, p2 = sys.argv[1], sys.argv[2]
    combine_datasets(p1,p2)
