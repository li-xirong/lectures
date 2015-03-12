print 'hello world'
print "hello world"

import sys

if len(sys.argv)<3:
    print 'needs two input'
    sys.exit(0)
 
arg1 = sys.argv[1]
arg2 = sys.argv[2]
print arg1, ":", arg2
