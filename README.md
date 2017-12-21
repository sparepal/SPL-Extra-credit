
Intro:
Given a file written by the Twitter.py,
the functions in EC.py will read and organize the information in that file. 
There are function definitions to:

i) Return the top 'n' users who have tweeted the most related to the search
	string for the entire timeline. 'n' is provided by the user and can be
	any positive integer.

ii) Return the top 'n' users who have tweeted the most for every hour. The function
	written to do this will do this for every our as defined by the timeline specified
	in and returned by Twitter.py.

iii) Return the top 'n' users who have the maximum followers.

iv) Return the top 'n' tweets which have the maximum retweet count.

This was accomplished, primarily, by making use of Python 3's built-in 
List and Dictionary structures. 

Instruction:
EC.py is compatible with Python 3. There are four independent functions contained within
that will interact with a .txt file written by the provided Twitter.py. As such, each function
asks the user to specify a file to open. As currently written, this path must include the entire
path EXCEPT for the .txt file-type written at the end of the path. For example, if the file
the user wishes to open is named "data.txt" and is located in "C:\Users\documents", the 
user should enter "C:\Users\documents\data" when prompted for the file.

Additionally, EC.py will ask the user to specify a file to write the information organized
by the function to. This file can be named whatever the user desires and will be saved to the
folder in which EC.py is currently located.

NOTE: Even though the file written by Twitter.py was encoded as 'utf-8', EC.py was not
able to read it with encoding specified as 'utf-8'. When opening, the encoding had to be specified
as 'latin-1' in order for the file to be read without error.

To run the seperate functions on a file, the user must uncomment the function calls located at
the bottom of the file on lines 138, 139, 140, 141, and execute the program.

i) To write the top 'n' users who have tweeted the the most, uncomment "topNusersTotal()" on line 138.
ii) To write the top 'n' users who have tweeted the most per hour, uncomment "topNusersPerHourr()" on line 139.
iii) to write the top 'n' users who have the maximum followers, uncomment "maximumFollowers()" on line 140.
iv) To write the top 'n' tweets which have the maximum retweet count, uncomment "maximumRetweet()" on line 141.

