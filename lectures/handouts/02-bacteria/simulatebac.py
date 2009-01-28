import random
import bacteria

def mean(values):
    '''
    mu = mean(values)

    Compute a mean value.
    '''
    return sum(values)/float(len(values))

fixed = [.234]*200
sharp = [.2] * 40 + [.4]*40 + [.6]*40 + [.8]*40 + [1.]*40
very_sharp = [.0] * 40 + [.5]*40 + [1.]*40 + [.5]*40 + [0.]*40
smooth     = [.01*i for i in xrange(200)]
p_reprod = .3

experiments = [
    ('fixed env. no sigma evolution',            1000,  0,fixed),
    ('fixed env. w  sigma evolution',             500,500,fixed),
    ('smooth changes env. w sigma evolution',     500,500,smooth),
    ('sharp changes env. w sigma evolution',      500,500,sharp),
    ('very sharp changes env. w sigma evolution', 500,500,very_sharp),
    ]
for name, initial_fixed, initial_evolve, environs in experiments:
    print 'Experiment',name
    population = [bacteria.Bacteria(random.random(),random.random()) for i in xrange(initial_fixed)] +\
            [bacteria.EvolveSigma(random.random(),random.random()) for i in xrange(initial_evolve)]
    bacteria.simulate(population,environs,(initial_fixed+initial_evolve)*10,p_reprod)
    print 'Mean sigma:', mean([a.sigma for a in population])
    print 'Mean Adaptation:',mean([b.adaptation for b in population])
    print 'Fraction adaptative:', mean([type(b) == bacteria.EvolveSigma for b in population])
    print

