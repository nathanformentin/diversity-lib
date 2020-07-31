from math import sqrt

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
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    df_measure = N00/N00+N01+N10+N11
    return df_measure

def pw_q_statistic(predict1,predict2,correct_answer): #n11*n00 - n01*n10 / n11*n00 + n01*n10
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    q_statistic = (N11*N00 - N01*N10)/(N11*N00+N01*N10)
    return q_statistic
                 
def disagreement(predict1,predict2,correct_answer):
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    disagreement = (N01 + N10) / (N11 + N10 + N01 + N00)
    return disagreement

def pw_agreement(predict1,predict2,correct_answer):
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    disagreement = (N11 + N00) / (N11 + N10 + N01 + N00)
    return agreement

def p_correlation(predict1,predict2,correct_answer):
    N00, N01, N10, N11 = matrix_generator(predict1,predict2,correct_answer,visualize=False)
    p_correlation = (N11*N00 - N01*N10) / sqrt((N11+N10)*(N01+N00)(N11*N01)*(N10+N00))
