import collections
import sys
import getopt
import json

def generate(args):
    f = open(args["inputFile"], 'r')
    allLines = f.read().splitlines()

    separator  = args["separator"]

    joinedString = separator.join(allLines)

    w = open(args["output"], 'w')
    w.write(joinedString + "\n")



def getArgs(argv):
   inputFile = None
   separator = None
   output = None

   try:
      opts, args = getopt.getopt(argv,"i:s:o:",["inputFile=", "separator=","output="])
   except getopt.GetoptError:
      print('split.py -i <inputFile> -s <separator> -o <output>')
      sys.exit(2)


   for opt, arg in opts:
      if opt in ("-i", "--inputFile"):
         inputFile = arg
      if opt in ("-s", "--separator"):
         separator = arg
      if opt in ("-o", "--output"):
         output = arg


   jsonData = None

   
   config = {
       "inputFile": inputFile,
       "separator": separator,
       "output": output
   }
   
   return config


if __name__ == '__main__':
    try:
        argv = sys.argv[1:]
        args = getArgs(argv)
        
        generate(args)
    except Exception as e:
        print(e)


