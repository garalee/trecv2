import MongoEx
import ElasticIndexing
import ElasticSearching
import ElasticTraining
import pandas as pd


if __name__ == "__main__":
    
    training = ElasticTraining.ElasticTraining()
    indexing = ElasticIndexing.ElasticIndexing()
#    searching = ElasticSearching.ElasticSearching()

    scheme = ['lmd','lmj','dfr','bm25','ib','tfidf']
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
    
    # for s in ['bm25','tfidf','lmd','lmj','dfr']:
    #     for i in range(25,30):
    #         print "Working on",s+"_"+str(i)
    #         training.search_field(i,'summary',s)
    # for s in scheme:
    #     for i in range(1,31):
    #         print 'working on :',str(i)
    #         training.search_field(i,'summary',s)
        
   

    # print "Building Scheme Vector..."
    # for i in range(1,31):
    #     training.buildVectorWithScheme(i)
    # print "Done"
    
    # print "Scheme Vector Integration" 
    
    # prefix = "scheme_score_vector"
    # training.buildVectorWithoutTN(prefix,'description')
    # training.buildVectorWithoutTN(prefix,'summary')

    # print "Scheme Training..."
    # l = pd.DataFrame()
    # for num in range(1,31):
    #     filename = "vector/scheme_vector_summary_" + str(num) + ".csv"
    #     print "working on",filename
    #     l = training.training_scheme(filename)
    #     l.to_csv("analysis/scheme_" + str(num) +".csv",sep='\t',index=False,columns=['scheme1','scheme2','ds','topic','loss','alpha','beta'])
    # print "Done"


    # print "Building Field Vector..."
    # for i in range(1,31):
    #     training.buildVectorWithField('ib',i)
                
    print "Field Training....."
    for s in ['ib','tfidf','dfr','lmd','lmj','bm25']:
        print "working on",s
        training.training_field(s,'summary')
    print "Done"

    # for s in ['tfidf','lmd','lmj','dfr','bm25']:
    #     for i in range(1,31):
    #         print "working on :",s,str(i)
    #         training.search_scheme(s,i,'summary')
