

def leave_only_the_wanted_class_and_copy_txt(source_txt_path: str,
                                             dest_txt_path: str,
                                             wanted_indexes: list) -> bool:
    
    '''
    This function takes a txt file path and a destination txt file path and a wanted index.
    It copies the lines that has the wanted index to the destination txt file.
    '''
    wanted_indexes = [str(x) for x in wanted_indexes]

    try:
        with open(source_txt_path, "r") as f:
            #open the source txt file
            lines = f.readlines()

            #open the destination txt file
            with open(dest_txt_path, "w") as f2:
                #iterate over the lines
                for line in lines:
                    #strip the line
                    linestrp = line.strip()
                    #if the first element of the line is on of the wanted indexes
                    if linestrp.split(" ")[0] in wanted_indexes:
                        #write the line to the destination txt file
                        changed_line = "0" + line[1:]
                        f2.write(changed_line)
        #return True if everything is ok
        return True
    except:
        #return False if there is an error
        return False


source = "/home/umut/Desktop/remaining_images/labels/Frame-0502_png_jpg.rf.d2870441dba7be2fc8823083f5f3730b.txt"
dest = "/home/umut/Desktop/Frame-0502_png_jpg.rf.d2870441dba7be2fc8823083f5f3730b.txt"

leave_only_the_wanted_class_and_copy_txt(source, dest, [4])







