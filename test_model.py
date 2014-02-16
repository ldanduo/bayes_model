#!/usr/bin/env python
#-*-conding:utf-8
import os
import sys
import pdb
from numpy import *

from bayes_model import *

def main():
    if len(sys.argv) != 5:
        print "Usage [%s] [train] [test] [model] [result]" % (sys.argv[0])
        sys.exit(0)

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    model_file = sys.argv[3]
    result_file = sys.argv[4]

    modelfp = file(model_file,"w")
    resultfp = file(result_file,"w")

    news_list,news_class = loadData(sys.argv[1])
    doc_size = len(news_list)

    wordSet = createVocabList(news_list)

    trainMat = []
    count = 0
    for document in news_list:
        if count % 100 == 0:print count
        count += 1
        trainMat.append(setOfWords2Vec(wordSet,document))
    a,b,c,d,e,f = trainNB(trainMat,news_class)
    print >> modelfp,"pauto = %f,pbusiness = %f,psport = %f" % (d,e,f)

    word_size = len(wordSet)
    for i in range(word_size):
        print >> modelfp,"%s\t%f\t%f\t%f" % (wordSet[i],a[i],b[i],c[i])

    doc_size = 0
    true_count = 0
    for doc in file(test_file):
        if not doc:continue
        array = doc.strip().split("\t")
        subarray = array[0].split(" ")
        doc_class = array[1]
        test_list = setOfWords2Vec(wordSet, subarray)
        result = classifyNB(test_list,a,b,c,d,e,f)
        if doc_class == result:
            true_count += 1
        else:
            print >> resultfp,doc.strip()
            print >> resultfp,"[ERROR] true = %s ### result = %s" % (doc_class,result)
        print >> resultfp,"true = %s ### result = %s" % (doc_class,result)
        doc_size += 1
    print >> resultfp,"the accurency is %f " % (1.0 * true_count / doc_size)

    #test_size = len(test_list)
    #true_count = 0
    #for i in range(test_size):
    #    test_vec = setOfWords2Vec(wordSet, test_list[i])
    #    result = classifyNB(test_vec,a,b,c,d,e,f)
    #    if test_class[i] == result:
    #        true_count += 1
    #    print "true = %s ### result = %s" % (test_class[i],result)
    #print "the accurency is %f " % (1.0 * true_count / test_size)
    modelfp.close()
    resultfp.close()
if __name__ == "__main__":
    main()


