# precondition: l is a nonempty list of numbers
# postcondition: returns the smallest value in l
def FindMin(l):
    m = l[0]
    i = 1

    # Loop invariant: m = min l[0:i] (including 0 but excluding i)
    # AND i<= len(l)
    while i<len(l):
        if l[i]<m:
            m = l[i]
        i += 1
    # loop postcondition m = min l
    # (implied by i>= len(l) AND the invariant))
    return m
