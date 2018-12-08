import scipy
import numpy as np
from matplotlib.pyplot import *
import pylab as plt
def print_result(l, solutions, reserved):    
    z = np.zeros(l)                         
    checker = 0                             
    for i,item in enumerate(z):
        if i in reserved:
            z[i] = solutions[checker]
            checker += 1
    return z 
    from scipy.optimize import linprog
    def chiststr(matrix):
    results = []
    for i,item in enumerate(matrix):
        minimum=min(item)
        indexes = list(np.where(np.array(item)==minimum))[0]
        for ind in indexes:
            jtem = np.array(matrix).T[ind]
            maximum = max(jtem)
            if maximum == minimum:
                results.append((i,ind))
                result = maximum
    if results != []:
        return(result, results[0])
    else: return False
    def show_result(pl1, pl2, r):
    print("""strategy of the first player is: %s
strategy of the first player is: %s
value of the game is: %s""" % (str(pl1), str(pl2), r))
 
    markerline, stemlines, baseline = plt.stem(range(1,len(pl1)+1),pl1, '-.')
    plt.setp(baseline, color='r', linewidth=2)
    plt.xlim(0,len(pl1)+2)
    plt.ylim(0,(max(pl1)+1))
    plt.show()
    figure()
 
    markerline, stemlines, baseline = plt.stem(range(1,len(pl2)+1),pl2, '-.')
    plt.setp(baseline, color='r', linewidth=2)
    plt.xlim(0,len(pl2)+2)
    plt.ylim(0,(max(pl2)+1))
    plt.show()
    def nashequilibrium(matrix):
    matrix=np.array(matrix)
    rows=len(matrix)
    cols=len(matrix.T)
    
     
    if not chiststr(matrix):
        pass
    else:
        val,pair = chiststr(matrix)
        player1=print_result(cols, [1],[pair[0]] )
        player2=print_result(rows, [1],[pair[1]] )
        return (player1, player2, val)
    minim=matrix.min()
    pok=False
    if minim<=0:
            matrix=matrix-minim+1
            pok=True
    c=np.array([-1]*cols)
    b=np.array([1]*rows)
    
     
    res=linprog(c,matrix,b)
     
    player2=np.array(res.x)
      
    val=1/(player2.sum())
    player2=player2*val
    matrix=-matrix.transpose()
    c=np.array([1]*rows)
    b=np.array([-1]*cols)
 
    res=linprog(c,matrix,b)
   
    player1=np.array(res.x)
    val=1/(player1.sum())
    player1=player1*val
    if pok==True:
        val=val+minim-1
    return(player1, player2, val)
    m = [[7,-1,-4,1],[4,2,3,2],[2,2,5,2],[4,-3,7,-2]]
    pl1, pl2, r = nashequilibrium(m)
 
    show_result(pl1, pl2, r)
    m=[[0,3,4],[2,1,-3]]
    pl1, pl2, r = nashequilibrium(m)
    show_result(pl1, pl2, r)
    m=[[4,0,6,2,2,1],[3,8,4,10,4,4],[1,2,6,5,0,0],[6,6,4,4,10,3],[10,4,6,4,0,9],[10,7,0,7,9,8]]
    pl1, pl2, r = nashequilibrium(m)
    show_result(pl1, pl2, r)
    m=[[1,4,6,3],[3,1,2,4],[2,3,4,3],[0,1,5,2]]
    pl1, pl2, r = nashequilibrium(m)
    show_result(pl1, pl2, r)
