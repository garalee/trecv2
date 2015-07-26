import numpy as np
import pandas as pd

class ElasticAnalyzer:
    def __init__(self):
        self.es = Elasticsearch([{'host':'localhost','port':9200}])
        self.que = pd.read_csv(open('query2014.csv'),sep='\t')
        self.ans_eval = pd.read_csv(open('answer2014.csv'),sep='\t')
        self.scheme = ['bm25','tfidf','ib','lmd','lmj','dfr']


    def field_weight_average(self):
        scheme = ['ib','tfidf','lmd','lmj','bm25','dfr']
        
        for s in scheme:
            filename = 'field_' + s + '_summary.csv'
            print "working on",filename
            avgAlpha= 0
            avgBeta = 0
            data = pd.read_csv(open('analysis/'+filename),sep='\t')
            for idx,entry in data.iterrows():
                avgAlpha = avgAlpha + entry['alpha']
                avgBeta = avgBeta + entry['beta']
            print "Alpha:",avgAlpha/30,",Beta:",avgBeta/30

    def scheme_weight_average(self):
        scheme = ['ib','tfidf','lmd','lmj','dfr','bm25']
        
        for s1 in range(len(scheme)):
            for s2 in range(s1+1,len(scheme)):
                filename = scheme[s1] + '_' + scheme[s2] + '_summary.csv'
                print "working on",filename
                avgAlpha = 0.0
                avgBeta = 0.0
                data = pd.read_csv(open('analysis/'+filename),sep='\t')
                for idx,entry in data.iterrows():
                    avgAlpha = avgAlpha + entry['alpha']
                    avgBeta = avgBeta + entry['beta']
                print "Alpha:",avgAlpha/30,",Beta:",avgBeta/30

    def field_evaluation(self):
        print "Without weighting"

    def scheme_evaluation(self):
        pass
    

    def query_field_control(self,scheme,ds,topic,num,weights):
        (alpha,beta,gamma) = weights
        for index,entry in self.que.iterrows():
            if entry['topic'] == topic:
                query =entry
                break
        
        
        content = query[ds].replace(r"/",',')
        token = content.split(' ')
        content = [x for idx,x in enumerat(toeken) if not idx ==0]
        content = ' '.join(content)
        analyzer = "my_" + scheme + "_analyzer"

        resTitle = self.es.search(index=scheme+"_garam_eval",q='title:'+content,doc_type='article',analyzer=analyzer,size=10000)
        resAbstract = self.es.search(index=scheme+"_garam_eval",q='abstract:'+content,doc_type='article',analyzer=analyzer,size=10000)
        resBody = self.es.search(index=scheme+"_garam_eval",q='body:'+content,doc_type='article',analyzer=analyzer,size=10000)

        for entry in resTitle['hits']['hits']:
            pmcid = entry['_id']
            score = entry['_score']
        
