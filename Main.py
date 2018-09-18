"""
Created on Mon Sep 17 20:44:54 2018
@author: William E Basquez
"""

import os
import random
from pathlib import Path


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
	# To be implemented by Diego: Replace with ML model
	# Changed by William Basquez to extend capabilities
    # (mawilliams7) Two if statements not necessary here. Elif could be used.
    if "dog" in path:
        return 0.5 + random.random() / 2
    if "cat" in path:
        return random.random() / 2
    else:
        return 0.5


#This function fills arrays with either dog or cat 'pictures'.
#by looking through the current directory
def populateArrs(fileList):
    cats = []
    dogs = []
	
    for i in range(len(fileList)):
        if classify_pic(fileList[i]) > 0.5:
            dogs.append(fileList[i])
        elif classify_pic(fileList[i]) < 0.5:
            cats.append(fileList[i])
	
    return [cats, dogs]
		

def process_dir(path):
	
    dir_list, file_list = get_dirs_and_files(path)
	
    cat_list = []
    dog_list = []
    # (mawilliams7) It's not really necessary to have the three separate if statements,
    # maybe an if, elif, else would be better. Its possible if, else could do too.
	#If there are no more 'folders', just populate lists and return them
    if len(dir_list) == 0:
        for i in range(len(file_list)):
            cat_list = populateArrs(file_list)[0]
            dog_list = populateArrs(file_list)[1]
            
        return [cat_list, dog_list]
	
	#If there is only one 'folder', populate lists and join paths with that single 'folder'
    if len(dir_list) == 1:
	# (mawilliams7) I'm unsure what this for loop is doing as i is not being used.
        for i in range(len(file_list)):
            cat_list = populateArrs(file_list)[0]
            dog_list = populateArrs(file_list)[1]
        
        cat_list.extend(process_dir(os.path.abspath(os.path.join(path, dir_list[0])))[0])
        dog_list.extend(process_dir(os.path.abspath(os.path.join(path, dir_list[0])))[1])
    
    #If there are more than one 'folder', populate lists and join paths with every 'folder'
    if len(dir_list) > 1:
	# (mawilliams7) Same for loop comment as above.
        for i in range(len(file_list)):
            cat_list = populateArrs(file_list)[0]
            dog_list = populateArrs(file_list)[1]
        
        for i in range(len(dir_list)):
            cat_list.extend(process_dir(os.path.abspath(os.path.join(path, dir_list[i])))[0])
            dog_list.extend(process_dir(os.path.abspath(os.path.join(path, dir_list[i])))[1])
    # (mawilliams7) Nit: Brackets not really necessary here, but fine if kept.
    return [cat_list, dog_list]


def main():
    start_path = './'
	
    listCats, listDogs = process_dir(start_path)
    	
    #for i in range(len(listCats)):
    #    print("Cat",(i+1),":", listCats[i])
    #for i in range(len(listDogs)):
    #   print("Dog",(i+1),":", listDogs[i])

	
main()
