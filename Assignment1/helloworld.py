# 2014-01 Jason Roebuck
# Product of work for GEOG 590 @ Portland State University
# May be used for whatever!
# github.com/jtroe/GEOG-590 - Fork me on github!
def main():
    # Declare a good, old fashioned greeting.
    greeting = 'Hello, Portland!'
    print greeting

    # print a separator
    print '======'

    # prints every character from 'Hello, Portland!' on it's very own line!
    for char in greeting:
        print char

    print '======'

    # should print 'Hell Portland!'
    print greeting[0:4], greeting[7:]

    print '======'

    # declare a list of smurf strings
    mySmurfList = ['Papa', 'Smurfette', 'Hefty', 'Brainy', 'Grouchy', 'Clumsy']
    for smurf in mySmurfList:
        # if string length is greater than 4, print it! Sorry, papa.
        if len(smurf) > 4:
            print smurf

    print '======'

    # equivalent of the more traditional for loop.
    # instead of getting the actual object of the list, gets the index
    # for(int i = 0; i < mySmurfList.Length; i++) <= C# equivalent
    for i in range(len(mySmurfList)):
        print mySmurfList[i]

if __name__ == "__main__":
    main()