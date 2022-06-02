interns = [1,2,3,4,8,10]

juniors = [5,6,7,9]

seniors = [11,12,13,14,15,16]


def getScenarios(clinicians):
    new_scenarios = []
    for i in clinicians:
        new_scenarios.extend([(i - 1) * 3, (i - 1) * 3 + 1, (i - 1) * 3 + 2])

    return new_scenarios