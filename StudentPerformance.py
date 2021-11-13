import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random

student_result=[]
for i in range(0,1000):
    test_preparation_course= random.randint(1,100)
   
    student_result.append(test_preparation_course)

mean = statistics.mean(student_result)
median = statistics.median(student_result)
mode = statistics.median(student_result)

print("mean , median and mode of student's result are {} ,{} and {} respectively".format(mean,median,mode))

std = statistics.stdev(student_result)
print(std)

#finding the 3 standard deviation intervals
first_std_start,first_std_end = mean-std,mean+std



data_within_first_std = [result for result in student_result if result > first_std_start and result < first_std_end]


print("{}% of data lies within first standard deviation".format(len(data_within_first_std)*100/len(student_result)))
