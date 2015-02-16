#Convenient functions.
import os
import sys

class ArgumentError(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)

def getFileName(url):
    sep = url.split("/")
    return sep[len(sep)-1]

def listcwd():
	return os.listdir(os.getcwd())
		
def defaultVal(var):
	# '''
	# Evaluate the 'var' as an answer or not
	# for an yes/no question.
	# '''
    var = var.lower()
    if var == "y" or var == "yes":
        return True
    elif var == "n" or var == "no" :
        return False
    else:
        return None

def checkIndex(dictionary, index):
	#'''Check the index of a dictionary.'''
    try:
        dictionary[index]
        return True
    except KeyError:
        return False

def parseArgs(char, target, list=False, string=True):

    '''
    Returns dict with the words in items "i"
    of the list "li" separated by the specified char "char"
    '''

    finaldict = {}
    for i in li:
        #print "Before split:", i
        st = i.split(char)
        #print "After split:", st
        finaldict[st[0]] = st[1]
    return finaldict

def checkType(element, what="file"):
    directory = (what=="dir")
    fil = (what=="file")
    if (fil==directory)==True:
        raise ValueError("'what' argument neither 'file' nor 'dir'")
    try:
        os.chdir(element)
        os.chdir("..")
        if directory:
            return True
        if fil:
            return False
    except:
        if directory:
            return False
        if fil:
            return True

def test():
    t = listcwd()
    for i in listcwd():
        checkType(i, what="dir")

def reverseVals(di, target="keys"):
    vals = target=="values"
    keys = target=="keys"
    if vals or keys:
        if vals:
            normal = di.keys()
            reverse = di.values()
        else:
            normal = di.values()
            reverse = di.keys()
    else:
        raise ValueError("Unknown target type.")
    final = {}
    for i in range(1, len(normal)):
        final[normal[i-1]] = reverse[-i]
    return final

if __name__ == "__main__":
	sys.exit(1)
