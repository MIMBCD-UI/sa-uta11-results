interns = [1,2,3,4,8,10]

juniors = [5,6,7,9]

seniors = [11,12,13,14,15,16]


assertive = [1,2,5,7,9,12,15,17,19,21,22,23,26,28,30,31,32,36,37,38,42,45,46,47]

non_assertive = [3,4,6,8,10,11,13,14,16,18,20,24,25,27,29,33,34,35,38,40,41,43,44,48]

proactive = [1,3,4,5,9,11,14,16,17,21,22,24,27,28,29,32,34,36,37,39,40,42,44,47]

reactive = [2,6,7,8,10,12,13,15,18,19,20,23,25,26,30,31,33,35,38,41,43,45,46,48]


groups_assertiveness = ["Novice Assertive", "Novice Non Assertive", "Expert Assertive", "Expert Non Assertive"]
groups_behaviour = ["Novice Proactive", "Novice Reactive", "Expert Proactive", "Expert Reactive"]

def getScenarios(clinicians):
    new_scenarios = []
    for i in clinicians:
        new_scenarios.extend([(i - 1) * 3, (i - 1) * 3 + 1, (i - 1) * 3 + 2])
    return new_scenarios