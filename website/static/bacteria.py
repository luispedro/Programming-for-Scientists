import random
from math import exp
import math

def exp_dist(d,L):
    '''
    p = exp_dist(x,lambda_)

    Returns the cpf the exponential distribution.

    See http://en.wikipedia.org/wiki/Exponential_distribution
    '''
    return 1-math.exp(-L*d)

class Bacteria(object):
    '''
    Bacteria
    
    Implements a simple bacterium

    Functions:
    ---------

      * P_dead(self,e): probability of death in environment e
      * reproduce(): returns a new bacterium
    '''
    L=.95
    def __init__(self,adaptation,sigma):
        self.adaptation = adaptation
        self.sigma = sigma
    def P_dead(self,e):
        '''
        p = b.P_dead(e)

        Probability of death in environment e (which should be a number)
        '''
        return exp_dist(abs(self.adaptation - e),self.L)
    def reproduce(self):
        '''
        b1 = b.reproduce()

        Return a child of this bacterium
        '''
        return Bacteria(self.adaptation + random.normalvariate(0,self.sigma),self.sigma)

class EvolveSigma(Bacteria):
    '''
    EvolveSigma

    EvolveSigma is a type of bacterium where the 
    sigma parameter evolves at reproduction.
    '''
    def __init__(self,adaptation,sigma):
        Bacteria.__init__(self,adaptation,sigma)

    def reproduce(self):
        return EvolveSigma(self.adaptation + random.normalvariate(0,self.sigma),
                    self.sigma+random.normalvariate(0.,self.sigma/2.))

def simulate(population,environs,max_population,p_reprod):
    '''
    simulate(population,environs)

    Simulate iters iterations of evolution.
    '''
    for environ in environs:
        ai = 0
        while ai < len(population):
            if population[ai].P_dead(environ) < random.random():
                del population[ai]
            else:
                ai += 1
        N = len(population)
        for ai in xrange(N):
            if random.random() < p_reprod:
                population.append(population[ai].reproduce())
        if N >= max_population:
            random.shuffle(population)
            while len(population) >= max_population:
                population.pop()


