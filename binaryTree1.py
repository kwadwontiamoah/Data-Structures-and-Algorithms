# This file contains functions to create and manipulate the
# "list of lists" representation of the binary search tree, as
# described in Section 6.3 of the textbook.

# Create a binary tree consisting of only one node -- the root
def BinaryTree(r):
    return [r, [], []]

# Insert a new branch into the left of the 
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
print("Created tree:")
print(r)
l = getLeftChild(r)
print("Left subtree of the tree above:")
print(l)

setRootVal(l,9)
print("Changed root of left subtree from",getLeftChild(r)[0],"to 9. Tree is now:")
print(r)
insertRight(l,11)
print("Inserted 11 into right of the left subtree.  Tree is now")
print(r)
print("Right subtree of right child is:")
print(getRightChild(getRightChild(r)))


