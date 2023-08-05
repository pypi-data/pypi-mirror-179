
import numpy as np
import matplotlib.pyplot as plt



def basic_test(S):
    '''Test the model with a basic test'''
    print(S)
    W=S.wealths

    print('\n')
    #check wealths add up to 1 print True if np.sum(W)==1 else False
    print('Sum of wealths: ',np.sum(W),'\t',True if np.sum(W)==1 else False)
    #reset the sistem with uniform wealths S.reset()
    S.reset('equal')
    W=S.wealths
    #check all wealths are equal print True if np.all(W==1/len(W)) else False
    print('All wealths equal: ',np.all(W==1/len(W)),'\t',True if np.all(W==1/len(W)) else False)
    #print initial gini
    print('Initial Gini: ',S.Gini())

    S.termalize(1000)

    #print final gini
    print('Final Gini: ',S.Gini())


    #Wealths distribution
    W=S.wealths
    fig,Ax=plt.subplots(1,2,figsize=(12,4))
    Ax[0].hist(W,bins=100)
    Ax[0].set_title('Wealths')
    #loglog plot
    Ax[1].loglog(np.sort(W),np.linspace(1,0,len(W)),'o')
    Ax[1].set_title('Wealths (loglog)')
    fig.suptitle('Wealths distribution',fontsize=16)
    fig.tight_layout()
    plt.show()


    #Wealths evolution follow an agent
    Wi=S.follow(100,agent=10)

    fig, ax=plt.subplots(1,1,figsize=(6,4))
    ax.plot(Wi)
    ax.set_title('Wealth of agent 5')
    ax.set_xlabel('time')
    ax.set_ylabel('wealth')
    fig.suptitle('Following an Agent',fontsize=16)
    fig.tight_layout()
    plt.show()


    #Epoch of mean wealth
    W=S.epoch(1000) 
    fig,ax=plt.subplots(1,1,figsize=(6,4))
    ax.hist(W,bins=30)
    ax.set_title('Mean Wealths')
    ax.set_xlabel('Wealth')
    ax.set_ylabel('Frequency')
    fig.suptitle('Epoch of mean wealth',fontsize=16)
    fig.tight_layout()
    plt.show()



    #Setting wealth by idx
    fig,Ax=plt.subplots(1,2,figsize=(12,4))
    S.reset('equal')
    W=S.wealths
    Ax[0].hist(W,bins=20)
    Ax[0].set_yscale('log')
    Ax[0].set_title('Wealths equal')
    S.set_wealth_by_idx([0,1,2,3,5,6,7,8,9,10],[0,.1,.2,.3,.5,.6,.7,.8,.9,1])
    W=S.wealths
    Ax[1].hist(W,bins=20)
    Ax[1].set_yscale('log')
    Ax[1].set_title('Wealths setted')
    fig.suptitle('Setting wealth by idx',fontsize=16)
    fig.tight_layout()
    plt.show()

def n_basic_test(S):
        
    print(S,'\n')
    print('Get Graph size =',S.get_graphSize())
    S.termalize(1000)
    #check S.wealths.size == S.get_graphSize()[0]*S.get_graphSize()[1]
    print('# of welaths == sistem size ',S.wealths.size == S.get_graphSize()[0]*S.get_graphSize()[1],'\n')
    Ginis = S.Gini()
    print(f'# Ginis: {Ginis.size} {Ginis.size==S.get_graphSize()[1]} \n',Ginis,'\n')
    print('Average Gini: ',np.mean(S.Gini()),' Std: ',np.std(S.Gini()))
