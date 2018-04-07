# a formula is either a variable,
# or a NOT of a formula,
# or an AND of two formulas
# or an OR of two formulas
def NOT(f):
    return ["not", f]
def AND(f1, f2):
    return [f1, "and", f2]
def OR(f1, f2):
    return [f1, "or", f2]

# example formula
f = AND(OR("a", NOT("b")), OR("c", "d"))
print(f)

# a model will be represented as a python dictionary, mapping variables
# to Boolean values

# example model
model = {"a":True, "b":False, "c":False, "d":True}

# evaluates a formula on a given model
def eval(f, model):
    if type(f)==str:
        return model[f]
    if type(f)==list and len(f)==2 and f[0]=="not":
       return not eval(f[1], model)
    if type(f)==list and len(f)==3 and f[1]=="and":
        return eval(f[0], model) and eval(f[2], model)
    if type(f)==list and len(f)==3 and f[1]=="or":
        return eval(f[0], model) or eval(f[2], model)

#evaluation of the example formula on the example model    
print(eval (f, model))

# generate all possible models for a given list of variables
# Each model is a dictionary mapping variables from the list to values
# Returns the list of all models for the given variable list
def genModels(variablesList):
    # base case: there is only one model -- the empty model
    if len(variablesList) == 0: return [{}]

    # inductive case: first generate all possibles for all but one variables
    models = genModels(variablesList[:-1])

    # Each model for all the variables can be obtained by taking a model
    # for all but one of the variables and then adding to it both options
    # for the last variable to get two new models
    ret = []
    for model in models:
        # we copy the model, because we need m1 and m2
        # to be separate -- else, we can't have both
        # last variable = False and last variable = True
        m1 = model
        m2 = model.copy()
        m1[variablesList[-1]]=False
        m2[variablesList[-1]]=True       
        ret.append(m1)
        ret.append(m2)
    return ret

        
# generate all models for four variables
# and evaluate the example formula on each model
for model in genModels(["a", "b", "c", "d"]):
    print (model, eval(f, model))
