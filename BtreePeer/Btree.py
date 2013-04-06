
#Node class
class Node:
    #create a node and intitialize left,right, peer pointers to null
    #and set data hold value
    def __init__(self,num):
        self.left=None
        self.right=None
        self.peer=None
        self.data=num


class Btree:
    #initialize root node to null
    def __init__(self):
        self.root=None
      

    #do a BFT and add None to mark the level
    def findPeer(self):
        q=Queue()
        #if empty tree return
        if not self.root:
            print "Empty\n"
            return
        #add root node to queue
        q.enqueue(self.root)
        #add level marker
        q.enqueue(None)
        
        while not q.isEmpty():
            temp=q.front();
            q.dequeue()
            #if not level marker ie) a Node do the below
            if temp:
                temp.peer=q.front()

                ''''Just preparing the peer data and printing'''
                if temp.peer:
                    peer_data=temp.peer.data
                else:
                    peer_data="Null"
                print "%s-->%s"%(temp.data,peer_data)

                
                if temp.left:
                    q.enqueue(temp.left)
                if temp.right:
                    q.enqueue(temp.right)
            #if level marker do the below
            else:
                if not q.isEmpty():
                    q.enqueue(None)
        print "\n"
        
#Simple Queuue Class to use
class Queue:
    def __init__(self):
        self.q=[]
        self.fp=-1

    def enqueue(self,obj):
        self.q.insert(0,obj)
        self.fp+=1

    def dequeue(self):
        ele=self.q.pop()
        self.fp-=1
        return ele

    def isEmpty(self):
        if self.fp==-1:
            return True
        return False
        
    def display(self):
        print self.q

    def front(self):
        return self.q[self.fp]


if __name__=="__main__":

    print "1. Empty case"
    bt=Btree()
    bt.findPeer()
    
    print "2. Single Node case"
    bt=Btree()
    bt.root=Node(1)
    bt.findPeer()
    
    print "3. left  child case"
    bt=Btree()
    bt.root=Node(1)
    bt.root.left=Node(2)
    bt.findPeer()

    print "4.  right child case"
    bt=Btree()
    bt.root=Node(1)
    bt.root.right=Node(2)
    bt.findPeer()

    print "5.  sibiling case"
    bt=Btree()
    bt.root=Node(1)
    bt.root.left=Node(2)
    bt.root.right=Node(3)
    bt.findPeer()

    print '''6. diffent cases including
a.sibiling
b.Left Left - Right Left
c.Left Left - Right Right
d.Left Right - Right left
e.Right Right- Right Right
refer tree_testcasepic.png
'''
    bt=Btree()
    bt.root=Node(1)
    bt.root.left=Node(2)
    bt.root.right=Node(3)
    bt.root.left.left=Node(4)
    bt.root.right.right=Node(5)
    bt.root.left.left.left=Node(6)
    bt.root.right.right.left=Node(7)
    bt.root.left.left.left.right=Node(8)
    bt.root.right.right.left.right=Node(9)
    bt.root.left.left.left.right.right=Node(10)
    bt.root.right.right.left.right.left=Node(11)
    bt.findPeer()
    
    

