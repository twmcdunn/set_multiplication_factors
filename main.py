
def all_sets(card, set = []):
    if len(set) == card:
        set.sort()
        return [set]
    compSets = []
    for i in range(12):
        if i not in set:
            set_copy = set.copy()
            set_copy.append(i)
            compSets.extend(all_sets(card, set_copy))
    return compSets

def normal_order(set):
    rotations = []
    for first in range(len(set)):
        rot = []
        for i in range(len(set)):
            rot.append(set[(first + i) % len(set)])
        rotations.append(rot)
    for i in range(len(rotations)):
        rotations[i] = transToZero(rotations[i])
    bestOrds = rotations
    while True:
        for interval in range(len(set)):
            best = 1000 # dummy value
            for s in bestOrds:
                i = s[len(set) - 1 - interval] - s[0]
                if i < 0:
                    i += 12
                best = min(best, i)
            bestOrdsNarrowed = []
            for s in bestOrds:
                i = s[len(set) - 1 - interval] - s[0]
                if i < 0:
                    i += 12
                if i == best and s not in bestOrdsNarrowed:
                    bestOrdsNarrowed.append(s)
            bestOrds = bestOrdsNarrowed
        if len(bestOrds) == 1:
            return bestOrds[0]
        
        
def transToZero(set):
    transSet = []
    for i in range(len(set)):
        transSet.append((set[i] + 12 - set[0]) % 12)
    return transSet

def uniqueSets(card):
    allSets = all_sets(card)
    uniqueSets = []
    for set in allSets:
        s = normal_order(set)
        if s not in uniqueSets:
            uniqueSets.append(s)
    return uniqueSets

def isCompProd(set1, set2):
    prod = []
    for i in range(len(set1)):
        for n in range(len(set2)):
            sum = (set1[i] + set2[n]) % 12
            if sum not in prod:
                prod.append(sum)
            else:
                return False
    return True

def allMultiples(seta, setb, mult = []):
    if len(mult) == len(seta):
        return [mult]
    mult1 = mult.copy()
    mult1.append(seta)
    options1 = allMultiples(seta,setb,mult1)
    mult2 = mult.copy()
    mult2.append(setb)
    options2 = allMultiples(seta,setb,mult2)
    options1.extend(options2)
    return options1

#print(allMultiples([0,1],[2,3,4]))

allowReps = False

def canFormAgg(seta, setb):
    set1 = seta

    allMult = allMultiples(seta,setb)
    workingMults = []
    for mult in allMult:
        prod = []
        reps = False
        for i in range(len(set1)):
            set2 = mult[i]
            for n in range(len(set2)):
                sum = (set1[i] + set2[n]) % 12
                if sum not in prod:
                    prod.append(sum)
                else:
                    reps = True
        if len(prod) == 12 and (not reps or allowReps):
            workingMults.append(mult)
    for mult in workingMults:
        mult.insert(0,seta)
    return workingMults

card4Sets = uniqueSets(4)
card3Sets = uniqueSets(3)
pairs = []
for card4Set in card4Sets:
    for card3Set in card3Sets:
        if(isCompProd(card4Set,card3Set)):
            pairs.append([card3Set,card4Set])

for p in pairs:
    print(p)

print()

pairs = []

#sets = []
#for card in range(3,5):
 #   sets.extend(uniqueSets(card))

allowReps = True

for setA in card4Sets:
    for setB in card3Sets:
        pairs.extend(canFormAgg(setA,setB))

for p in pairs:
    print(p)





