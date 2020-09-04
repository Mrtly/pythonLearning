# modules in python

import sys, os, random, datetime

def main():
    v = sys.version_info
    print('python version {}.{}.{}'.format(*v))
    print(sys.platform) # darwin for Mac
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd()) # current working dir
    print(os.urandom(25).hex())
    print(random.randint(1,1000))
    # random list shuffle:
    xlist = list(range(25))
    print(xlist)
    random.shuffle(xlist)
    print(xlist)
    # date time
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()