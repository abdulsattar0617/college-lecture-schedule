from datetime import datetime 
import calendar
import sys 

lectureTime = [
        ['0','0'],   # lecture start at 0, end at 1 (index)
        ['12:00','12:50'] , 
        ['12:50', '1:40'], 
        ['1:40', '2:30'],
        ['2:30', '3:20'], 
        ['3:20', '5:20'] 
        ]  

subjectWithCode = [ 
    ['###','Environment'],    
    ['501', 'Windows Programming'],
    ['502', 'Python'],
    ['503', 'Data Science'],
    ['504B', 'Basics of Linux'],
    ['505B', 'System Analysis & Design (SAD)'],
    ['506', 'Windows Programming'],
    ['507', 'Python'] 
] 

def returnLecture(presentDay):
    global lectureTime
    global subjectWithCode 
    # at index 0 --> subject code, at index 1 --> subject
    lecture1 = ['---', "No lecture"]  
    lecture2 = ['---', "No lecture"] 
    lecture3 = ['---', "No lecture"] 
    lecture4 = ['---', "No lecture"] 

    practical = ['---', "No Practical"]

    heading = calendar.day_name[presentDay] 
    
    match presentDay:
        case 0:
            # heading = "Monday"
            lecture1 = subjectWithCode[5] 
            lecture2 = subjectWithCode[4] 
            lecture3 = subjectWithCode[1]
            lecture4 = subjectWithCode[1]
            
        case 1:
            # heading = "Tuesday" 
            lecture1 = subjectWithCode[5] 
            lecture2 = subjectWithCode[4] 
            lecture3 = subjectWithCode[1]
            lecture4 = subjectWithCode[2]

        case 2:
            # heading = "Wednesday" 
            lecture1 = subjectWithCode[5] 
            lecture2 = subjectWithCode[4] 
            lecture3 = subjectWithCode[1]
            lecture4 = subjectWithCode[3] 

        case 3:
            # heading = "Thursday"
            lecture1 = subjectWithCode[2]  
            lecture2 = subjectWithCode[3] 
            lecture3 = subjectWithCode[0] # env
            # lecture4 = "No lecture" # don't need it, since it is already initialized with it.
            
        
        case 4: # friday 
            # heading = "Friday"
            lecture1 = subjectWithCode[2] 
            lecture2 = subjectWithCode[3] 
            lecture3 = subjectWithCode[0] 
            lecture4 = subjectWithCode[5] 
            practical = subjectWithCode[6] 
        
        case 5: # saturday 
            # heading = "Saturday"
            lecture1 = subjectWithCode[2] 
            lecture2 = subjectWithCode[3] 
            lecture3 = subjectWithCode[0] 
            lecture4 = subjectWithCode[4]  
            practical = subjectWithCode[7] 
        
        case 6:
            pass 

        case _ :
            raise Exception("Error: Invalid Day !\nThe day can be in between 0 & 6.")
        
    return [lecture1,lecture2,lecture3,lecture4, practical] 

if __name__ == "__main__":
    print("Library methods for main app.")