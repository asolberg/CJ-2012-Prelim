# Problem
# 
# You're watching a show where Googlers (employees of Google) dance, and then each dancer is
# given a triplet of scores by three judges. Each triplet of scores consists of three
# integer scores from 0 to 10 inclusive. The judges have very similar standards, so it's
# surprising if a triplet of scores contains two scores that are 2 apart. No triplet of
# scores contains scores that are more than 2 apart.
# 
# For example: (8, 8, 8) and (7, 8, 7) are not surprising. (6, 7, 8) and (6, 8, 8) are
# surprising. (7, 6, 9) will never happen.
# 
# The total points for a Googler is the sum of the three scores in that Googler's triplet of
# scores. The best result for a Googler is the maximum of the three scores in that Googler's
# triplet of scores. Given the total points for each Googler, as well as the number of
# surprising triplets of scores, what is the maximum number of Googlers that could have had
# a best result of at least p?
# 
# For example, suppose there were 6 Googlers, and they had the following total points: 29,
# 20, 8, 18, 18, 21. You remember that there were 2 surprising triplets of scores, and you
# want to know how many Googlers could have gotten a best result of 8 or better.
# 
# With those total points, and knowing that two of the triplets were surprising, the
# triplets of scores could have been:

def search(totals, p):
    combos = []
    current_combo = []
    for c in range(len(totals)):
        combos.append(list())
        for i in range(11):
            for j in range(11):
                for k in range(11):
                    current_combo = [i, j, k]
#                    print("Trying Googler #%d, Combo %s" % ((c+1), str(current_combo)))
                    if (sum(current_combo) == totals[c] and max(current_combo) >= p and
                    abs(current_combo[0]-current_combo[1])<=2 and 
                    abs(current_combo[0]-current_combo[2])<=2 and 
                    abs(current_combo[1]-current_combo[2])<=2):
                        try:
                            combos[c].append(tuple(current_combo))
#                            print("len of combos: %d" %len(combos))
#                            print("Googler #%d - Appending score: %s" % ((c+1), str(current_combo)))
                        except:
#                            print("C=%d and Length of combo list: %d" % (c, len(combos)))
                            combos.append(list())
                            combos[c].append(tuple(current_combo))
#                            print("Googler #%d - Extending List, appending score: %s" % ((c+1), str(current_combo)))

                    k+=1
                j+=1
            i+=1
    return combos

def NumberOfAllSurprises(combos):
    all_surprises=0
    winning_scores=[]
    num_blank_scores = 0
#    print("Combos: %s" % str(combos))
#    print("len of combos= %d" %len(combos))
    for c in range(len(combos)):
        winning_scores.append(list())
        if len(combos[c]) ==0:
            num_blank_scores +=1
        for score in combos[c]:
#            print("googler %d - trying score: %s" % ((c+1), str(score)))
            if (abs(score[0]-score[1])<=1 and 
                abs(score[0]-score[2])<=1 and 
                abs(score[1]-score[2])<=1):
                winning_scores[c].append(tuple(score))
                continue
        if (combos[c] and (len(winning_scores[c]) == 0)):
            all_surprises+=1
#    print("winning scores: %s, blank scores: %d, all surprises: %d" % (str(winning_scores), num_blank_scores, all_surprises))
    return all_surprises
                
                    
                    
                        

filePrefix = 'B-small-attempt0'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())
combs = []
for i in range(T):
    N, S, p, *t = [int(x) for x in fin.readline().split()]
#    print("N=%d" %N)
    combos = search(t, p)
#    print("Number of Googlers: %d" %len(combos))
#    for googler in combos:
#        print("Len of scores: %d" % len(googler))
    all_surprises=NumberOfAllSurprises(combos)
#    print("All Surprises = %d" % all_surprises)
    if all_surprises > S:
        deduction = all_surprises-S
    else:
        deduction = 0
    non_empty_scores = 0
    for googler in combos:
        if len(googler)>0:
            non_empty_scores +=1
#    print("Non-empty scores: %d" % non_empty_scores)
    if non_empty_scores - deduction <= 0:
        answer = 0
    else:
        answer = non_empty_scores-deduction    
    print("Case #%d: %d" % ((i+1), answer))
    fout.write("Case #%d: %d\n" % ((i+1), answer))