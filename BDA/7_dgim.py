
class Bucket:
    """ This is Bucket(Node) which holds data and timestamp"""
    def __init__(self , timestamp , data = 1):
        self.timestamp = timestamp
        self.data = data
        self.next = None

    def doubleData(self):
        self.data = self.data * 2

    def __repr__(self):
        return "(time: " + str(self.timestamp) + " - value: " + str(self.data) + ")"

class DGIM:
    """
        To initialize this clas, please set the Window Size first
    """
    def __init__(self , MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.head = None
        self.tail = None

    """
        This removes the last bucket of buffer when window size is full
    """
    def removeTail(self):
        prev = None
        curr = self.head

        while curr.next != None:
            prev = curr
            curr = curr.next
        print("current state" , end=" : ")
        self.printBuffer()
        print()
        print("removing =>", curr)
        if prev is not None:
            self.tail = prev
            prev.next = None
        
        return
    
    """
        This prints full buffer
    """
    def printBuffer(self):
        
        cur = self.head
        
        while cur is not None:
            print(cur , end=" => ")
            cur = cur.next
    
    """
        This returns total sum of current window
    """
    def getSum(self):
        cur = self.head
        ans = 0
        while cur is not None:
            ans += cur.data
            cur = cur.next
        
        return ans
            
    """
        This adds new Bucket with value = 1 and timestamp as input
    """
    def add(self , timestamp):

        newBucket = Bucket(timestamp)

        if self.head is None:
            self.head = newBucket
            self.tail = newBucket

            return
        
        #Adding new Bucket to front of Buffer
        newBucket.next = self.head
        self.head = newBucket
        #check If Window is full
        if self.head.timestamp - self.tail.timestamp >= self.MAX_SIZE:
            self.removeTail()

        cur = self.head

        while cur is not None:

            nex = cur.next
            curData = cur.data

            #Check if next two nodes exists
            if nex is not None and nex.next is not None:
                megaNex = nex.next
                #Check if next two nodes have same values as current
                if curData == nex.data and nex.data == megaNex.data:

                    #Merge the values to latest Bucket
                    nex.doubleData( )
                    #Remove the older bucket
                    nex.next = megaNex.next

            
            cur = nex
            
    """
        Just a demo example to start quickly
        with window size = 40
    """
    def demoStart(self):
        self.MAX_SIZE = 40
        b1 = Bucket(98 , 1)
        b2 = Bucket(95 , 2)
        b3 = Bucket(92 , 2)
        b4 = Bucket(87 , 4)
        b5 = Bucket(80 , 8)
        b6 = Bucket(65 , 8)

        self.head = b1
        self.tail = b6

        b1.next = b2
        b2.next = b3
        b3.next = b4
        b4.next = b5
        b5.next = b6

        return "Demo List Made"


# Demo Testing for last k = 4 bits
S = '10100101011011'
k = 4
dg = DGIM(k)

for i,s in enumerate( list(S) ):
    
    if s == '1':
        dg.add(i+1)
    
print("last k" , k , "bits has approx ", dg.getSum() , ' ones ')


"""
Output:

current state : (time: 6 - value: 1) => (time: 3 - value: 1) => (time: 1 - value: 1) => 
removing => (time: 1 - value: 1)
current state : (time: 8 - value: 1) => (time: 6 - value: 1) => (time: 3 - value: 1) => 
removing => (time: 3 - value: 1)
current state : (time: 10 - value: 1) => (time: 8 - value: 1) => (time: 6 - value: 1) => 
removing => (time: 6 - value: 1)
current state : (time: 13 - value: 1) => (time: 11 - value: 1) => (time: 10 - value: 2) => 
removing => (time: 10 - value: 2)
last k 4 bits has approx  3  ones

"""