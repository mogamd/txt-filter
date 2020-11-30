from collections import Counter

#=====================================================================================

    # This Algorithm will scan a .txt file that a user will select. It will filter
    # out the data it is provided with (example: {1,1,2,3,1,1,3,3,3,3,3,1,2}) and 
    # omit data sets which does not meet the requirments. It will then create a new
    # .txt file with the remaining data that has passed the necessary requirements

#=====================================================================================





# The txt file has to be within the same folder as this Algorithim 
# You can change the name of the txt file by changing the name of it within
# the parenthesis (brackets): 
# NB only change the name within the commas ('NAME'.txt) 
# The name always needs to end with .txt

# This selects the txt_file.
txt_file = open('ones.txt')


#=====================================================================================

    #We need to organise the data for our Algo to interperate it

#=========================================================================================


#This does some stuff in order Python to read the data on the text file. 
#!!! DO NOT MAKE ANY CHANGES TO THIS CODE !!!
data = txt_file.read()
new_data = (data.split(' '))
total_data_sets = len(new_data) #This gets the amount of data sets within the text file

print('The total amount of Datasets within the Text file is: ' + str(total_data_sets))

#This will be the final Data for the Algo to work with
txtData = []




#This slices through all of the data sets and cuts out the {} and appends the data to
#txtData
for i in range(total_data_sets):
    txtData.append(new_data[i][1:26])

    #USED FOR TROUBLESHOOTING:
    #print(txtData[i])
    #print(txtData[i][12:13])

#USED FOR TROUBLESHOOTING:
#print(len(txtData))

#=========================================================================================

    #Now we need to ad the data into a class so we can reference self.

#=========================================================================================

class Data:
    def __init__(self, data):
        self.data = data

ClassData = Data(txtData[0:total_data_sets])

#Used for trouble shooting purposes:
#print(ClassData.data[total_data_sets-3])

FinalData = ClassData.data

'''
for index, item in enumerate(FinalData):
    print(item, index)
'''

#=========================================================================================

    #We need to count how many times a number repeats itself within a Dataset

#=========================================================================================

# This is the variables we will be needing:
a = '1'
b = '2'
c = '3'

# These are the functions that counts how many times a number repeats itself within the data

def count1(list, a): 
    count = 0
    for element in list: 
        if (element == a): 
            count = count + 1
    return count 

def count2(list, b): 
    count = 0
    for element in list: 
        if (element == b): 
            count = count + 1
    return count 

def count3(list, c): 
    count = 0
    for element in list: 
        if (element == c): 
            count = count + 1
    return count 

#=========================================================================================

# Driver Code 

Data1 = []
Data2 = []
Data3 = []
Data4 = []
Data5 = []
Data6 = []
Data7 = []
Data8 = []
Data9 = []
Data10 = []

newTxTdata = []


