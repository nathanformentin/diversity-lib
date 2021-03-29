from math import sqrt
from math import ceil
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def matrix_generator(predict1,predict2,correct_answer,visualize):
    N00 = 0
    N01 = 0
    N10 = 0
    N11 = 0
    if len(predict1) != len(correct_answer) or len(predict2) != len(correct_answer):
        raise ValueError(
            'Vectors size do not match.'
        )
    for instance in range(len(predict1)):
        if predict1[instance] == predict2[instance]:
            if predict1[instance] == correct_answer[instance]:
                N11 += 1
            else:
                N00 += 1
        else:
            if predict1[instance] == correct_answer[instance]: 
                N10 += 1
            else:
                if predict2[instance] == correct_answer[instance]: #se fosse binario nao precisaria esse teste, mas esse algoritmo ja serve para problemas multiclasse.
                    N01 += 1 
    if visualize == True:
        data = [{'classifier 1 correct': N11, 'classifier 1 wrong': N01}, {'classifier 1 correct':N10,'classifier 1 wrong': N00}]
        table = pd.DataFrame(data,index=['classifier 2 correct','classifier 2 wrong'])
        return N00,N01,N10,N11,table
    else:
        return N00,N01,N10,N11


def pw_double_fault_measure(predict1,predict2,correct_answer):
    N00, _, _, _ = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    return (N00/
            len(predict1)
    

def pw_q_statistic(predict1,predict2,correct_answer): #n11*n00 - n01*n10 / n11*n00 + n01*n10
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    return ((N11*N00 -
             N01*N10) /
            (N11*N00+
             N01*N10))
 
                 
def disagreement(predict1,predict2,correct_answer):
    _, N01, N10, _ = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    return (N01 + N10) /
            len(predict1)

def pw_agreement(predict1,predict2,correct_answer):
    N00, _, _, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    return (N11 + N00) /
            len(predict1)

def p_correlation(predict1,predict2,correct_answer):
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    return (N11*N00 -
            N01*N10) /
            sqrt((N11+N10) *
                 (N01+N00) *
                 (N11*N01) *
                 (N10+N00))


def avg_disagreement(predicts_vector,correct_answer):
    clf1 = 0
    clf2 = clf1 + 1
    disagreement_sum = 0
    for clf1 in range(clf1,len(predicts_vector)):
        for clf2 in range(clf1+1,len(predicts_vector)):
            disagreement_sum += disagreement(predicts_vector[clf1],predicts_vector[clf2],correct_answer)
    return ((2*disagreement_sum) /
            (len(predicts_vector) * 
             (len(predicts_vector)-1)))

def kohavi_wolpert_variance(n_class,avg_disagreement):
    return (((n_class-1)* 
             avg_disagreement) /
            (2*n_class))

def entropy_measure(predicts_vector,correct_answer):
    corrects = 0
    n_classifiers = len(predicts_vector)
    n_classes = len(set(correct_answer))
    for instance in range(len(predicts_vector[0])):
        for classifier in range(n_classifiers):
            if predicts_vector[classifier][instance] == correct_answer[instance]:
                corrects +=1
        less_frequent = min(corrects,n_classifiers-corrects)
        accumulated_entropy = less_frequent/((n_classes)-ceil(n_classes/2))
        corrects = 0
    entropy = (accumulated_entropy /
               len(predicts_vector[0]))
    return entropy

def difficulty_measure(predicts_vector,correct_answer):
    bars = [0]*(len((predicts_vector))+1) #Considering that all classes are represented in the test vector
    corrects = 0
    for instance in range(len(predicts_vector[0])):
        for classifier in range(len(predicts_vector)):
            if predicts_vector[classifier][instance] == correct_answer[instance]:
                corrects +=1
        bars[corrects] += 1
        corrects = 0
    plt.hist(bars)
    plt.legend()
    plt.title('Prediction Distribution Over Instances')
    plt.xlabel('Hypothesis')
    plt.ylabel('Occurrences')
    plt.ylim(0, len(predicts_vector[0]))
    plt.xlim(0,len(bars)-1)
    plt.show()
