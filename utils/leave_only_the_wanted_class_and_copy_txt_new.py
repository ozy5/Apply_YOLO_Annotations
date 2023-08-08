

def leave_only_the_wanted_class_and_copy_txt(source_txt_path: str,
                                             dest_txt_path: str,
                                             wanted_indexes: list) -> bool:
    
    '''
    This function takes a txt file path and a destination txt file path and a wanted index.
    It copies the lines that has the wanted index to the destination txt file.
    '''
    wanted_indexes = [str(x) for x in wanted_indexes]

    try:
        with open(source_txt_path, 'r') as in_file:
            lines = in_file.readlines()

        filtered_lines = [line for line in lines if (line.split(' ', 1)[0] in wanted_indexes)]

        with open(dest_txt_path, 'w') as out_file:
            out_file.writelines(filtered_lines)
        #return True if everything is ok
        
        return True
    except:
        #return False if there is an error
        return False








