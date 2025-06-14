class node:
    def __init__(self,data):
        self.left=None
        self.val=data
        self.right=None
def createBST(arr):
    root=None
    for data in arr:
        if(root==None):
            root=node(data)
        else:
            temp=root
            while(True):
                if(data<temp.val):
                    if(temp.left==None):
                        temp.left=node(data)
                        break
                    else:
                        temp=temp.left
                if(data>temp.val):
                    if(temp.right==None):
                        temp.right=node(data)
                        break
                    else:
                        temp=temp.right
    inorder(root)
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
arr=list(map(int,input().split(',')))
(createBST(arr))
