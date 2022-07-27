import pickle
import streamlit as st
import pandas as pd

pickle_in = open("edtech_model.pkl", 'rb')
model = pickle.load(pickle_in)


def predict_cost(institute, course_name, mode_of_program, course_duration, Country, City,
                 certification_provided, practice_assignments_included, doubt_session, 
                internship_provided, course_rating, placement_assistance, recorded_videos, trainer_grade):
    
    if institute == 'TraiNocate':
        institute = 78
    elif institute == 'Iverson':
        institute = 44
    elif institute == '360DigiTMG':
        institute = 0
    elif institute == 'Mindasys':
        institute = 51
    elif institute == 'Simplilearn':
        institute = 68       
    elif institute == 'Qspyders':
        institute = 61
    elif institute == 'Udemy':
         institute = 80
    elif institute == 'Besant technologies':
        institute = 9
    elif institute == 'IMARTICUS Learning':
         institute = 39
    elif institute == 'Velocity':
        institute = 84
    elif institute == 'IBM':
        institute = 36
    elif institute == 'Datamines Global Institute for Data Science':
        institute = 19
    elif institute == 'UpGrad':
        institute = 81
    elif institute == 'Diksha':
        institute = 22
    elif institute == 'ACTE':
        institute = 2
    elif institute == 'Cisco':
         institute = 10
    elif institute == 'Coursera':
        institute = 14
    elif institute == 'Harvard University':
        institute = 35
    elif institute == 'ExcelR':
        institute = 28
    elif institute == 'Resh I Technologies':
        institute = 63
    elif institute == 'Siptech':
         institute = 69
    elif institute == 'Codegn':
        institute = 13
    elif institute == 'DeepNeuron':
        institute = 20
    elif institute == 'Data Gyan':
        institute = 17
    elif institute == 'BEPEC':
         institute = 8   
    elif institute == 'Data Pro':
        institute = 18
    elif institute == 'Pace Institute':
        institute = 56
    elif institute == 'Pincle':
        institute = 59
    elif institute == 'Livewire Institute':
        institute = 47
    elif institute == 'Internshala':
        institute = 43
    elif institute == 'ACE training':
        institute = 1
    elif institute == 'Techsutra':
        institute = 75            
    elif institute == 'Rahitech':
        institute = 62
    elif institute == 'NPTEL':
        institute = 53
    elif institute == 'Innomatics Research Labs':
        institute = 41 
    elif institute == 'III Bombay':
        institute = 38
    elif institute == 'IIMBx':
        institute = 37
    elif institute == 'Microsoft':
        institute = 49
    elif institute == 'Scaler':
        institute = 66
    elif institute == 'AWS':
        institute = 3
    elif institute == 'Edureka':
        institute = 27
    elif institute == 'Social Prachar':
         institute = 71
    elif institute == 'Palle Technologies':
        institute = 57
    elif institute == 'Institute of Industrial Design':
        institute = 42
    elif institute == 'GIT Solutions':
        institute = 31
    elif institute == 'Shri Shiridi sai institute':
        institute = 67
    elif institute == 'Dreams Media Solutions':
        institute = 23
    elif institute == 'Lucid IT solutions':
        institute = 48   
    elif institute == 'Sandsya Institute':
         institute = 65
    elif institute == 'Sulekha Institute':
        institute = 73
    elif institute == 'Prime Classes':
        institute = 60       
    elif institute == 'SV Trainings':
        institute = 64
    elif institute == 'Alison':
        institute = 6
    elif institute == 'Elearn InfoTech':
        institute = 24
    elif institute == 'ISC':
        institute = 40   
    elif institute == 'Great Learning':
         institute = 33   
    elif institute == 'Newsion':
        institute = 54
    elif institute == 'Fabtech':
        institute = 30
    elif institute == 'AdelaideX':
        institute = 4
    elif institute == 'Digital Nest':
        institute = 21
    elif institute == 'Valaxy Tech':
        institute = 83
    elif institute == 'Aditi Digital Solution':
        institute = 5   
    elif institute == 'JSpyders':
         institute = 45   
    elif institute == 'Skillslash learn':
        institute = 70
    elif institute == 'Miles Education':
        institute = 50
    elif institute == 'DV Analytics':
        institute = 16
    elif institute == 'The IOT academy':
        institute = 76
    elif institute == 'Uptop education':
        institute = 82    
    elif institute == 'Zenclassofficial':
         institute = 85   
    elif institute == 'JanBask Training':
        institute = 46
    elif institute == 'Edubridge Learn':
        institute = 25
    elif institute == 'Nuclearnedu':
        institute = 55
    elif institute == 'Geeklearn':
        institute = 32
    elif institute == 'Pantech':
        institute = 58    
    elif institute == 'Almabetter':
         institute = 7   
    elif institute == 'NIIT':
        institute = 52
    elif institute == 'TalentSprint':
        institute = 74
    elif institute == 'FITA Academy':
        institute = 29
    elif institute == 'Softlogic Systems':
        institute = 72
    elif institute == 'Tutedude':
        institute = 79    
    elif institute == 'Edupraj':
        institute = 26
    elif institute == 'Credo Systemz':
        institute = 15
    elif institute == 'CloudyML':
        institute = 12
    elif institute == 'Gutsy':
        institute = 34
    elif institute == 'Cloud X lab':
        institute = 11
    elif institute == 'Thriyam':
        institute = 77
        
            
    if course_name == 'Data Science':
        course_name = 60
    elif course_name == 'Python':
        course_name = 138
    elif course_name == 'Data Analytics':
        course_name = 56
    elif course_name == 'Software Development':
        course_name = 150
    elif course_name == 'Full stack Development':
        course_name = 92
    elif course_name =='Software Testing':
        course_name = 151
    elif course_name == 'Data Science Masters Program':
        course_name = 62
    elif course_name == 'AutoCAD':
        course_name = 24
    elif course_name == 'Tableau':
        course_name = 153
    elif course_name == 'Data Science with ML':
        course_name = 68
    elif course_name == 'C Programming':
        course_name = 35
    elif course_name == 'Agile Project Management Foundation':
        course_name = 14
    elif course_name == 'IBM Certified Data Science':
        course_name = 95
    elif course_name == 'Testing Selenium':
        course_name = 154
    elif course_name == 'Deep Learning':
        course_name = 74
    elif course_name == 'Certified Data Science Course':
        course_name = 45
    elif course_name == 'Machine Learning with Python':
        course_name = 114
    elif course_name == 'Full Stack Java':
        course_name = 91   
    elif course_name == 'Data Science and AI':
        course_name = 64
    elif course_name == 'Java':
        course_name = 104
    elif course_name == 'Artificial Intelligence':
        course_name = 22
    elif course_name == 'Machine Learning':
        course_name = 110                
    elif course_name == 'PHP Security':
        course_name = 130
    elif course_name == 'Salesforce':
        course_name = 147    
    elif course_name == 'Designing and implementing Microsoft DevOps solutions':
        course_name = 78
    elif course_name == 'Salesforce CRM training':
        course_name = 148
    elif course_name == 'Core Java':
        course_name = 53
    elif course_name == 'Microsoft Information Protection Administrator':
        course_name = 121   
    elif course_name == 'Data Mining with Python':
        course_name = 58
    elif course_name == 'Red Hat System Administration':
        course_name = 143
    elif course_name == 'AI Career Transition Program':
        course_name = 2
    elif course_name == 'Administrating Windows Server Hybrid Core Infrastructure':
        course_name = 10   
    elif course_name == 'Data Science Career Transition Program':
        course_name = 61
    elif course_name == 'Full Stack Data Science Course':
        course_name = 90
    elif course_name == 'Designing Cisco Enterprise Networks v1.1':
        course_name = 77
    elif course_name == 'MSBI':
        course_name = 109    
    elif course_name == 'Python and Data Science FullStack':
        course_name = 139
    elif course_name == 'Android Security Essentials':
        course_name = 18         
    elif course_name == 'Linux System Engineer':
        course_name = 107
    elif course_name == 'Big Data Hadoop Training':
        course_name = 32    
    elif course_name == 'Administration of IBM WebSphere DataPower Gateway V7':
        course_name = 11
    elif course_name == 'Certified Visual Analytics Expert Training':
         course_name = 50
    elif course_name == 'Oracle Big Data Fundamentals Ed 1':
        course_name = 129
    elif course_name == 'AWS':
        course_name = 4    
    elif course_name == 'Crisis Communication Manager':
        course_name = 54
    elif course_name == 'Network Installation,Configuration and Administration':
        course_name = 126  
    elif course_name == 'Azure DevOps':
        course_name = 29
    elif course_name == 'SAN Management':
        course_name = 144   
    elif course_name == 'Python with ML':
        course_name = 142
    elif course_name == 'MYSQL 5.7 for Database Administrators':
        course_name = 124
    elif course_name == 'MYSQL 8.0 Fundamentals':
        course_name = 125   
    elif course_name == 'Developing on AWS':
        course_name = 82    
    elif course_name == 'The Complete 2022 Web Development Course - Build 15 Projects':
        course_name = 155
    elif course_name == 'Web Development with Python and Django':
        course_name = 158   
    elif course_name == 'Machine Learning on GCP':
        course_name = 113
    elif course_name == 'Data Visualization using Tableau':
        course_name = 72
    elif course_name == 'Data visualization Using Power BI training':
        course_name = 73
    elif course_name == 'Executive programme in Full stack Data Science':
        course_name = 86
    elif course_name == 'Artificial Intelligence & Deep Learning courses training':
        course_name = 23
    elif course_name == 'Machine Learning on AWS sagemaker':
        course_name = 111
    elif course_name == 'Machine Learning on Azure':
        course_name = 112
    elif course_name == 'ML on cloud & AutoMl':
        course_name = 108
    elif course_name == 'Data Science using Python':
        course_name = 67
    elif course_name == 'Hadoop':
        course_name = 94  
    elif course_name == 'Catia and #Dmax and Creo':
        course_name = 41
    elif course_name == 'Networking':
        course_name = 127    
    elif course_name == 'AutoCAD and Catia and Ansys':
        course_name = 25
    elif course_name == 'MasterCAM and Creo and 3Dmax':
        course_name = 118    
    elif course_name == 'Dot not developer':
        course_name = 84
    elif course_name == 'Data Engineering':
        course_name = 57
    elif course_name == 'Data Science job guarantee program':
        course_name = 66
    elif course_name == 'Automotive':
        course_name = 28    
    elif course_name == 'C language':
        course_name = 37    
    elif course_name == 'AWS & DevOps & Linux':
        course_name = 5
    elif course_name == 'SQL & Oracle & PLSQL':
        course_name = 146    
    elif course_name == '3D designing':
        course_name = 1
    elif course_name == 'Enterprise Big Data Professional':
        course_name = 85
    elif course_name == 'Java and Python and Dot Net':
        course_name = 105
    elif course_name == 'Python and DevOps':
        course_name = 140
    elif course_name == 'Python with Django course':
        course_name = 141
    elif course_name == 'Data Science Professional certificate':
        course_name = 63    
    elif course_name == 'SQL':
        course_name = 145
    elif course_name == 'C and C++':
        course_name = 36
    elif course_name == 'Power BI':
        course_name = 134    
    elif course_name == 'CISSP':
        course_name = 40
    elif course_name == 'CC':
        course_name = 38    
    elif course_name == 'Web Design':
        course_name = 156
    elif course_name == 'Microsoft Power BI Data Analytics':
        course_name = 123
    elif course_name == 'Professional Scrum Master Certification':
        course_name = 136
    elif course_name == 'Alibaba Cloud Machine Learning and AI':
        course_name = 15 
    elif course_name == 'Account':
        course_name = 8
    elif course_name == 'Automotion Testing':
        course_name = 26
    elif course_name == 'Fundamentals of Artificial Intelligence':
         course_name = 93    
    elif course_name == 'Philosophy':
        course_name = 133
    elif course_name == 'Introduction to Cyber Security':
        course_name = 101    
    elif course_name == 'Web Development':
        course_name = 157
    elif course_name == 'Cloud Computing':
        course_name = 51
    elif course_name == 'Supply Chain Mangement':
        course_name = 152    
    elif course_name == 'AWS IoT: Developing and Deploying an Internet of Things':
        course_name = 6
    elif course_name == 'Business Analyst':
        course_name = 34    
    elif course_name == 'Additive manufacturing':
        course_name = 9
    elif course_name == 'Digital Art':
        course_name = 83    
    elif course_name == 'DS transformers for NLP':
        course_name = 55
    elif course_name == 'Certification in AI and ML':
        course_name = 42
    elif course_name == 'Data Science with Python':
        course_name = 69
    elif course_name == 'AWS and DevOps':
        course_name = 7
    elif course_name == 'Analyzing and Visualizing Data with Excel':
        course_name = 17    
    elif course_name == 'Professional Scrum Product Owner':
        course_name = 137
    elif course_name == 'Full Ethical Hacking Course':
        course_name = 89    
    elif course_name == 'Machine Learning with Python: A Practical Introduction':
        course_name = 115
    elif course_name == 'Data Science: R Basics':
        course_name = 71
    elif course_name == 'Deep Learning Fundamentals with Keras':
        course_name = 76    
    elif course_name == 'Analyzing Data with Excel':
        course_name = 16
    elif course_name == 'Data Science and Machine Learning Capstone Project':
        course_name = 65
    elif course_name == 'Big data Analytics':
        course_name = 30    
    elif course_name == '100 Days of Code: The Complete Python Pro Bootcamp for 2022':
        course_name = 0
    elif course_name == 'Introduction to Data Analysis using Excel':
        course_name = 102
    elif course_name == 'Feature Engineering for Machine Learning':
        course_name = 87    
    elif course_name == 'Implementation of Data Structures':
        course_name = 98
    elif course_name == 'Shell Programming - A necessity for all Programmers':
        course_name = 149    
    elif course_name == 'Applied BaYesian for Analytics':
        course_name = 21
    elif course_name == 'Foundations of Data Science':
        course_name = 88
    elif course_name == 'Industrial IoT FUndamentals on AWS':
        course_name = 100
    elif course_name == 'Master of Science in data Science':
        course_name = 117    
    elif course_name == 'Master of Science in Computer Science (Specialization in CyberSecurity)':
        course_name = 116
    elif course_name == 'Advanced Certificate in Digital Marketing and Communication':
        course_name = 13    
    elif course_name == 'Implementing and Administrating Cisco Solutions v1.0':
        course_name = 99
    elif course_name == 'DevOps Engineering on AWS':
        course_name = 79
    elif course_name == 'IBM i System Administration':
         course_name = 96
    elif course_name == 'IoT Foundation':
         course_name = 103
    elif course_name == 'Microsoft 365 Mobility and Security':
         course_name = 119
    elif course_name == 'Licensed Penetration Tester':
         course_name = 106
    elif course_name == 'ITIL 4 Foundation':
         course_name = 97
    elif course_name == 'Data Science: Inference and Modeling':
         course_name = 70
    elif course_name == 'POST GRADUATE PROGRAM IN CYBERSECURITY':
         course_name = 131
    elif course_name == 'Certified Information System Security Professional Prep Course':
         course_name = 47
    elif course_name == 'Microsoft Power Automate RPA Developer':
         course_name = 122
    elif course_name == 'Networking in Google Cloud Platform':
         course_name = 128
    elif course_name == 'Certified Information Systems Auditor':
         course_name = 48
    elif course_name == 'Developing Solutions for Microsoft Azure':
         course_name = 81
    elif course_name == 'Professional Agile Leadership - Essentials':
         course_name = 135
    elif course_name == 'Data Protection and Management':
         course_name = 59
    elif course_name == 'CompTIA Cybersecurity Analyst':
         course_name = 52
    elif course_name == 'Certified IoT Security Analyst':
        course_name = 49
    elif course_name == 'Certified Hacking Forensic Investigator v10':
        course_name = 46
    elif course_name == 'Certified Data Centre Expert':
        course_name = 44
    elif course_name == 'Certified Application Security Engineer (CASE) Java':
         course_name = 43
    elif course_name == 'Big Data Foundation':
         course_name = 31
    elif course_name == 'Blockchain Foundation':
         course_name = 33
    elif course_name == 'Automation with Ansible and Ansible Tower':
         course_name = 27
    elif course_name == 'Apache Spark Development':
        course_name = 20
    elif course_name == 'AIX Basics':
        course_name = 3
    elif course_name == 'Microsoft Azure IoT Developer':
        course_name = 120
    elif course_name == 'Administrator Training CDP Private Cloud Base':
        course_name = 12
    elif course_name == 'CEH v11 - Certified Ethical Hacking Course':
        course_name = 39
    elif course_name == 'Deep Learning Course (with Keras & TensorFLow) Certification Training':
         course_name = 75
    elif course_name == 'PROFESSIONAL CERTIFICATION IN SUPPLY CHAIN MANAGEMENT & Analytics':
         course_name = 132
    elif course_name == 'DevOps certification training course':
        course_name = 80
    elif course_name == 'Ansys and Catia and Creo':
        course_name = 19

         
    
    if mode_of_program == 'Online':
        mode_of_program = 2
    elif mode_of_program == 'Both':
        mode_of_program = 0
    elif mode_of_program == 'Offline':
        mode_of_program = 1
        
    
    if Country == 'India':
        Country = 1
    elif Country == 'Malaysia':
        Country = 3
    elif Country == 'USA':
        Country = 5
    elif Country == 'UK':
        Country = 4
    elif Country == 'Australia':
        Country = 0
    elif Country == 'Ireland':
        Country = 2
        
        
    if City == 'Hyderabad':
        City = 10
    elif City == 'Kuala lumpur':
        City = 12
    elif City == 'Bangalore':
        City = 1
    elif City == 'Cheni':
        City = 5
    elif City == 'Pune':
        City = 16
    elif City == 'Madurai':
        City = 13
    elif City == 'Vishakapatnam':
        City = 19
    elif City == 'Vijayawada':
        City = 18
    elif City == 'Mumbai':
        City = 14
    elif City == 'Delhi':
        City = 9
    elif City == 'Gurugram':
        City = 6
    elif City == 'Cambridge':
        City = 4
    elif City == 'Noida':
        City = 15
    elif City == 'Kakida':
        City = 11
    elif City == 'Edinburgh':
        City = 7
    elif City == 'Adelaide':
        City = 0
    elif City == 'Galway':
        City = 8
    elif City == 'San Francisco':
        City = 17
    elif City == 'California':
        City = 3
    elif City == 'Bedford':
        City = 2
        
        
    if certification_provided == 'Yes':
        certification_provided = 1
    elif certification_provided == 'No':
        certification_provided = 0
        
    
    if practice_assignments_included == 'Yes':
        practice_assignments_included = 1
    elif practice_assignments_included == 'No':
        practice_assignments_included = 0
    
    
    if doubt_session == 'Yes':
        doubt_session = 1
    elif doubt_session == 'No':
        doubt_session = 0
        
        
    if internship_provided == 'Yes':
        internship_provided = 1
    elif internship_provided == 'No':
        internship_provided = 0
        
        
    if placement_assistance == 'Yes':
        placement_assistance = 1
    elif placement_assistance == 'No':
        placement_assistance = 0
        
    
    if recorded_videos == 'Yes':
        recorded_videos = 1
    elif recorded_videos == 'No':
        recorded_videos = 0
        
        
    if trainer_grade == 'High':
        trainer_grade = 0
    elif trainer_grade == 'Medium':
        trainer_grade = 1
    else:
        trainer_grade = 2
        
    
    predict_cost = model.predict(pd.DataFrame([[institute, course_name, mode_of_program, course_duration, Country, City,
                     certification_provided, practice_assignments_included, doubt_session, 
                    internship_provided, course_rating, placement_assistance, recorded_videos, trainer_grade]]))
    return predict_cost


