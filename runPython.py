import MongoEx
import ElasticIndexing
import ElasticSearching
import ElasticTraining
import ElasticAnalyzer

import pandas as pd


if __name__ == "__main__":
    
    training = ElasticTraining.ElasticTraining()
    #indexing = ElasticIndexing.ElasticIndexing()
    # searching = ElasticSearching.ElasticSearching()
    analyzer = ElasticAnalyzer.ElasticAnalyzer()
    
    scheme = ['ib','tfidf','lmd','lmj','dfr','bm25']
    # indexing.doIndex()


    
    # for s in scheme:
    #     for i in range(1,31):
    #         print "Working on",s+"_"+str(i)
    #         training.search_field(i,'summary',s)
    # for i in range(25,31):
    #     print "Working on","ib_"+str(i)
    #     training.search_field(i,'summary','ib')


    # print "Building Scheme Vector..."
    # for s in scheme:
    #     for i in range(1,31):
    #         print "working on",s,str(i)
    #         training.buildVectorWithScheme(i,s)
    # print "Done"
    
    # print "Scheme Vector Integration" 
   
    # print "Scheme Training..."
    # for s1 in range(len(scheme)):
    #     for s2 in range(s1+1,len(scheme)):
    #         print "working on",scheme[s1],'and',scheme[s2]
    #         training.training_scheme(scheme[s1],scheme[s2],'summary')
    # print "Done"

    # print "Scheme 3"
    # s = ['ib','dfr','tfidf']
    # training.training_scheme3(s[0],s[1],s[2],'summary')
    # (alpha,beta,gamma) = analyzer.scheme_weight3_average()
    

    # print "Building Field Vector..."
    # for s in scheme:
    #     for i in range(1,31):
    #         print "Working on :", s + "_" + str(i)
    #         training.buildVectorWithField(s,i)
                
    # print "Field Training....."
    # for s in ['ib','tfidf','lmd','bm25','lmj','dfr']:
    #     print "working on",s
    #     training.training_field(s,'summary')
    # print "Done"
    
    # analyzer.scheme_weight_average()
    # analyzer.field_weight_average()

    # pocket = analyzer.scheme_weight
    # for i in pocket:
    #     (s1,s2,alpha,beta) = i
    #     analyzer.scheme_evaluation(alpha,beta,s1,s2,15,0.11)
        
    # for i in analyzer.field_weight:
    #     s,alpha,beta = i
    #     analyzer.field_evaluation(alpha,beta,s,20,0.2)


     # analyzer.scheme_evaluation(0.2,0.5,'dfr','lmd',10,0)
     # analyzer.field_evaluation(0.727,0.273,'dfr',1,0.01)
        
    # analyzer.scheme3_evaluation(alpha,beta,gamma,'dfr','bm25','tfidf',20,0)
    # analyzer.build_double_scheme()
    analyzer.display_double_scheme()
