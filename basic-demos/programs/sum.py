import sys

def main():
    arguments=[ float(x) for x in sys.argv[1:] ]
    sum=0
    for value in arguments:
        sum+=value
    print(sum)


main()