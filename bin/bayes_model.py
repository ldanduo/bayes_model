#!/usr/bin/env python
#-*-conding:utf-8
"created by darrenan 2014:20:07"

import os
import sys
import pdb
from numpy import *

def loadData(data_file):
    news_list = []
    news_class = []
    infp = file(data_file)
    for line in infp:
        line = line.strip()
        array = line.split("\t")
        if len(array) != 2:continue
        subarray = array[0].split(" ")
        news_list.append(subarray)
        news_class.append(array[1])
    infp.close()
    return news_list,news_class

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = +1
        #else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def trainNB(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])

    auto_num = trainCategory.count("auto")
    business_num = trainCategory.count("business")
    sport_num = trainCategory.count("sport")
    doc_num = auto_num + business_num + sport_num

    pAuto = 1.00 * auto_num / doc_num
    pBusiness = 1.00 * business_num / doc_num
    pSport = 1.00 * sport_num / doc_num

    p0Num = 1.00 * ones(numWords)
    p1Num = 1.00 * ones(numWords)
    p2Num = 1.00 * ones(numWords)
    p0Denom = 1.00 * numWords
    p1Denom = 1.00 * numWords
    p2Denom = 1.00 * numWords
    for i in range(numTrainDocs):
        if trainCategory[i] == "auto":
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        if trainCategory[i] == "business":
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        if trainCategory[i] == "sport":
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
    p0Vect = p0Num/p0Denom
    p1Vect = p1Num/p1Denom
    p2Vect = p2Num/p2Denom
    return p0Vect,p1Vect,p2Vect,\
            pAuto,pBusiness,pSport

def classifyNB(vec2Classify, p0Vec, p1Vec, p2Vec,\
                pClass0, pClass1, pClass2):
    p0 = sum(vec2Classify * log(p0Vec)) + log(pClass0)
    p1 = sum(vec2Classify * log(p1Vec)) + log(pClass1)
    p2 = sum(vec2Classify * log(p2Vec)) + log(pClass2)
    if p0 > max(p1,p2):
        return "auto"
    elif p1 > max(p0,p2):
        return "business"
    elif p2> max(p1,p0):
        return "sport"
