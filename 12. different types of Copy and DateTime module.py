###$$$~~~~~~~ Copy ~~~~~~~~$$$####


##import copy
##var = [["a","b"],["c","d"]]
##newvar = copy.copy(var)
##
###after the copy
##print(var)
##print(newvar)
##
###copy.copy is called "shallow copy because....
##newvar[1][0] = "e"
##
###above code tries to change the value of "c" form to "e" from the list
##print(newvar)
##print(var)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import copy
##var = [["a","b",],["c","d",]]
##newvar = copy.deepcopy(var)
##
###after the copy
##print(var)
##print(newvar)
##
###copy.deepcopy is called "deep copy because....
##newvar[1][0] = "e"
##
###above code tries to change the value of "c" form to "e" from the list
##print(newvar)
##print(var)
### when newvar gets the change it will not reflect back to the existing variable
### "cloning" happens here instead of object reference.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import copy
##
##old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
##new_list = copy.copy(old_list)
##
##old_list.append([4, 4, 4])
##
##print("Old list:", old_list)
##print("New list:", new_list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~ shutil() ~~~~~~~~~~~~~~~~~~~~~

##import os
##import shutil
##import time
##
##stat_info = os.stat('camera.jpg')
##print(stat_info)
##
##print(' Created :', time.ctime(stat_info.st_ctime))
##print(' Accessed:', time.ctime(stat_info.st_atime))
##print(' Modified:', time.ctime(stat_info.st_mtime))
##
##os.mkdir('new123')
##shutil.copy2('camera.jpg' , 'new123')
##
##abc = os.stat('new123/camera.jpg')
##print(abc)
##print(' Created :', time.ctime(abc.st_ctime))
##print(' Accessed:', time.ctime(abc.st_atime))
##print(' Modified:', time.ctime(abc.st_mtime))




##import os
##import shutil
##import time
##
##def file_metadata(a):
##    stat_info = os.stat(a)
##    #print(' Mode    :', int(stat_info.st_mode))
##    print(' Created :', time.ctime(stat_info.st_ctime))
##    print(' Accessed:', time.ctime(stat_info.st_atime))
##    print(' Modified:', time.ctime(stat_info.st_mtime))
##
##os.mkdir('Deepak_metadata')
##print("SOURCE FILE:")
##file_metadata('camera.jpg')
##
##shutil.copy2('camera.jpg' , 'Deepak_metadata')
##
##print("DESTINATION FILE:")
##file_metadata('Deepak_metadata/camera.jpg')



##import shutil
##import os
##
##print(os.listdir("."))
##shutil.copy("camera.jpg","copycamera.jpg")
##print(os.listdir("."))
##
##
##os.mkdir('Deepak_new')
##shutil.copy("camera.jpg",'Deepak_new')
##print(os.listdir('Deepak_new'))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ~~~~ Print current daye and time ~~~~~#####

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##from datetime import datetime, timedelta 
##time_var = datetime.now()
##print(time_var)

##print(datetime.now())

##time_var_second_removal = time_var.replace(microsecond = 0)
##print(time_var_second_removal)


##time_var_adding = time_var + timedelta(seconds = 10)
##print(time_var_adding)

    ###~~~~~~~ fmt = "%y%m%d %H%M%S # default time format

##fmt = "%Y**%B**%d %H/%M/%S"
##format_change = datetime.strftime(time_var, fmt)
##print(format_change)
