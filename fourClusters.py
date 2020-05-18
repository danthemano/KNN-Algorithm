import random
import math

class fourClusters:

    arr = []
    def __init__(self, text):
        with open(text, "r") as f:
            #skips the first 2 lines because they are not relevant
            inputfile = f.readlines()[2:]
        for line in inputfile:
            line = line.strip('\n')
            self.arr.append([int(line.split('\t')[0]), int(line.split('\t')[1])])


    def kEquals4(self):

        #randomly chooses 4 centroids
        kMean1 = [random.choice(self.arr)]
        kMean2 = [random.choice(self.arr)]
        kMean3 = [random.choice(self.arr)]
        kMean4 = [random.choice(self.arr)]

        while (kMean2 == kMean1 or kMean2 == kMean3 or kMean3 == kMean1):
            kMean2 = [random.choice(self.arr)]
            kMean3 = [random.choice(self.arr)]
        while (kMean4 == kMean1 or kMean4 == kMean2 or kMean4 == kMean3):
            kMean4 = [random.choice(self.arr)]

        subCluster1 = []
        subCluster2 = []
        subCluster3 = []
        subCluster4 = []

        meanEquals = False

        while (meanEquals == False):
            #calculates the euclidian distance
            for x in range(len(self.arr)):
                dist1 = math.sqrt((self.arr[x][0] - kMean1[0][0])**2 +
                                  (self.arr[x][1] - kMean1[0][1])**2)
                dist2 = math.sqrt((self.arr[x][0] - kMean2[0][0])**2 +
                                  (self.arr[x][1] - kMean2[0][1])**2)
                dist3 = math.sqrt((self.arr[x][0] - kMean3[0][0])**2 +
                                  (self.arr[x][1] - kMean3[0][1])**2)
                dist4 = math.sqrt((self.arr[x][0] - kMean4[0][0])**2 +
                                  (self.arr[x][1] - kMean4[0][1])**2)

                if dist1 <= dist2 and dist1 <= dist3 and dist1 <= dist4:
                    subCluster1.append(self.arr[x])
                elif dist2 <= dist1 and dist2 <= dist3 and dist2 <= dist4:
                    subCluster2.append(self.arr[x])
                elif dist3 <= dist1 and dist3 <= dist2 and dist3 <= dist4:
                    subCluster3.append(self.arr[x])
                else:
                    subCluster4.append(self.arr[x])


            #creates variables to store the means
            x1Mean, x2Mean, x3Mean, x4Mean, y1Mean, y2Mean, y3Mean, y4Mean = 0, 0, 0, 0, 0, 0, 0, 0

            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []

            #calculates the means of the subclusters
            for element in subCluster1:
                x1Mean += element[0]
                y1Mean += element[1]
            temp1.append([(x1Mean/len(subCluster1)), (y1Mean/len(subCluster1))])

            for element in subCluster2:
                x2Mean += element[0]
                y2Mean += element[1]
            temp2.append([(x2Mean/len(subCluster2)), (y2Mean/len(subCluster2))])

            for element in subCluster3:
                x3Mean += element[0]
                y3Mean += element[1]
            temp3.append([(x3Mean/len(subCluster3)), (y3Mean/len(subCluster3))])

            for element in subCluster4:
                x4Mean += element[0]
                y4Mean += element[1]
            temp4.append([(x4Mean/len(subCluster4)), (y4Mean/len(subCluster4))])


            if (kMean1 == temp1 and kMean2 == temp2 and kMean3 == temp3 and kMean4 == temp4):
                meanEquals = True

            else:
                kMean1 = temp1
                kMean2 = temp2
                kMean3 = temp3
                kMean4 = temp4

                subCluster1.clear()
                subCluster2.clear()
                subCluster3.clear()
                subCluster4.clear()

                x1Mean, x2Mean, x3Mean, x4Mean, y1Mean, y2Mean, y3Mean, y4Mean = 0, 0, 0, 0, 0, 0, 0, 0

        #adds labels to the clusters
        l1 = []
        for l in range(len(subCluster1)):
            l1.append(str(1))
        l2 = []
        for l in range(len(subCluster2)):
            l2.append(str(2))
        l3 = []
        for l in range(len(subCluster3)):
            l3.append(str(3))
        l4 = []
        for l in range(len(subCluster4)):
            l4.append(str(4))

        #print results to file
        f = open("output4.txt", "w")
        for i in range(len(subCluster1)):
            f.write((str(subCluster1[i]) + "\t" + str(l1[i]) + "\n"))
        for i in range(len(subCluster2)):
            f.write((str(subCluster2[i]) + "\t" + str(l2[i]) + "\n"))
        for i in range(len(subCluster3)):
            f.write((str(subCluster3[i]) + "\t" + str(l3[i]) + "\n"))
        for i in range(len(subCluster4)):
            f.write((str(subCluster4[i]) + "\t" + str(l4[i]) + "\n"))

