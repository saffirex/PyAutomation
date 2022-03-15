#! python
#BAcking up all the files of a folder in a zip file with increments

import zipfile,os,time

def backupthis(folder):
    folder = os.path.abspath(folder)

    sn=1
    while True: #Finds out the right name for the zipfile to be created based on whether or not the filenames already exist
         #basename vs dirname
        zipfilename= os.path.basename(folder)+'_'+str(sn)+'.zip'

        if os.path.exists(zipfilename):
            sn=sn+1
        else:
            break
    
    print(f'Craeating {zipfilename} to backup things in: {folder}')
    time.sleep(1)

    #creating zipfile object
    backupzip= zipfile.ZipFile(zipfilename,'w')

    #file walking to add everything in the folder including all the subfolders and filenames

    for foldername,subfolders,filenamestuple in os.walk(folder):
        print(f'Adding the files in {foldername} to {zipfilename}')

        backupzip.write(foldername)

        for filename in filenamestuple: #not dealing with subfolders because in every iteration the walk method returns the current foldername, subs and files and we are anyhow going to get into coming subfolders in the next upcoming iterations

            newbase= os.path.basename(folder)+ '_'
            if filename.startswith(newbase) and filename.endswith('.zip'):
                continue #i.e don't add existing zip files into the zip we goin to create
            backupzip.write(os.path.join(foldername, filename)) #join= creates a path that joins the folder in current iteration like foldername/filename and then passes it to zipfile's write method that directky adds to the zip
        
    backupzip.close()
    print('Finished')


backupthis(r'C:\Users\IDEAPAD\Desktop\Models\bark')
        