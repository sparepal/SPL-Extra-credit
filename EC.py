import string
import operator
import sys
def topNusersTotal():
    SEARCH = input("Enter the file path: ")
    INPUT_FILE_PATH = SEARCH+ '.txt'
    SEARCH2 = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = './' + SEARCH2 + '.txt'
    n = int(input("Enter how many users you would like to return information on: "))
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()
    d = {}
    for elem in data:
        #print(elem)
        tempList = elem.split()
        if tempList[0] in d:
            d[tempList[0]] +=1
        else:
            d[tempList[0]] = 1
    d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    #print(d[0])
    newFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    newFile.write("The top n = " + str(n) + " users who have tweeted the most related to the search string for the entire timeline: \n")
    for x in range (0,n):
        newFile.write("The user " + d[x][0] + " tweeted " + str(d[x][1]) + " times" + "\n")
        #print("The user " + d[x][0] + "has tweeted " + str(d[x][1]) + " times")
    newFile.close

def topNusersPerHour():
    SEARCH = input("Enter the file path: ")
    INPUT_FILE_PATH = SEARCH+ '.txt'
    SEARCH2 = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = './' + SEARCH2 + '.txt'
    n = int(input("Enter how many users you would like to return information on: "))
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    #create dictionary containing each use in an hour and the
    #number of times they posted in that hour
    d = {}
    for elem in data:
        tempList = elem.split()
        tempList2 = tempList[1].split(":")
        tempKey = tempList[0] + " " + tempList2[1]
        if tempKey in d:
            d[tempKey]+=1
        else:
            d[tempKey]=1
    d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)

    #get total number of posts per hour recorded
    d2={}
    totalNumPostsInFile = 0
    for elem in d:
        totalNumPostsInFile+=1
        if(elem[0].split()[1]) in d2:
            d2[elem[0].split()[1]]+=1
        else:
            d2[elem[0].split()[1]]=1
    d2 = sorted(d2.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = n*len(d2)
    newFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    #print n top users per hour
    for x in range (0,len(d2)):
        #print("\n")
        nIter = n
        #print ("Top n = " + str(n) + " users and their number of posts per hour in hour = " + d2[x][0])
        newFile.write("\nTop n = " + str(n) + " users and their number of posts per hour in hour = " + d2[x][0] +"\n\n")
        for elem in d:
            if nIter == 0:
                break
            if elem[0].split()[1] == d2[x][0]:
                newFile.write("Hour: " + d2[x][0] + " -- Username: " + elem[0].split()[0] + " -- Number of Posts: " + str(elem[1]) + "\n")
                #print ("Hour: " + d2[x][0] + " -- Username: " + elem[0].split()[0] + " -- Number of Posts: " + str(elem[1]))
                nIter-=1
    newFile.close

            
def maximumFollowers():
    SEARCH = input("Enter the file path: ")
    INPUT_FILE_PATH = SEARCH+ '.txt'
    SEARCH2 = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = './' + SEARCH2 + '.txt'
    n = int(input("Enter how many users you would like to return information on: "))
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    d = {}
    for elem in data:
        tempList = elem.split()
        if tempList[0] not in d:
            d[tempList[0]] = int(tempList[-2])

    d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    newFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    newFile.write("The top n = " + str(n) + " users who have the maximum followers: " + "\n\n")
    #print("The top n = " + str(n) + " users who have the maximum followers: ")
    for x in range (0, n):
        newFile.write(str(x+1) + ". Username: " + d[x][0] + " -- Number of Followers: " + str(d[x][1]) + "\n\n")
        #print (str(x+1) + ". Username: " + d[x][0] + " -- Number of Followers: " + str(d[x][1]))
    newFile.close
        
        
def maximumRetweet():
    SEARCH = input("Enter the file read path: ")
    INPUT_FILE_PATH = SEARCH+ '.txt'
    SEARCH2 = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = './' + SEARCH2 + '.txt'
    n = int(input("Enter how many users you would like to return information on: "))
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    d = {}
    for elem in data:
        #print (elem)
        tempList = elem.split()
        y = len(tempList)-2
        tempTweet = "\""
        for x in range (4, y):
            tempTweet += tempList[x] + " "
        tempTweet += " ::::;:::: " + tempList[0]
        #print(tempTweet)
        if tempTweet not in d:
            d[tempTweet] = int(tempList[-1])

    newFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    d = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    newFile.write("The top n = " + str(n) + " tweets that have the maximum retweets: " +"\n\n")
    #print("The top n = " + str(n) + " tweets that have the maximum retweets: ")
    for x in range (0, n):
        newFile.write(str(x+1) + ". Username: " + d[x][0].split()[-1] + "\n -- Tweet: " +
                      d[x][0].split("::::;::::")[0] + "\n -- Number of retweets: " + str(d[x][1]) + "\n\n")
        #print (str(x+1) + ". Username: " + d[x][0].split()[-1] + "\n -- Tweet: " +
               #d[x][0].split("::::;::::")[0] + "\n -- Number of retweets: " + str(d[x][1]))
    newFile.close

topNusersTotal()
#topNusersPerHour()
#maximumFollowers()
#maximumRetweet()
        

