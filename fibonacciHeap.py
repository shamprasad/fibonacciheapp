from random import randint
import time
import sys
class Node:
    def __init__(self, key):
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.key = key        
        self.degree = 0
        self.marked = False
        
def insert(key):
    global minPtr,numberOfNodes
    tempNode = Node(key)
    tempNode.left = tempNode.right = tempNode
    addToTreeList(tempNode)
    if minPtr is None or tempNode.key < minPtr.key:
        minPtr = tempNode
    numberOfNodes += 1

def linkHeap( H1, H2):
    removefromroot(H1)
    H1.left = H1
    H1.right = H1
    addtoChildList(H2, H1)
    H2.degree += 1
    H1.parent = H2
    H1.marked = False

def extractMinimum():
    global minPtr,numberOfNodes
    tempMin = minPtr
    if tempMin is not None:
        if tempMin.child is not None:
 
            allChild = [child1 for child1 in iterate(tempMin.child)]
            for i in xrange(0, len(allChild)):
                addToTreeList(allChild[i])
                allChild[i].parent = None
        removefromroot(tempMin)

        if tempMin == tempMin.right:
            minPtr = None
            TreeList = None
        else:
            minPtr = tempMin.right
            consolidate()
        numberOfNodes -= 1
    return tempMin


def iterate(H):
    
    stopFlag = False
    node = H
    end = H

    while True:
        if node == end and stopFlag is True:
            break
        elif node == end:
            stopFlag = True
        yield node
        node = node.right

TreeList, minPtr = None, None
numberOfNodes = 0


def addToTreeList(node):
    global TreeList
    if TreeList is None:
        TreeList = node
    else:
        node.right = TreeList.right
        node.left = TreeList
        TreeList.right.left = node
        TreeList.right = node
  

def addtoChildList(parent, node):
    if parent.child is None:
        parent.child = node
    else:
        node.right = parent.child.right
        node.left = parent.child
        parent.child.right.left = node
        parent.child.right = node

def decreaseKey(node1, newKey):
    if newKey > node1.key:
        return None
    node1.key = newKey
    PNode = node1.parent
    if PNode is not None and node1.key < PNode.key:
        cut(node1, PNode)
        cascadingCut(PNode)
    if node1.key < minPtr.key:
        minPtr = node1

def cut(node1, node2):
    removefromchild(node2, node1)
    node2.degree -= 1
    addToTreeList(node1)
    node1.parent = None
    node1.marked = False

def cascadingCut(node1):
    nodeP = node1.parent
    if nodeP is not None:
        if node1.marked is False:
            node1.marked = True
        else:
            cut(node1, nodeP)
            cascadingCut(nodeP)

def consolidate():
    global minPtr
    tempNodeList = [None] * numberOfNodes
    nodes = [node1 for node1 in iterate(TreeList)]
    for node1 in xrange(0, len(nodes)):
        node2= nodes[node1]
        tempDegree = node2.degree
        while tempNodeList[tempDegree] != None:
            node3 = tempNodeList[tempDegree] 
            if node2.key > node3.key:
                temp = node2
                node2, node3 = node3, temp
            linkHeap(node3, node2)
            tempNodeList[tempDegree] = None
            tempDegree += 1
        tempNodeList[tempDegree] = node2

    for i in xrange(0, len(tempNodeList)):
        if tempNodeList[i] is not None:
            if tempNodeList[i].key < minPtr.key:
                minPtr = tempNodeList[i]



def removefromchild(parent, node):
    if parent.child == parent.child.right:
        parent.child = None
    elif parent.child == node:
        parent.child = node.right
        node.right.parent = parent
    node.left.right = node.right
    node.right.left = node.left


def removefromroot( node):
    global TreeList
    if node == TreeList:
        TreeList = node.right
    node.left.right = node.right
    node.right.left = node.left
    

print int(sys.argv[1]),
for i in xrange(0, int(sys.argv[1])):
    #startTime = time.time()
    insert(randint(1,100))    
    #elapsedTime = time.time() - startTime
    #print i,elapsedTime

startTime = time.time()
for i in xrange(0, int(sys.argv[1])):
    
    m = extractMinimum()    
elapsedTime = time.time() - startTime
print elapsedTime



