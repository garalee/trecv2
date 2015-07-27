import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class ElasticAnalyzer:
    def __init__(self):
        self.que = pd.read_csv(open('query2014.csv'),sep='\t')
        self.ans_eval = pd.read_csv(open('answer2014.csv'),sep='\t')
        self.scheme = ['bm25','tfidf','ib','lmd','lmj','dfr']

        self.field_weight = {
            ('ib',0.732,0.267), 
            ('tfidf',0.665,0.334), 
            ('lmd',0.901,0.098), 
            ('lmj',0.748,0.251), 
            ('bm25',0.745,0.254) , 
            ('dfr',0.727,0.273)
                             }

        self.scheme_weight = [('ib','tfidf',0.543,0.456),
                              ('ib','lmd',0326666666667 ,0.967333333333),
                              ('ib','lmj',0.0326666666667 ,0.967333333333),
                              ('ib','dfr',0.0326666666667,0.967333333333),
                              ('ib','bm25',0.543666666667 ,0.456333333333),
                              ('tfidf','lmd',0.456333333333 ,0.543666666667),
                              ('tfidf','lmj',0.456333333333 ,0.543666666667),
                              ('tfidf','dfr',0.456333333333 ,0.543666666667),
                              ('tfidf','bm25',0.031 ,0.969),
                              ('lmd','lmj',0.0326666666667 ,0.967333333333),
                              ('lmd','dfr',0.0326666666667 ,0.967333333333),
                              ('lmd','bm25',0.543666666667 ,0.456333333333),
                              ('lmj','dfr',0.0326666666667 ,0.967333333333),
                              ('lmj','bm25',0.543666666667 ,0.456333333333),
                              ('dfr','bm25',0.543666666667 ,0.456333333333)]

        self.scheme3 = [('dfr','lmd','lmj',0.32737,0.334963333333,0.337666666667)]

    def build_double_scheme(self):
        for target in self.scheme:
            v = pd.DataFrame()
            for attach in self.scheme:
                if target == attach:
                    continue
                try:
                    f = open('analysis/'+target + '_' + attach + '_summary.csv')
                    v = v.append(pd.read_csv(f,sep='\t'))
                except IOError:
                    f = open('analysis/'+attach + '_' + target + '_summary.csv')
                    temp = pd.read_csv(f,sep='\t')
                    temp.rename(columns={'scheme1' : 't'})
                    temp.rename(columns={'scheme2' : 'scheme1'})
                    temp.rename(columns={'t'       : 'scheme2'})
                    temp.rename(columns={'alpha'   : 't'})
                    temp.rename(columns={'beta'    : 'alpha'})
                    temp.rename(columns={'t'       : 'beta'})
                    v = v.append(temp)

            v.to_csv('analysis/double_scheme_' + target + '.csv',sep='\t',index=False)
            

    def display_double_scheme(self):
        fig,axes = plt.subplots(nrows=2,ncols=3)

        data = pd.read_csv(open('analysis/double_scheme_ib.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[0,0],by='topic',column='alpha')

        data = pd.read_csv(open('analysis/double_scheme_dfr.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[0,1],by='topic',column='alpha')

        data = pd.read_csv(open('analysis/double_scheme_lmd.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[0,2],by='topic')

        data = pd.read_csv(open('analysis/double_scheme_lmj.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[1,0],by='topic')

        data = pd.read_csv(open('analysis/double_scheme_tfidf.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[1,1],by='topic')

        data = pd.read_csv(open('analysis/double_scheme_bm25.csv'),sep='\t')
        data = data.ix[:,['topic','alpha']]
        data.boxplot(ax=axes[1,2],by='topic')

        fig.show()

        raw_input()

    
            
            
            


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

    def scheme_weight3_average(self):
        filename = 'analysis/scheme_dfr_lmd_lmj_summary.csv'
        data = pd.read_csv(open(filename),sep='\t')

        print "Alpha:", data['alpha'].sum()/30
        print "Beta:", data['beta'].sum()/30
        print "Gamma:", data['gamma'].sum()/30
        return (data['alpha'].sum()/30, data['beta'].sum()/30, data['gamma'].sum()/30)
        

    def scheme_weight_average(self):
        scheme = ['ib','tfidf','lmd','lmj','dfr','bm25']
        
        for s1 in range(len(scheme)):
            for s2 in range(s1+1,len(scheme)):
                filename = scheme[s1] + '_' + scheme[s2] + '_summary.csv'
                print "working on",filename
                avgAlpha = 0.0
                avgBeta = 0.0
                loss = 0.0
                data = pd.read_csv(open('analysis/'+filename),sep='\t')
                for idx,entry in data.iterrows():
                    avgAlpha = avgAlpha + entry['alpha']
                    avgBeta = avgBeta + entry['beta']
                    loss = loss + entry['loss']
                print "Alpha:",avgAlpha/30,",Beta:",avgBeta/30, ",Loss:",loss

    def field_evaluation(self,alpha,beta,scheme,num,limit):
        print "Field Evaluation"
        print "Without weighting"
        filename = 'field_' + scheme + '_summary_' + str(num) + '_eval.csv'

        comparison = scheme+"_summary_" + str(num) + '.csv'
        data = pd.read_csv(open('vector/'+filename),sep='\t')
        comparison_data = pd.read_csv(open('search_result/'+comparison),sep='\t')
        m =pd.merge(comparison_data,data,how='inner',on=['pmcid','relevancy'])

        print 'scheme:',scheme,'precision:',len(m[(m['score'] > limit)&((m['relevancy'] == 1) | (m['relevancy'] == 2))])/float(len(m))
        
        print "With weighting"
        m['result'] = m['title']*alpha + m['abstract']*beta
        print 'weighting precision:', len(m[(m['result'] > limit) & ((m['relevancy'] == 1)|(m['relevancy'] == 2))])/float(len(m))
        print '\n'

    def scheme3_evaluation(self,alpha,beta,gamma,s1,s2,s3,num,limit):
        print "Scheme 3 Evaluation"
        print "Without weighting"

        filename1 = 'scheme_' + s1 + '_summary_' + str(num) + '_eval.csv'
        filename2 = 'scheme_' + s2 + '_summary_' + str(num) + '_eval.csv'
        filename3 = 'scheme_' + s3 + '_summary_' + str(num) + '_eval.csv'

        data1 = pd.read_csv(open('vector/'+filename1),sep='\t')
        data1 = data1.rename(columns={'score' : s1})
        data2 = pd.read_csv(open('vector/'+filename2),sep='\t')
        data2 = data2.rename(columns={'score' : s2})
        data3 = pd.read_csv(open('vector/'+filename3),sep='\t')
        data3 = data3.rename(columns={'score' : s3})


        print "scheme:",s1,"precision:",len(data1[(data1[s1] > limit)&((data1['relevancy'] == 1)|(data1['relevancy'] == 2))])/float(len(data1))
        print "scheme:",s2,"precision:",len(data2[(data2[s2] > limit)&((data2['relevancy'] == 1)|(data2['relevancy'] == 2))])/float(len(data2))
        print "scheme:",s3,"precision:",len(data3[(data3[s3] > limit)&((data3['relevancy'] == 1)|(data3['relevancy'] == 2))])/float(len(data3))

        print "With weighting"
        m = pd.merge(data1,data2,how='outer',on=['pmcid','relevancy'])
        m = pd.merge(m,data3,how='outer',on=['pmcid','relevancy'])
        m.fillna(0)

        m[s1] = m[s1]*alpha
        m[s2] = m[s2]*beta
        m[s3] = m[s3]*gamma
        m['result'] = m[s1]+m[s2]+ m[s3]
        print "weighting precision:",len(m[(m['result'] > limit)&((m['relevancy'] == 1) | (m['relevancy'] == 2))])/float(len(m))
        print '\n'
        
        
    def scheme_evaluation(self,alpha,beta,scheme1,scheme2,num,limit):
        print "Scheme Evaluation"
        print "Without weighting"
        filename1 = 'scheme_' + scheme1 + '_summary_' + str(num) + '_eval.csv'
        filename2 = 'scheme_' + scheme2 + '_summary_' + str(num) + '_eval.csv'

        data1 = pd.read_csv(open('vector/'+filename1),sep='\t')
        data1 = data1.rename(columns={'score' : scheme1})
        data2 = pd.read_csv(open('vector/'+filename2),sep='\t')
        data2 = data2.rename(columns={'score' : scheme2})

        print "scheme:",scheme1,"precision:",len(data1[(data1[scheme1] > limit)&((data1['relevancy'] == 1)|(data1['relevancy'] == 2))])/float(len(data1))
        print "scheme:",scheme2,"precision:",len(data2[(data2[scheme2] > limit)&((data2['relevancy'] == 1)|(data2['relevancy'] == 2))])/float(len(data2))
        
        print "With weighting"
        m = pd.merge(data1,data2,how='outer',on=['pmcid','relevancy'])

        m[scheme1] = m[scheme1]*alpha
        m[scheme2] = m[scheme2]*beta
        m['result'] = m[scheme1]+m[scheme2]

        print "weighting precision:",len(m[(m['result'] > limit)&((m['relevancy'] == 1) | (m['relevancy'] == 2))])/float(len(m))
        print '\n'

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
        
