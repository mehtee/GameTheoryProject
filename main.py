from cmath import inf
import numpy as np

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