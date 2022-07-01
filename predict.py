

def predict(feature):
    prob = []
    label = []
    for i in range(len(feature['CL_NO'])):
        prob.append(0.5)
        label.append(1)

    return prob, label