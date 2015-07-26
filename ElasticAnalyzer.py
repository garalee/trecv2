import numpy as np
import pandas as pd

class ElasticAnalyzer:
    def __init__(self):
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

    def scheme_evaluation(self,alpha,beta,scheme1,scheme2,num,limits):
        print "Without weighting"
        filename1 = 'scheme_' + scheme1 + '_summary_' + str(num) + '_eval.csv'
        filename2 = 'scheme_' + scheme2 + '_summary_' + str(num) + '_eval.csv'

        data1 = pd.read_csv(open('vector/'+filename1),sep='\t')
        data1 = data1.rename(columns={'score' : scheme1})
        data2 = pd.read_csv(open('vector/'+filename2),sep='\t')
        data2 = data2.rename(columns={'score' : scheme2})

        print "scheme:",scheme1,"precision:",len(data1[(data1[scheme1] > limits)&((data1['relevancy'] == 1)|(data1['relevancy'] == 2))])/float(len(data1))
        print "scheme:",scheme2,"precision:",len(data2[(data2[scheme2] > limits)&((data2['relevancy'] == 1)|(data2['relevancy'] == 2))])/float(len(data2))
        
        print "With weighting"
        m = pd.merge(data1,data2,how='outer',on=['pmcid','relevancy'])

        m[scheme1] = m[scheme1]*alpha
        m[scheme2] = m[scheme2]*beta
        m['result'] = m[scheme1]+m[scheme2]

        print "weighting precision:",len(m[(m['result'] > limits)&((m['relevancy'] == 1) | (m['relevancy'] == 2))])/float(len(m))

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
        
