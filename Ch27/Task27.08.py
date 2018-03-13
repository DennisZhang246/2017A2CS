#S3C3 Dennis
#Task 27.08

class Assessments:
   def __init__(self, t, m):
      self.__AssessmentTitle = t
      self.__MaxMarks = m
   def OutputAssessmentDetails(self):
      print(self.__AssessmentTitle, "Your Grade is",self.__MaxMarks)
      
class Course:
   def __init__(self, t, m): 
      self.__CourseTitle = t
      self.__MaxStudents = m
      self.__NumberOfLessons = 0
      self.__CourseLesson = []
      self.__CourseAssessment = Assessment

   def AddLesson(self, t, d, r):
      self.__NumberOfLessons = self.__NumberOfLessons + 1
      self.__CourseLesson.append(Lesson(t, d, r))
      
   def AddAssessment(self, t, m):
      CourseAssessment = Assessment(t, m)
      
   def OutputCourseDetails(self):
      print(self.__CourseTitle, end=' ')
      print( "Maximum number of students: ",self.__MaxStudents)
      for i in range(self.__NumberOfLessons):
          print(self.__CourseLesson[i].OutputLessonDetails())
          
class Lesson:
   def __init__(self, t, d, r):
      self.__LessonTitle = t
      self.__DurationMinutes = d
      self.__requiresLab = r
   def OutputLessonDetails(self):
      print(self.__LessonTitle,self.__DurationMinutes)

def Main():#From textbook
    MyCourse = Course("Computing", 10) # sets up a new course
    MyCourse.AddAssessments("Programming", 100) # adds an assignment
    # add 3 lessons
    MyCourse.AddLesson("Problem Solving", 60, False)
    MyCourse.AddLesson (" Programming" , 120, True )
    MyCourse.AddLesson("Theory", 60, False)
    # check it all works MyCourse.OutputCourseDetails()
    
