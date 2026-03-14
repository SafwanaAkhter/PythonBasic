weight = input('Weight: ' )
weight_lbs_kg=input('(L)bs or (K)g: ' )
if weight_lbs_kg=='l':
    K = float(weight) * 0.45
    print(f"you are {K} kg ")
elif weight_lbs_kg=='k':
    L= float(weight)/0.45
    print(f"you are {L} pounds ")
