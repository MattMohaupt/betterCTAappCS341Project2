#
# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
#-------------------------------------------------------------------------------------------
#Project 2: Chicago Lobbyist Database App
#Data Tier
#Date: 10/16/24
#Course: CS 341, Spring 2024, UIC
#System: Visual Studio Code
#Author: Matthew Mohaupt; mmohau3; 651525023
#Description: a console-based database application in Python using an N-tier design which consists of the data-tier, object-tier and 
#    presentation-tier
#-------------------------------------------------------------------------------------------
import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#
def select_one_row(dbConn, sql, parameters = None):
    dbcursor =dbConn.cursor()
    #use a try and catch block so that if a incorrect sql statement is used then the program wont crash
    try:
        #need to use this if else statement as if we just put the empty parameters as an argument it will throw an error if the command didnt require any parameters
        if(parameters == None):
            dbcursor.execute(sql)
        else:
            dbcursor.execute(sql, parameters)
        row = dbcursor.fetchone()
    except:
        row = ()
    #use finally as no matter what must always close the database connection after using it
    finally:
        dbcursor.close()
    #check to see if what returned was none and a empty tuple must be returned
    if(row == None):
        row = ()
    return row


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    dbcursor =dbConn.cursor()
    #use a try and catch block so that if a incorrect sql statement is used then the program wont crash
    try:
        #need to use this if else statement as if we just put the empty parameters as an argument it will throw an error if the command didnt require any parameters
        if(parameters == None):
            dbcursor.execute(sql)
        else:
            dbcursor.execute(sql, parameters)
        rows = dbcursor.fetchall()
    except Exception as e:
        print("select_n_rows failed: ",e)
        return None
    #use finally as no matter what must always close the database connection after using it
    finally:
        dbcursor.close()
    #check to see if what returned was none and a empty list must be returned
    if(rows == None):
        rows = []
    return rows


##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert", 
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via 
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an 
#          error occurs a msg is output and -1 is 
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g. 
#          because the where condition was false?).
#
def perform_action(dbConn, sql, parameters = None):
    dbcursor =dbConn.cursor()
    #use a try and catch block so that if a incorrect sql statement is used then the program wont crash
    try:
        #need to use this if else statement as if we just put the empty parameters as an argument it will throw an error if the command didnt require any parameters
        if(parameters == None):
            dbcursor.execute(sql)
        else:
            dbcursor.execute(sql, parameters)
        dbConn.commit()
    except Exception as e:
        print("perform_action failed: ", e)
        return -1
    #use finally as no matter what must always close the database connection after using it
    finally:
        dbcursor.close()
    return dbcursor.rowcount