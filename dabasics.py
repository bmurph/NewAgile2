import fileinput
import csv
import numpy
import unittest
import random


batterysample = [['46;471289267;2010-12-15T10:49:32.994+0000;power', 'battery', 'level;94'], ['47;471289359;2010-12-15T10:49:33.086+0000;power', 'battery', 'scale;100'], ['48;471289452;2010-12-15T10:49:33.179+0000;power', 'battery', 'temperature;272'], ['49;471289505;2010-12-15T10:49:33.232+0000;power', 'battery', 'voltage;4070'], ['366;471316384;2010-12-15T10:50:00.111+0000;power', 'battery', 'level;93'], ['367;471316609;2010-12-15T10:50:00.336+0000;power', 'battery', 'scale;100'], ['368;471316800;2010-12-15T10:50:00.527+0000;power', 'battery', 'temperature;287'], ['369;471317063;2010-12-15T10:50:00.790+0000;power', 'battery', 'voltage;4045'], ['3100;475016888;2010-12-15T11:51:40.615+0000;power', 'battery', 'level;92'], ['3101;475068951;2010-12-15T11:52:32.678+0000;power', 'battery', 'scale;100'], ['3102;475069251;2010-12-15T11:52:32.978+0000;power', 'battery', 'temperature;230'], ['3103;475121903;2010-12-15T11:53:25.630+0000;power', 'battery', 'voltage;4084'], ['3104;475122450;2010-12-15T11:53:26.177+0000;power', 'battery', 'level;93'], ['3105;475187885;2010-12-15T11:54:31.612+0000;power', 'battery', 'scale;100'], ['3106;475188068;2010-12-15T11:54:31.795+0000;power', 'battery', 'temperature;230'], ['3107;475188267;2010-12-15T11:54:31.994+0000;power', 'battery', 'voltage;4084'], ['3108;475188371;2010-12-15T11:54:32.098+0000;power', 'battery', 'level;92'], ['3109;475188481;2010-12-15T11:54:32.208+0000;power', 'battery', 'scale;100'], ['3110;475188564;2010-12-15T11:54:32.291+0000;power', 'battery', 'temperature;230'], ['3111;475188637;2010-12-15T11:54:32.364+0000;power', 'battery', 'voltage;4084'], ['4841;477304015;2010-12-15T12:29:47.742+0000;power', 'battery', 'level;91'], ['4921;477304623;2010-12-15T12:29:48.350+0000;power', 'battery', 'scale;100'], ['4922;477304795;2010-12-15T12:29:48.522+0000;power', 'battery', 'temperature;230'], ['4923;477304801;2010-12-15T12:29:48.528+0000;power', 'battery', 'voltage;4079'], ['4924;477415931;2010-12-15T12:31:39.658+0000;power', 'battery', 'level;92'], ['4925;477416721;2010-12-15T12:31:40.448+0000;power', 'battery', 'scale;100'], ['4926;477436878;2010-12-15T12:32:00.605+0000;power', 'battery', 'temperature;228'], ['4927;477437003;2010-12-15T12:32:00.730+0000;power', 'battery', 'voltage;4079'], ['4928;477521908;2010-12-15T12:33:25.635+0000;power', 'battery', 'level;91'], ['4929;477587865;2010-12-15T12:34:31.592+0000;power', 'battery', 'scale;100'], ['4930;477588219;2010-12-15T12:34:31.946+0000;power', 'battery', 'temperature;230'], ['4931;477589343;2010-12-15T12:34:33.070+0000;power', 'battery', 'voltage;4079'], ['6532;479630904;2010-12-15T13:08:34.631+0000;power', 'battery', 'level;90'], ['6533;479631432;2010-12-15T13:08:35.159+0000;power', 'battery', 'scale;100'], ['6534;479687879;2010-12-15T13:09:31.606+0000;power', 'battery', 'temperature;276'], ['6535;479688016;2010-12-15T13:09:31.743+0000;power', 'battery', 'voltage;4070']]

samplelines = [['6534;479687879;2010-12-15T13:09:31.606+0000;power', 'battery', 'temperature;276']]

##Counts all rows in the sample file
def CountRows(dataset):
	counter = 0
	for row in dataset:
		counter += 1
	return counter

# print CountRows(batterysample)

