import random
from math import exp
import numpy as np
import scipy.stats
import math

def exp_dist(d,L):
    '''
    p = exp_dist(x,lambda_)

    Returns the cpf the exponential distribution.

    See http://en.wikipedia.org/wiki/Exponential_distribution
    '''
    return scipy.stats.expon.sf(d,0,L)

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
    

very_sharp = np.r_[np.ones(40)*.2,np.ones(40)*.4,np.ones(40)*.6,np.ones(40)*.8,np.ones(40)*1.]
sharp      = np.r_[np.ones(40)*0.,np.ones(40)*.5,np.ones(40)*1.,np.ones(40)*.5,np.ones(40)*0.]
smooth     = np.linspace(0,2.,200)
p_reprod = .3

experiments = [
    ('fixed env. no sigma evolution',            1000,  0,np.ones(200)*.23),
    ('fixed env. w  sigma evolution',             500,500,np.ones(200)*.23),
    ('smooth changes env. w sigma evolution',     500,500,smooth),
    ('sharp changes env. w sigma evolution',      500,500,sharp),
    ('very sharp changes env. w sigma evolution', 500,500,very_sharp),
    ]
for name, initial_fixed, initial_evolve, environs in experiments:
    print 'Experiment',name
    population = [Bacteria(random.random(),random.random()) for i in xrange(initial_fixed)] +\
            [EvolveSigma(random.random(),random.random()) for i in xrange(initial_evolve)]
    simulate(population,environs,(initial_fixed+initial_evolve)*10,p_reprod)
    print 'Mean sigma:', np.mean([a.sigma for a in population])
    print 'Mean Adaptation:',np.mean([b.adaptation for b in population])
    print 'Fraction adaptative:', np.mean([type(b) == EvolveSigma for b in population])
    print


