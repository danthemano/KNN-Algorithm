import random
import math

class twoClusters:

    arr = []
    def __init__(self, text):
        with open(text, "r") as f:
            #skips the first 2 lines because they are not relevant
            inputfile = f.readlines()[2:]
        for line in inputfile:
            line = line.strip('\n')
            self.arr.append([int(line.split('\t')[0]), int(line.split('\t')[1])])

    #This function takes as input the input file because there are 2 input files
    #that have k = 2
    def kEquals2(self, text):

        #randomly chooses 2 centroids
        kMean1 = [random.choice(self.arr)]
        kMean2 = [random.choice(self.arr)]

        while (kMean2 == kMean1):
            kMean2 = [random.choice(self.arr)]
        subCluster1 = []
        subCluster2 = []

        meansEqual = False

        while (not meansEqual):
            #calculates the euclidian distance
            for x in range(len(self.arr)):
                dist1 = math.sqrt((self.arr[x][0] - kMean1[0][0])**2 +
                                       (self.arr[x][1] - kMean1[0][1])**2)
                dist2 = math.sqrt((self.arr[x][0] - kMean2[0][0])**2 +
                                       (self.arr[x][1] - kMean2[0][1])**2)

                #stores the element in the correct cluster
                if dist1 <= dist2:
                    subCluster1.append( self.arr[x])
                else:
                    subCluster2.append( self.arr[x])

            #creates variables to store the means
            x1Mean, y1Mean, x2Mean, y2Mean= 0,0,0,0

            #stores the temporary means
            temp1 = []
            temp2 = []

            #calculates the means of the subclusters
            for element in subCluster1:
                x1Mean += element[0]
                y1Mean += element[1]
            temp1.append([(x1Mean/len(subCluster1)), (y1Mean/len(subCluster1))])

            for element in subCluster2:
                x2Mean += element[0]
                y2Mean += element[1]
            temp2.append([(x2Mean/len(subCluster2)), (y2Mean/len(subCluster2))])

            #if both means are the same then we are done
            if (kMean1 == temp1 and kMean2 == temp2):
                meansEqual = True

            else:
                kMean1 = temp1
                kMean2 = temp2
                subCluster1.clear()
                subCluster2.clear()
                x1Mean, y1Mean, x2Mean, y2Mean= 0,0,0,0

        #adds labels to the clusters
        l1 = []
        for l in range(len(subCluster1)):
            l1.append(str(1))

        l2 = []
        for l in range(len(subCluster2)):
            l2.append(str(2))

        #checks to see which output file we want to create based on the given
        #input file
        if(text == "input1.txt"):
            f = open("output1.txt", "w")
            for i in range(len(subCluster1)):
                f.write((str(subCluster1[i]) + "\t" + str(l1[i]) + "\n"))
            for i in range(len(subCluster2)):
                f.write((str(subCluster2[i]) + "\t" + str(l2[i]) + "\n"))
        else:
            f = open("output2.txt", "w")
            for i in range(len(subCluster1)):
                f.write((str(subCluster1[i]) + "\t" + str(l1[i]) + "\n"))
            for i in range(len(subCluster2)):
                f.write((str(subCluster2[i]) + "\t" + str(l2[i]) + "\n"))