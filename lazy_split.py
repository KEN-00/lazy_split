import collections
import sys
import getopt
import json

def generate(args):
    inputString = args["inputString"]
    separator  = args["separator"]

    splittedStrings = inputString.split(separator)

    w = open(args["output"], 'w')

    for s in splittedStrings:
        print(s)
        w.write(s + "\n")


def getArgs(argv):
   inputString = None
   separator = None
   output = None

   try:
      opts, args = getopt.getopt(argv,"i:s:o:",["inputString=", "separator=","output="])
   except getopt.GetoptError:
      print('split.py -i <inputString> -s <separator> -o <output>')
      sys.exit(2)


   for opt, arg in opts:
      if opt in ("-i", "--inputString"):
         inputString = arg
      if opt in ("-s", "--separator"):
         separator = arg
      if opt in ("-o", "--output"):
         output = arg


   jsonData = None

   
   config = {
       "inputString": inputString,
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


