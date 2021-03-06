import numpy as np
import copy

n = int(input())
A = []
B = []

for i in range(n):
    Ai = list(map(int, input().split()))
    A.append(Ai)

for i in range(n):
    Bi = list(map(int, input().split()))
    B.append(Bi)

assert len(A) == len(B) and len(A[0]) == len(B[0])


def nash_eq(payoff1, payoff2):
    p1 = np.array(payoff1)
    c = 0
    maxes_p1 = []
    while c != len(p1[0]):
        max_indices_of_this_col = []
        col = p1[:, c]
        c += 1
        max_value_col = max(col)
        for i in range(len(col)):
            if col[i] == max_value_col:
                max_indices_of_this_col.append(i)
        maxes_p1.append(max_indices_of_this_col)

    p2 = np.array(payoff2)
    maxes_p2 = []
    for row in p2:
        max_indices_of_this_row = []
        max_value_row = max(row)
        for i in range(len(row)):
            if row[i] == max_value_row:
                max_indices_of_this_row.append(i)
        maxes_p2.append(max_indices_of_this_row)
    
    for i in range(len(maxes_p2)):
        row = maxes_p2[i]
        for j in row:
            mp2 = maxes_p1[j]
            if i in mp2:
                print(i + 1, ",", j + 1, sep="")

print("Pure nash equilibrium")
nash_eq(A, B)


def strongly_dominant_strategy(payoff, player):
    pnp = np.array(payoff)
    for i in range(len(payoff)):
        Payoff = copy.deepcopy(pnp)

        # player 1: row-wise
        if player == 1:
            iPayoff = copy.deepcopy(Payoff[i])
            Payoff = np.delete(Payoff, i, 0)
        
        # player 2: col-wise
        elif player == 2:
            iPayoff = copy.deepcopy(Payoff[:, i])
            Payoff = np.delete(Payoff, i, 1)

        isStrongly = True
        
        if player == 1:
            for p in Payoff:
                # the chosen strategies has to strongly dominate "all other" strategies
                if (iPayoff > p).all() == True:
                    pass
                else:
                    isStrongly = False
                    break
            
        elif player == 2:
            c = 0
            while c != len(Payoff[0]):
                p = Payoff[:, c]
                c += 1
                if (iPayoff > p).all() == True:
                    pass
                else:
                    isStrongly = False
                    break

        if isStrongly:
            return i + 1
        
print("Strongly dominant strategy player 1")
stronglyP1 = strongly_dominant_strategy(A, 1)
print(stronglyP1)
stronglyP2 = strongly_dominant_strategy(B, 2)
print("Strongly dominant strategy player 2")
print(stronglyP2)



def weakly_dominant_strategy(payoff, player):
    pnp = np.array(payoff)
    for i in range(len(payoff)):
        Payoff = copy.deepcopy(pnp)

        # player 1: row-wise
        if player == 1:
            iPayoff = copy.deepcopy(Payoff[i])
            Payoff = np.delete(Payoff, i, 0)
        
        # player 2: col-wise
        elif player == 2:
            iPayoff = copy.deepcopy(Payoff[:, i])
            Payoff = np.delete(Payoff, i, 1)

        isWeakly = True
        isWeaklyAkidan = False
        if player == 1:
            for p in Payoff:
                # the chosen strategies has to weakly dominate "all other" strategies
                if (iPayoff >= p).all() == True:
                    pass
                else:
                    isWeakly = False
                    break
            if isWeakly:
                for p in Payoff:
                    # one of strategies has to be strongly dominated by the chosen strategy
                    if (iPayoff > p).any() == True:
                        isWeaklyAkidan = True
                        break
            

        elif player == 2:
            c = 0
            while c != len(Payoff[0]):
                p = Payoff[:, c]
                c += 1
                if (iPayoff >= p).all() == True:
                    pass
                else:
                    isWeakly = False
                    break

            if isWeakly:
                c = 0
                while c != len(Payoff[0]):
                    p = Payoff[:, c]
                    c += 1
                    if (iPayoff > p).any() == True:
                        isWeaklyAkidan = True
                        break

        if isWeakly and isWeaklyAkidan:
            return i + 1

print("Weakly dominant strategy player 1")
weaklyP1 = weakly_dominant_strategy(A, 1)
print(weaklyP1)
print("Weakly dominant strategy player 2")
weaklyP2 = weakly_dominant_strategy(B, 2)
print(weaklyP2)

print("Strogly dominant strategy equilibrium")
if stronglyP1 != None and stronglyP2 != None:
    print(stronglyP1,",",stronglyP2, sep="")
else:
    print("None")
    
print("Weakly dominant strategy equilibrium")
if weaklyP1 != None and weaklyP2 != None:
    print(weaklyP1,",",weaklyP2, sep="")
else:
    print("None")

def maxmin(payoff, i):
    Anp = np.array(payoff)
    # Minimum of each row of payoff matrix (i.e. each strategy of player i)
    minimums_of_player = []

    # for each strategy of player i
    for iStrategy in range(n):
        # getting row of ith strategy of player i 
        # (all payoffs corresponding to the strategy i of player i)
        if i == 1: # if player 1, we should consider its row!
            Ai = Anp[iStrategy]
        elif i == 2: 
            Ai = Anp[:, iStrategy] # if player 2, we should consider its column!
        # minimum of those payoffs
        minAi = min(Ai)
        # adding to the min array
        minimums_of_player.append(minAi)
    # maximum of minimums
    max_val_player = max(minimums_of_player)
    # saving indices (1-based) of maxmin (i.e. the ith maxmin strategies)
    max_indices = []
    # search which elements' indices are those of that maxmin value:
    for index, element in enumerate(minimums_of_player):
        if element == max_val_player:
            # and appending each of them to the max_indices array
            max_indices.append(str(index+1))

    print("Maxmin values and strategy player", i)
    print(max_val_player, "-", ",".join(max_indices), sep="")

maxmin(A, 1)
maxmin(B, 2)


def minmax(payoff, i) -> tuple:
    Anp = np.array(payoff)

    # Maximum of each row/col of payoff matrix (i.e. each strategy of player i)
    maximum_of_player = []

    for iStrategy in range(n):
        # getting row/col of ith strategy of player i 
        # (all payoffs corresponding to the strategy i of player i)

        if i == 1: # if player 1, we should consider its column!
            Ai = Anp[:, iStrategy]
        elif i == 2: # if player 2, we should consider its row!
            Ai = Anp[iStrategy]
        
        # maximum of those payoffs
        maxAi = max(Ai)
        # adding to the max array
        maximum_of_player.append(maxAi)

    # minimum of maximums
    min_val_player = min(maximum_of_player)
    # saving indices (1-based) of minmax (i.e. the ith minmax strategies)
    min_indices = []
    # search which elements' indices are those of that minmax value:
    for index, element in enumerate(maximum_of_player):
            if element == min_val_player:
                # and appending each of them to the min_indices array
                min_indices.append(str(index+1))
    return min_val_player, min_indices

minmax_of_1 = minmax(A, 1)
minmax_of_2 = minmax(B, 2)

# strategy output of player 1 is the minmax strategy of player 2 and vice-versa
print("Minmax values and strategy player 1")
print(minmax_of_1[0], "-", ",".join(minmax_of_2[1]), sep="")

print("Minmax values and strategy player 2")
print(minmax_of_2[0], "-", ",".join(minmax_of_1[1]), sep="")