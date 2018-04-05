# precondition: a and b are nonnegative integers
# postcondition: returns gcd (a, b) if they are not simultaneously 0
# returns 0 if a=b=0
def Euclid(a, b):
    if a==b: return a
    # Postcondition from the line above: a!=b and a>=0 and b>=0
    if a<b: # swap so that a>b
        a, b = b, a
    # Postcondition from the above two lines:a>b
    # and (current a, current b) = (input a, input b) OR = (input b, input a)
    # and b>=0
    # (by case analysis from the "if" above)

    # Loop invariant:
    # I = "gcd(current a, current b) = gcd (input a, input b) and b>=0"
    # implied by the precondition above
    # ("b>0" AND I) imply I, so the invariant remains
    # true after each loop iteration

    while b>0:
        a, b = b, a%b

    # Postcondition from the loop above (implied by not(b>0) and I): b=0 and I
    # Equivalent to saying gcd (current a, 0) = gcd (input a, input b)
    # But gcd (current a, 0) = current a, so 
    # current a is the gcd (input a, input b) by transitivity

    return a