def main():
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Price Prediction of an EdTech Product </h1> 
    </div> 
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    institute = st.selectbox('Institute Name', [
        'TraiNocate', 'Iverson', '360DigiTMG', 'Mindasys', 'Simplilearn', 'Qspyders', 'Udemy',
        'Besant technologies', 'IMARTICUS Learning', 'Velocity', 'IBM', 'Datamines Global Institute for Data Science',
        'UpGrad', 'Diksha', 'ACTE', 'Cisco', 'Coursera', 'Harvard University','ExcelR', 'Resh I Technologies', 'Siptech', 'Codegn', 'DeepNeuron',
        'BEPEC', 'Data Pro', 'Pace Institute', 'Pincle', 'Livewire Institute', 'Internshala', 'ACE training', 'Techsutra', 'Rahitech', 'NPTEL',
        'Innomatics Research Labs', 'III Bombay', 'IIMBx', 'Microsoft', 'Scaler', 'AWS', 'Edureka', 'Social Prachar', 'Palle Technologies',
        'Institute of Industrial Design', 'GIT Solutions', 'Shri Shiridi sai institute', 'Dreams Media Solutions', 'Lucid IT solutions', 'Sandsya Institute',
        'Sulekha Institute', 'Prime Classes', 'SV Trainings', 'Alison', 'Elearn InfoTech', 'ISC', 'Great Learning', 'Newsion','Fabtech','AdelaideX', 'Digital Nest', 'Valaxy Tech',
        'Aditi Digital Solution', 'JSpyders', 'Skillslash learn', 'Miles Education', 'DV Analytics',
        'The IOT academy', 'Uptop education', 'Zenclassofficial', 'JanBask Training', 'Edubridge Learn',
        'Nuclearnedu', 'Pantech', 'Almabetter', 'NIIT', 'TalentSprint','FITA Academy', 'Softlogic Systems', 'Tutedude', 'Edupraj', 'Credo Systemz', 'CloudyML',
        'Gutsy', 'Cloud X lab', 'Thriyam'])
    
    course_name = st.selectbox('Course Name', [
    'Data Science', 'Python', 'Data Analytics', 'Software Development', 'Full stack Development',
    'Software Testing', 'Data Science Masters Program', 'AutoCAD', 'Tableau', 'Data Science with ML',
    'C Programming', 'Agile Project Management Foundation', 'IBM Certified Data Science', 'Testing Selenium',
    'Deep Learning', 'Certified Data Science Course', 'Machine Learning with Python', 'Full Stack Java',
    'Data Science and AI', 'Java', 'Artificial Intelligence', 'Machine Learning', 'PHP Security', 'Salesforce',
    'Designing and implementing Microsoft DevOps solutions', 'Salesforce CRM training', 'Core Java',
    'Microsoft Information Protection Administrator', 'Data Mining with Python', 'Red Hat System Administration',
    'AI Career Transition Program', 'Administrating Windows Server Hybrid Core Infrastructure',
    'Data Science Career Transition Program', 'Full Stack Data Science Course', 'Designing Cisco Enterprise Networks v1.1',
    'MSBI', 'Python and Data Science FullStack', 'Android Security Essentials', 'Linux System Engineer',
    'Big Data Hadoop Training', 'Administration of IBM WebSphere DataPower Gateway V7', 'Certified Visual Analytics Expert Training',
    'Oracle Big Data Fundamentals Ed 1', 'AWS', 'Crisis Communication Manager', 'Network Installation,Configuration and Administration',
    'Azure DevOps', 'SAN Management', 'Python with ML', 'MYSQL 5.7 for Database Administrators',
    'MYSQL 8.0 Fundamentals', 'Developing on AWS', 'The Complete 2022 Web Development Course - Build 15 Projects',
    'Web Development with Python and Django', 'Machine Learning on GCP', 'Data Visualization using Tableau',
    'Data visualization Using Power BI training', 'Executive programme in Full stack Data Science',
    'Artificial Intelligence & Deep Learning courses training', 'Machine Learning on AWS sagemaker',
    'Machine Learning on Azure', 'ML on cloud & AutoMl', 'Data Science using Python', 'Hadoop', 'Catia and #Dmax and Creo',
    'Networking', 'AutoCAD and Catia and Ansys', 'MasterCAM and Creo and 3Dmax', 'Dot not developer',
    'Data Engineering', 'Data Science job guarantee program', 'Automotive', 'C language', 'AWS & DevOps & Linux',
    'SQL & Oracle & PLSQL', '3D designing', 'Enterprise Big Data Professional', 'Java and Python and Dot Net',
    'Python and DevOps', 'Python with Django course', 'Data Science Professional certificate', 'SQL',
    'C and C++', 'Power BI', 'CISSP', 'CC', 'Web Design', 'Microsoft Power BI Data Analytics',
    'Professional Scrum Master Certification', 'Alibaba Cloud Machine Learning and AI', 'Account', 'Automotion Testing',
    'Fundamentals of Artificial Intelligence', 'Philosophy', 'Introduction to Cyber Security', 'Web Development',
    'Cloud Computing', 'Supply Chain Mangement', 'AWS IoT, Developing and Deploying an Internet of Things',
    'Business Analyst', 'Additive manufacturing', 'Digital Art', 'DS transformers for NLP', 'Certification in AI and ML',
    'Data Science with Python', 'AWS and DevOps', 'Analyzing and Visualizing Data with Excel',
    'Professional Scrum Product Owner', 'Full Ethical Hacking Course', 'Machine Learning with Python, A Practical Introduction',
    'Data Science, R Basics', 'Deep Learning Fundamentals with Keras', 'Analyzing Data with Excel',
    'Data Science and Machine Learning Capstone Project', 'Big data Analytics', '100 Days of Code, The Complete Python Pro Bootcamp for 2022',
    'Introduction to Data Analysis using Excel', 'Feature Engineering for Machine Learning', 'Implementation of Data Structures',
    'Shell Programming - A necessity for all Programmers', 'Applied BaYesian for Analytics', 'Foundations of Data Science',
    'Industrial IoT FUndamentals on AWS', 'Master of Science in data Science', 'Master of Science in Computer Science (Specialization in CyberSecurity)',
    'Advanced Certificate in Digital Marketing and Communication', 'Implementing and Administrating Cisco Solutions v1.0',
    'DevOps Engineering on AWS', 'IBM i System Administration', 'IoT Foundation', 'Microsoft 365 Mobility and Security',
    'Licensed Penetration Tester', 'ITIL 4 Foundation', 'Data Science, Inference and Modeling',
    'POST GRADUATE PROGRAM IN CYBERSECURITY', 'Certified Information System Security Professional Prep Course',
    'Microsoft Power Automate RPA Developer', 'Networking in Google Cloud Platform', 'Certified Information Systems Auditor',
    'Developing Solutions for Microsoft Azure', 'Professional Agile Leadership - Essentials', 'Data Protection and Management',
    'CompTIA Cybersecurity Analyst', 'Certified IoT Security Analyst', 'Certified Hacking Forensic Investigator v10',
    'Certified Data Centre Expert', 'Certified Application Security Engineer (CASE) Java', 'Big Data Foundation',
    'Blockchain Foundation', 'Automation with Ansible and Ansible Tower', 'Apache Spark Development',
    'AIX Basics', 'Microsoft Azure IoT Developer', 'Administrator Training CDP Private Cloud Base',
    'CEH v11 - Certified Ethical Hacking Course', 'Deep Learning Course (with Keras & TensorFLow) Certification Training',
    'PROFESSIONAL CERTIFICATION IN SUPPLY CHAIN MANAGEMENT & Analytics', 'DevOps certification training course',
    'Ansys and Catia and Creo'])
    
    mode_of_program = st.selectbox('Mode of program', ['Online','Offline','Both'])
    
    course_duration = st.slider('Course duration', 1, 200)
    
    Country = st.selectbox('Country', ['India', 'Malaysia', 'USA', 'UK', 'Australia', 'Ireland'])
    
    City = st.selectbox('City', ['Hyderabad', 'Kuala lumpur', 'Bangalore', 'Cheni', 'Pune', 'Madurai', 'Vishakapatnam', 'Vijayawada',
    'Mumbai', 'Delhi', 'Gurugram', 'Cambridge', 'Noida', 'Kakida', 'Edinburgh', 'Adelaide',
    'Galway', 'San Francisco', 'California', 'Bedford'])
    
    certification_provided = st.selectbox('Certification provided', ['Yes', 'No'])
    
    practice_assignments_included = st.selectbox('Practice Assignments Provided', ['Yes', 'No'])
    
    doubt_session = st.selectbox('Doubt sessions',['Yes', 'No'])
    
    internship_provided = st.selectbox('Internship provided', ['Yes', 'No'])
    
    course_rating = st.slider('Course Rating', 1, 5)
    
    placement_assistance = st.selectbox('Placement Assistance', ['Yes', 'No'])
    
    recorded_videos = st.selectbox('Recorded Videos', ['Yes', 'No'])
    
    trainer_grade = st.selectbox('Trainer Grade', ['Low', 'Medium', 'High'])
    
    result = ""
    
    if st.button('Price'):
        result = predict_cost(institute, course_name, mode_of_program, course_duration, Country, City,
            certification_provided, practice_assignments_included, doubt_session, 
            internship_provided, course_rating, placement_assistance, recorded_videos, trainer_grade)
        
        st.success(f'The Predicted price of the course is {result[0]:.0f} INR')
   
if __name__ == '__main__':
    main()
