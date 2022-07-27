# PCUserLog_FaceRecognition
 Record any faces when PC is logged in


**How to use it:**
1. Download the files and make sure it's being put in the same folder.
2. Create a folder and name it "FaceData".
3. Open task scheduler, then create new task.
4. Add new trigger and set "begin the task" to "at log on"
5. Add new action, set the script to your python.exe (eg. C:\Users\XXX\Local\Programs\Python\Python37\python.exe), set the arguments to "FaceRecordData.pyw", and set the start in to XXX\PCUserLog_FaceRecognition [fill the XXX depends on the file's location]
6. Enable the task.
7. DONE!
