import math
import os
import random
import re
import sys

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    #a node is said to be visited if its outorder vertices are all scanned
    visited=[0 for i in range(n)]
    #dist array stores the values of distance 
    dist=[0 for i in range(n)]
    rows,cols=n,n
    k=0
    arr=[[sys.maxsize for i in range(cols)] for j in range(rows)]
    for i in edges:
        if(arr[i[0]-1][i[1]-1]>edges[k][2]):
            arr[i[0]-1][i[1]-1]=edges[k][2]
            arr[i[1]-1][i[0]-1]=edges[k][2]
        k=k+1
    for i in range(n):
        visited[i]=0
        dist[i]=sys.maxsize
    dist[s-1]=0
    u=s-1
    
    for i in range(n):
        visited[u]=1
        for i in range(n):
            if(arr[u][i]!=sys.maxsize and visited[i]==0):
                if(dist[i]>dist[u]+arr[u][i]):
                    dist[i]=dist[u]+arr[u][i]
        minimum=sys.maxsize
        for i in range(n):
            if(dist[i]<minimum and visited[i]==0):
                u=i
                minimum=dist[i]
    lst=[]
    for i in range(n):
        if(i!=s-1 and dist[i]!=sys.maxsize):
            lst.append(dist[i])
        elif(i!=s-1 and dist[i]==sys.maxsize):
            lst.append(-1)
    return lst






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
    

'''
#sample input
#no of testcases
#n,m: no of vertices,no of edges
#m lines containing start vertex, end vertex, dist of edge
#s: source vertex
1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1

#sample output
24 3 15
'''

