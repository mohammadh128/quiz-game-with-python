import random
import json
import os
from util import mathEvaluation

ans = {}
numQuestions = 20

for i in range(numQuestions):
    ans.setdefault("question", []).append(f"{random.randint(4, 9)}x{random.randint(6, 9)}" )    
    ans.setdefault("answer", []).append(random.randint(1,4))
    ans.setdefault("options", []).append([random.randint(35, 101) for _ in range(0,4)])
    trueAnswer = mathEvaluation(ans["question"][-1] )
    locAnswer = ans["answer"][-1] - 1

    while trueAnswer in ans["options"][-1]:
        indx = ans["options"][-1].index(trueAnswer)
        ans["options"][-1][indx] = random.randint(trueAnswer+1, 121)

    ans["options"][-1][ locAnswer ] = trueAnswer 

with open(os.path.join("data", "data.json"), "w") as f:
    json.dump(ans, f)
