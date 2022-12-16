
from numpy import array, dot, diagflat   
class Subgradient:
    """
    An ascent direction 
        
        f(x + t * d) >= f(x) + t * d
    
    where 0 < t and  t_i converge to zero but sum (t_i) converge to infinitive.
    d is the Ascent direction. 
    

    """
    
    def __init__( self,a=1,b=0,k=0, tfactor=0.2 ):
        self.a=a
        self.b=b
        self.k=0
        self.f_best=[-100000]        
        self.tfactor = max( min( tfactor, 0.999), 1.0e-3 )
        return

    def __test__( self, f, x, d, t = 0.1):
        """
        Given a ascent direction d for function f at the
        current iterate x, see if the steplength t satisfies 
        f( x + t * d ) >= f_best + t * d.
        """      
        
        self.f_best.append(f( x + t * d(x) ))
        f_plus = f( x + t * d(x) )
        
        
        return ( f_plus >=max(self.f_best[0:-1]) )

    def search( self, f,x, d):
        """
        Given a ascent direction d for function f at the
        current iterate x, compute a steplength t such that
        f(x + t * d) >= f(x) + t * d satisfies. 
         """
        self.k+=1
        #if d <= 0.0:
            #raise ValueError, "Direction must be a ascent direction"
            #return None
        t = 0.1
        
        while not self.__test__( f, x, d, t = t):
            
            self.tfactor=self.a/(self.b+self.k)
            t *= self.tfactor
        return t

def norm_infty( x ):
    "Returns the infinity (or max) norm of x"
    return max( abs( x ) )

    
    #"convert list w to diagonal matrix and compute new weight."
    #d=diagflat(d)
    #dim=w.shape
    #for i in range(dim[0]):
        #for j in range(dim[1]):
            #d[i][j]=d_prim[i][j]+w_prim[i]+w_prim[j]
    #return 
 
# Test
if __name__ == '__main__':
    
     
    def f(x):
        return (-1)*(10.0 * (x[1]-x[0]**2)**2 + (1-x[0])**2)

    

    def d(x):
        return (-1)*array( [ -40.0 * (x[1] - x[0]**2) * x[0] - 2.0 * (1-x[0]),
                        20.0 * (x[1] - x[0]**2) ], 'd' )
    #def f(x):
        #return -(x[0]**2) 

    #def d(x):
        #return array( [ - 2.0 * x[0],0], 'd' )

    GAD = Subgradient()
    #x = array( [4,0], 'd' ) 
    x = array( [1.5, 1.0], 'd' )
    f_n=-1000
    t=0
    
    while abs(f(x)-f_n) >1.0e-5:
        f_n=f(x)
        t= GAD.search(f,x,d)
        x+=t*d(x)
        print abs(f(x)-f_n)
    
   
    
