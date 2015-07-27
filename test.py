try:
    f = open('ElasticTraining.p')
except IOError:
    print "ERROR"
else:
    with f:
        print f.readlines()
