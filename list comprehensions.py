'''
You are given three integers x,y,z and n representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (x+y+z)is not equal to n.
'''



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    a=[]
    for i in range(0,(x+1)):
        for j in range(0,(y+1)):
            for q in range(0,(z+1)):
                if (i+j+q)!=n:
                    a.append([i,j,q])
    print (a)
        
