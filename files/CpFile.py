#!/usr/bin/env python

import shutil
import os


class CpFile :
    """[This class allow the user to copy files and folder]
    There are several way to copy files :
        - Copy directly all the file
        - Copy the files which are changed by the user
    """

    def __init__(self, src, dst):
        """[constructor]

        Args:
            srd ([String]): [path of folder/Files that the user want to backup]
            dst ([String]): [path of the destination to backup the folder/files]
        """
        self.src = src
        self.dst = dst
    
    
    def copy(self):
        """[copy src file to dst and call fail if an error occured]

        Returns:
            [Bool]: [return the state of the copy : true if succeded and false otherwise]
        """
        try:
            shutil.copytree(self.src,self.dst,symlinks=True)
            return ""
        except OSError as err:
            return err
    
    def fail(self):
        """[remove the files which are already created]
        """
        try:
            shutil.rmtree(self.dst)
            return ""
        except OSError as err:
            return err
    

if __name__ == '__main__':
    #file = CpFile("/home/paymal/Documents/CMI","/media/paymal/Nouveau nom/Test")
    print(file.copy())
