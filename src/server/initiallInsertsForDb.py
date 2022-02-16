import csv
import insertdb
import cv2
import numpy as np
import face_recognition

###################################subject insertion####################################
subjectBCT = {
    "SH401":"Engineering Mathematics I",
    "CT402":"Computr Programming",
    "ME401":"Engineering Drawing I",
    "SH402":"Engineering Physics",
    "CE401":"Applied Mechanics",
    "EE401":"Basic Electrical Engineering",

    "SH451":"Engineering Mathematics II",
    "ME451":"Engineering Drawing II",
    "EX451":"Basic Electronics Engineering",
    "SH453":"Engineering Chemistry",
    "ME452":"Fundamental of Thermodynamics and Heat Transfer",
    "ME453":"Workshop Technology",

    "SH501":"Engineering Mathematics III",
    "CT501":"Object Oriented Programming",
    "CT502":"Theory of Computation",
    "EE501":"Electric Circuit Theory",
    "EX501":"Electronic Devices and Circuits",
    "EX502":"Digital Logic",
    "EX503":"Electromagnetics",

    "SH551":"Applied Mathematics",
    "SH553":"Numerical Methods",
    "EE552":"Instrumentation I",
    "EE554":"Electrical Machines",
    "CT551":"Discrete Structure",
    "CT552":"Data Structure and Algorithm",
    "EX551":"Microprocessor",

    "SH601":"Communication English",
    "SH602":"Probability and Statics",
    "CT601":"Software Engineering",
    "CT602":"Data Communication",
    "CT603":"Computer Organization and Architecture",
    "EX602":"Instrumentation II",
    "EX603":"Computer Graphics",

    "CE655":"Engineering Economics",
    "CT651":"Object Oriented Analysis and Design",
    "CT652":"Database Management System",
    "CT653":"Artificial Intelligence",
    "CT655":"Embedded System",
    "CT656":"Operating System",
    "CT654":"Minor Project",

    "ME708":"Organization and Management",
    "EX701":"Energy Environment and Society",
    "CT701":"Project Management",
    "CT702":"Computer Network",
    "CT703":"Distrubuted System",
    "CT704":"Digital Signal Analysis and Processing",
    "CT725":"Elective I",
    "CT707":"Project(Part A)",

    "CE752":"Professional Practice",
    "CT751":"Information Systems",
    "CT753":"Simulation and Modelling",
    "CT754":"Internet and Intranet",
    "CT765":"Elective II",
    "CT785":"Elective III",
    "CT755":"Project(Part B)"
}

for x in subjectBCT:
    insertdb.insertSubject(x,subjectBCT[x])

##########################################class insertion##############################
classDB={
    "074bctAb":"074bctAb",
    "074bexAb":"074bexAb",
    "074belAb":"074belAb",

    "075bctAb":"075bctAb",
    "075bctCd":"075bctCd",
    "075bexAb":"075bexAb",
    "075belAb":"075belAb",

    "076bctAb":"076bctAb",
    "076bctCd":"076bctCd",
    "076bexAb":"076exAb",
    "076belAb":"076belAb",

    "077bctAb":"077bctAb",
    "077bctCd":"077bctCd",
    "077bexAb":"077bexAb",
    "077belAb":"077belAb"
}

for x in classDB:
    insertdb.insertClass(x,classDB[x])

######################################department insertion##########################
departmentDb={
    "1":"Department of Architecture",
    "2":"Department of Civil Engineering",
    "3":"Department of Electrical Engineering",
    "4":"Department of Mechanical Engineering",
    "5":"Department of Electronics and Computer Engineering"

}

for x in departmentDb:
    insertdb.insertDepartment(x,departmentDb[x])

################################# face embedding calculation ###########################################
'''
listEmbedding =[]

for i in range(52):
    if (i+49) == 87 or (i+49) == 73 or (i+49) == 99 or (i+49) == 97 :   #skip dropouts and section AB added students
        continue
    elif i == 51:
        iterator = str(i+49)
    else:
        iterator = "0"+str(i+49)
        try:
            imag = face_recognition.load_image_file("/home/rohan/Documents/minorProject2022/data/PUL075BCT"+iterator+".jpg")
        except:
            try:
                imag = face_recognition.load_image_file("/home/rohan/Documents/minorProject2022/data/PUL075BCT"+iterator+".jpeg")
            except:
                imag = face_recognition.load_image_file("/home/rohan/Documents/minorProject2022/data/PUL075BCT"+iterator+".png")
        
    imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)

    encodingsTest = face_recognition.face_encodings(imag)[0]
    listEmbedding.append(encodingsTest)

#saving data of face embeddings in a text file
#np.savetxt('embeddingDataCD.txt',listEmbedding,delimiter="\n", fmt="%s")
'''

file =open('./embeddingDataCD.txt')
listEmbedding = file.readlines()
i=0
j=128
#################################csv file reading and insert in student db#############################
# opening the CSV file
with open('./scraper/PUL075BCTCD.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.DictReader(file)

       # insert the contents of the CSV file
       for lines in csvFile:
            insertdb.insertStudent(lines['RollNo'],lines['Name'],"075bctCd","5",listEmbedding[i:j])
            i=i+128
            j=j+128

####################### teaher insertion#############

insertdb.insertTeacher("001","Aman Shakya","5")