import insertdb

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

departmentDb={
    "1":"Department of Architecture",
    "2":"Department of Civil Engineering",
    "3":"Department of Electrical Engineering",
    "4":"Department of Mechanical Engineering",
    "5":"Department of Electronics and Computer Engineering"

}

for x in subjectBCT:
    insertdb.insertSubject(x,subjectBCT[x])

for x in classDB:
    insertdb.insertClass(x,classDB[x])

for x in departmentDb:
    insertdb.insertDepartment(x,departmentDb[x])
