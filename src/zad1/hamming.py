class Hamming:
    def distance(first, second):
        numberOfErrors = 0
        if len(first) != len(second):
            raise ValueError("Strands should be the same length")
        for i in range(len(first)): 
            if first[i] != second[i]:
                numberOfErrors += 1
        return numberOfErrors