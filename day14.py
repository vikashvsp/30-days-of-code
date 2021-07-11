class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        sort_elem=sorted(self.__elements)
        self.maximumDifference=abs(sort_elem[-1]-sort_elem[0])
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)