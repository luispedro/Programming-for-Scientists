from pylab import *
X=linspace(0,1,1000)
def sigm(X,loc,lam):
    return 1./(1.+exp( - (X-loc) * lam))
plot(X,1-.6*sigm(X,.2,1000)+sigm(X,.5,20)+sigm(X,.6,30))
ylim(0,3)
xlabel(r'Time $\rightarrow$')
ylabel('Productivity')

xticks((0,.2,.8,1.),('Current','Learn New Thing','Use if Effectively',''))
yticks((),())

savefig('energybarrier.pdf')
