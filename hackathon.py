import sqlite3 as sql


def createProfiles(): # type=professor/module
    pass


def createUser():  #All students
    pass


def createRatings():
    pass


def createComments():
    pass


def getUser(userID):
    users=sql.connect("userData.db") #Stores username and userID


def getRatings(profileID,userID,rating):
    ratings=sql.connect("userRatings.db") #receiveID for the entity that received the rating, userID for the rater and the rating associated


def getComments(comment,userID,profileID):
    comments=sql.connect("userComments.db") #Stores comment, userID and receiveID


def addUser(username):
    users=sql.connect("userData.db")


def addRating(profileID,userID,rating):
    ratings=sql.connect("userRatings.db")


def addComment(profileID, userID, comment):
    comments=sql.connect("userComments.db")

addComment(1,2,3)