def SplitSemicolonValues(string):
	newlist = string.split(";")
	return newlist

def CreateAttributeList(dataset):
	attributes = []
	for item in dataset:
		attributes.append(item[2])
	return attributes

attributelist = CreateAttributeList(batterysample)

print attributelist

def CleanAttList(attlist):
	newlist = []
	for item in attlist:
		keyvalue = SplitSemicolonValues(item)
		newlist.append(keyvalue)
	return newlist

valuelist = CleanAttList(attributelist)
print valuelist
print len(valuelist)

def ListMaker(valuelist, key):
	newlist = []
	for item in valuelist:
		if item[0] == key:
			newlist.append(item[1])
	return newlist

templist = ListMaker(valuelist, "temperature")
templist = map(int, templist)
print templist

def MeanCalc(list):
	x = numpy.mean(list)
	return int(x)

print MeanCalc(templist)


###
#K-means Calc from DataMining HW, modified by BM
###

k = 2  # number of clusters


###
# Helper functions
# Fill in TODOs where needed
##/

def pick_centroids(xs, num):
    """Return list of num centroids given a list of numbers in xs"""
    ###
    # TODO select and return centroids
    centroidlist = random.sample(set(xs), num)
    return centroidlist
    ##/


def distance(a, b):
    """Return the distance of numbers a and b"""
    ###
    # TODO return correct expression
    return abs(a-b)
    ##/


def centroid(xs):
    """Return the centroid number given a list of numbers, xs"""
    ###
    # TODO calculate and return centroid
    total = sum(xs)
    centroid = total/(len(xs))
    return centroid
    ##/


def cluster(xs, centroids):
    """Return a list of clusters centered around the given centroids.  Clusters
    are lists of numbers."""

    clusters = [[] for c in centroids]

    for x in xs:
        # find the closest cluster to x
        dist, cluster_id = min(
            (distance(x, c), cluster_id) for cluster_id, c in enumerate(centroids)
        )
        # place x in cluster
        clusters[cluster_id].append(x)

    return clusters


def iterate_centroids(xs, centroids):
    """Return stable centroids given a dataset and initial centroids"""

    err = 0.001  # minimum amount of allowed centroid movement
    observed_error = 1  # Initialize: maxiumum amount of centroid movement
    new_clusters = [[] for c in centroids]  # Initialize: clusters

    while observed_error > err:
        new_clusters = cluster(xs, centroids)
        new_centroids = map(centroid, new_clusters)

        observed_error = max(abs(new - old) for new, old in zip(new_centroids, centroids))
        centroids = new_centroids

    return (centroids, new_clusters)


###
# Main part of program:
# Pick initial centroids
# Iterative to find final centroids
# Print results
##/

initial_centroids = pick_centroids(templist, k)
print initial_centroids
final_centroids, final_clusters = iterate_centroids(templist, initial_centroids)

for centroid, cluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroid
    print "Cluster contents: %r" % cluster




#Unit Test Classes

class CountRowsTests(unittest.TestCase):

    def testBatterySampleShouldHave36Rows(self):
        self.assertEqual(CountRows(batterysample), 36)

class SplitSemicolonValuesTests(unittest.TestCase):

	def testSplitStringShouldBeList(self):
		self.assertEqual(SplitSemicolonValues('voltage;4070'), ['voltage', '4070'])

	def testTwo(self):
		self.assertEqual(SplitSemicolonValues(attributelist[2]), ['temperature', '272'])

class CleanAttListTests(unittest.TestCase):

	def testNewListLenShouldEqualOldListLen(self):
		self.assertEqual(len(valuelist), len(attributelist))

	def testItem3inListShouldEqualNewSplitList(self):
		self.assertEqual(valuelist[2], ['temperature', '272'])

class ListMakerTests(unittest.TestCase):

	def testReturnEmptyListIfNoMatchesFound(self):
		self.assertEqual(ListMaker(valuelist, "nope"),[])

class MeanCalcTests(unittest.TestCase):

	def testMeanOfTemplistShouldBe245(self):
		self.assertEqual(MeanCalc(templist), 245)

class PickCentroids(unittest.TestCase):

	def testShouldReturn2Values(self):
		self.assertEqual(2, len(pick_centroids(templist, k)))



def main():
    unittest.main()

if __name__ == '__main__':
    main()




