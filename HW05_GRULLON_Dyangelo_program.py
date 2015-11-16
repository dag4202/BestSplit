"""
Author: Dyangelo Grullon
Professor: Thomas Kinsman
Course: Principles of Data Mining
Assignment: HW05 - Decision Trees 01
"""
from math import log, exp

def getSplit(attribute, data):
    split = {} #lets make a dictionary where the keys are the value of an attribute in any data point
    for instance in data: # for every object in a data array
        attributeValue = instance[attribute] # lets grab the value of the attribute of the object 
        if attributeValue not in split: #if the value grabbed is not in the dictionary
            split[attributeValue] = [] #lets go ahead and make an empty array to add all objects that have the same attribute value
        split[attributeValue].append(instance) #lets go ahead and append that object to the array (with the attribute value as the key)
    return split # We will need this later

def getData(filename): #lets encapsulate the data into a data structure
    dataFile = open(filename) #first we gotta open the file
    attributes = dataFile.readline().split() #know what? lets assume every file has tab-delimited attribute names on the first line
    data= [] #yeaaaah, we don't need anything more complicated than an array to compute the values we need
    for line in dataFile: #for every line in the datafile (hey...you said prolific professor :))
        instance = line.split() #lets get dem values in an array without spaces
        data.append(instance) #object encapsulated, time to add this beauty in the data array
    dataFile.close() #I guess this doesn't really matter, but hey, you never know. Might as well close the file
    return (data,attributes) #Lets return both the list of attributes (in string form) and the array of objects(held in an array of strings)

def findValues(attribute, target, data):#Okay, its time to find the entropy and yada yada
    jSplit = getSplit(attribute, data) #First lets split the data array into subarrays of data objects that only have a specific attribute value per array
                                        #lets call this attribute j and the target t
    mixedEntropy = 0 
    mixedGini = 0
    misclassE = 0
    length = float(len(data)) #this is the amount of data points that we're evaluating
    for attributeValue in jSplit.keys(): #for every variation of the attribute value we're finding the values for
        tSplit = getSplit(target, jSplit[attributeValue]) #lets go ahead and split the subarrays into smaller subarrays that only contain specific
                                                            #attribute target attribute values per array
        singleEntropy = 0
        singleGini = 0
        Pj = len(jSplit[attributeValue])/ length #this is the percentage of the objects that have the particular attribute value in the iteration (out of all data values)
        maxP = 0
        for targetValue in tSplit.keys(): #for every value in the subarray containing data objects with the case j & t 
            PtGj = len(tSplit[targetValue])/float(len(jSplit[attributeValue])) #lets go ahead and find the percentage of t given j
            singleEntropy += PtGj * (-log(PtGj,2)) #entropy formula without standardization
            singleGini += PtGj * PtGj #Gini formula without standardization
            if PtGj > maxP: #hey, is this percentage the highest percentage of t given j
                maxP = PtGj #no? well, lets change that
        misclassE += Pj * (1-maxP) #lets standardize our max percentage value with Pj and add it to the misclassification error
        mixedGini += Pj * (1-singleGini) #do the same to the Gini
        mixedEntropy += Pj * singleEntropy #and might as well do it to the entropy too.
    return [mixedEntropy, mixedGini, misclassE] # I figured I didn't want my computer to do this work 3 times, so I returned all 3 in one go. 

def computeAll():
    attribute = int(input('Provide the first attribute number to check: ' )) - 1 #get the first attribute number, so as to use it as an index
    last = int(input('Provide the last attribute number to check: ')) - 1  #get the last attribute number to check
    target = int(input('Provide the target attribute number: ')) - 1 #get the target attribute number
    encapsulated = getData('VHCLS_speeders_by_attributes_v042.txt') #encapsulate the data file, if you'd like, change the file name (make sure it has the same format)
    data = encapsulated[0] #grab the data array
    attributes = encapsulated[1] #grab the attributes array (told you we'd need it)
    bestEntropy = None #initialize to none for easy if statements
    bestGINI = None
    bestError = None
    bestEntAttr = None
    bestGINIAttr = None
    bestErrorAttr = None
    print('----------------------------------------------')
    while attribute <= last: #for every attribute within the attributes given
        if(attribute == target): #if its the target attribute, lets go ahead and skip that
            attribute += 1
            continue
        values = findValues(attribute, target, data) #find the values for the attribute we're looking at
        entropy = round(values[0],3) #lets round the entropy value
        GINI = round(values[1], 3) #round the GINI value
        misclass = round(values[2], 3)#round the misclassification error value
        print('Mixed Entropy was ' + str(entropy) + ' for Attribute ' + str(attribute+1)+' ' + attributes[attribute]) #formatted results printed
        print('Mixed Gini was ' + str(GINI) + ' for Attribute ' + str(attribute+1)+' ' + attributes[attribute])
        print('Misclass Error was ' + str(misclass) + ' for Attribute '+ str(attribute+1)+' ' + attributes[attribute])
        print('----------------------------------------------')
        if bestEntropy == None or entropy < bestEntropy: #I know I didn't have to do this, I just got lazy, or not, I don't know. I just did it I guess.
            bestEntropy = entropy #I guess I was just trying to avoid work in the future when I have to make me some decision trees
            bestEntAttr = attributes[attribute]#Now that I think about it, I guess I could use this to make decision trees on the fly. Maybe output some code?
        if bestGINI == None or GINI < bestGINI:#Yeah, I think that'd be nice
            bestGINI = GINI #at this point, the rest is self-explanatory, so if you want to leave, you can. You probably have other things to grade.
            bestGINIAttr = attributes[attribute] #No really, the most you can get out of the rest of this is a slight chuckle. I'm pretty much assuming you've stopped reading my code.
        if bestError == None or misclass < bestError: #If you're still here, I'm warning you that you'll never get these seconds back. Its just more of the same the farther down you go
            bestError = misclass #I am 99 percent sure that you've stopped reading this documentation. If you haven't, read any of the two lines above for guidance.
            bestErrorAttr = attributes[attribute]#99 bottles of beer on the wall, 99 bottles of beer...
        attribute+=1 #take one down, put it back up, 99 bottles of beer on the wall... Oh and this line keeps the loop going. This line of the code.
    print('The best attribute for lowest Entropy, GINI, and misclassifcation error is '+bestEntAttr+', '+bestGINIAttr+' and '+bestErrorAttr+' respectively for target ' + attributes[target])
    return

computeAll()
    
    
        



