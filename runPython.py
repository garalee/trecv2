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

    # print "Build DS Vector.."
    # for s in scheme:
    #     for i in range(1,31):
    #         print "<"+s+">" +"NUM : " + str(i)
    #         training.buildVectorWithDS(i,s)
    # print "\a"

    # print "Training DS Vector.."
    # l = pd.DataFrame(columns=['scheme','topic','loss','alpha'])
    # for s in scheme:
    #     for i in range(1,31):
    #         filename = "vector/DS_score_vector_"+s+"_" + str(i) + ".csv"
    #         l = l.append(training.training_ds(filename))
    # l.to_csv("analysis/ds_result.csv",sep='\t',index=False,columns=['scheme','topic','loss','alpha'])
    # print "Done"
    
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
    

    # print "Building Field Vector..."
    # for s in ['dfr']:
    #     for i in range(1,31):
    #         print "Working on :", s + "_" + str(i)
    #         training.buildVectorWithField(s,i)
                
    # print "Field Training....."
    # for s in ['ib','tfidf','lmd','bm25','lmj','dfr']:
    #     print "working on",s
    #     training.training_field(s,'summary')
    # print "Done"

    
    analyzer.scheme_weight_average()
    analyzer.field_weight_average()
