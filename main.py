import twoClusters
import threeClusters
import fourClusters

def main():
    file1 = twoClusters.twoClusters("input1.txt")
    file1.kEquals2("input1.txt")

    file2 = twoClusters.twoClusters("input2.txt")
    file2.kEquals2("input2.txt")

    file3 = threeClusters.threeClusters("input3.txt")
    file3.kEquals3()

    file4 = fourClusters.fourClusters("input4.txt")
    file4.kEquals4()


if __name__ == "__main__":
    main()