def DataFilter():
    

    for index, item in enumerate(FinalData):
        

        a = '1'
        b = '2'
        c = '3'

        list = FinalData[index]
        
        #we assign variables to the amout of times a number repeats itself
        #in order to use with booleans for our rules
        one = count1(list, a) #So the varaible 'one' = amount of times one is counted in a dataset
        two = count2(list, b) #So the varaible 'two' = amount of times one is counted in a dataset
        three = count3(list, c) #So the varaible 'three' = amount of times one is counted in a dataset

        #Used for trouble shooting purposes:
        #print('{} has occurred {} times'.format(a, count3(list, a)))
        
        
        #=================================
        element3 = item[4:5]
        element4 = item[6:7]
        element5 = item[8:9]
        element6 = item[10:11]
        element7 = item[12:13]
        element8 = item[14:15]
        element9 = item[16:17]
        element10 = item[18:19]
        element11 = item[20:21]
        element12 = item[22:23]
        element13 = item[24:25]
        #=================================


        #=====================================================================================
        
        #Lets get started with the applying the rules:

        #=====================================================================================
        

        
        #Rule 1: 
        #A set should contain 3-7 ones (1’s) meaning all sets 
        #with less than 3 (1’s) or more than 7 (ones) must be 
        #omitted regardless of the position of the e.g. 
        if one >= 3 and one <= 6:
            #print('There are a total of:' + str(one) +' 1s')
            #print('This dataset passed rule 1', FinalData.pop(index), 'There are a total of:' + str(one) + ' 1s'  )
            
            #Adds the data to a new variable:
            Data1.append(FinalData.pop(index))
        
        #==================================================================================================

        for index, item in enumerate(Data1):

        
            #Rule 2:  
            #All sets must contain 1-6 two’s (2) all sets that contain more 
            #than 6 twos’ (2) must be omitted e.g. sets that do not contain any 
            #two’s must be omitted
            
            if two >= 1 and two <= 6:
                #print('This Dataset passed rule 2:', FinalData.pop(index), 'There are a total of:' + str(two) + ' 2s' )
               
                #Adds the data to a new variable:
                Data2.append(Data1.pop(index))
        
        #==================================================================================================

        for index, item in enumerate(Data2):

            #Rule 3:
            #All sets must contain 2-7 three’s meaning all sets with less than
            #less than two three’s (3) or more than 7 threes’ must be omitted e.g.
            
            if three >= 2 and three <= 7:
                #print('This dataset passed rule 3: ', FinalData.pop(index), 'There are a total of:' + str(three) + ' 3s'  )
                
                #Adds the data to a new variable:
                Data3.append(Data2.pop(index))
        
        
        #==================================================================================================
        
        for index, item in enumerate(Data3):
        
            #Rule 4:
            #Sets that contain 3 consecutive 1s on position 5-7 needs to be omited

            if element5 =='1' and element6 =='1' and element7 == '1':
                #print('Rule 4 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data3.pop(index)

            else:
                #Adds the data to a new variable:
                Data4.append(Data3.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data4):

            #Rule 5:
            #Sets that contain 3 consecutive 2s on position 5-7 needs to be omited

            if element5 =='2' and element6 =='2' and element7 == '2':
                #print('Rule 5 has been applied, Dataset Omited: ',  FinalData.pop(index) )
                Data4.pop(index)

            else:
                #Adds the data to a new variable:
                Data5.append(Data4.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data5):

        #Rule 6:
        #Sets that contain 3 consecutive 3s on position 5-7 needs to be omited
        
            if element5 =='3' and element6 =='3' and element7 == '3':
                #print('Rule 6 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data5.pop(index)

            else:
                #Adds the data to a new variable:
                Data6.append(Data5.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data6):

            #Rule 7:
            #Sets that contain 3 consecutive 2s on position 8-10 needs to be omited
            
            if element8 =='2' and element9 =='2' and element10 =='2':
                #print('Rule 7 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data6.pop(index)

            else:
                #Adds the data to a new variable:
                Data7.append(Data6.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data7):

            #Rule 8:
            #Sets that contain 3 consecutive 3's on position 8-10 must be omited

            if element8 == '3' and element9 =='3' and element10 =='3':
                #print('Rule 8 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data7.pop(index)

            else:
                #Adds the data to a new variable:
                Data8.append(Data7.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data8):

            #Rule 9:
            #All sets that contain 3 consecutive 2s on 11-13 must be omited
            if element11 =='2' and element12 =='2' and element13 =='2':
                #print('Rule 9 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data8.pop(index)

            else:
                #Adds the data to a new variable:
                Data9.append(Data8.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data9):

            #Rule 10:
            #Sets that contain 3 consecitive 1s on position 3-5 must be omited
            if element3 =='1' and element4 =='1' and element5 =='1':
                #print('Rule 10 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data9.pop(index)

            else:
                #Adds the data to a new variable:
                Data10.append(Data9.pop(index))

        #==================================================================================================

        for index, item in enumerate(Data10):

            #Rule 11:
            #All sets without 1 from position 8-13 must be omited
            if element8 != '1' and element9 != '1' and element10 != '1' and element11 !='1' and element12 !='1' and element13 !='1':
                #print('Rule 11 has been applied, Dataset Omited: ', FinalData.pop(index) )
                Data10.pop(index)
    
            else:
                newTxTdata.append(Data10.pop(index))
                #print('Passed Requirements, will keep this dataset: ', newTxTdata.pop(index) )
                #print('There are a total of:' + str(one) +' 1s')
                

        #==================================================================================================

        



#==================================================================================================


#6. Once all of the rules has been applied we need to store it and create a new txt file


#==================================================================================================
    

def main():
    DataFilter()

    newTxTdatalength = len(newTxTdata)


    print("New Total Data: ",len(newTxTdata))

    #This creates a new files:
    f= open("New.txt","w+")

    for i in range(newTxTdatalength):
        f.write('{'+ newTxTdata[i] + '}')

    f.close()

main()


#==================================================================================================

# Notes... 
# Booleans does not seem to be appying correclty 
# thus the filter method is not working. I think 
# I need to layer the filter methods 
# so each rule filters through the entire list 

#===========================================###
#Billing Information:                       ###
project_rate = 350                          ###
TimeOnProject = 18                          ###                              
total_pay = project_rate * TimeOnProject    ###
#print(total_pay)                           ###
#===========================================###