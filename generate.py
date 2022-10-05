import math
import random
import json
import os
from util import mathEvaluation

ans = {}
numQuestions = 150
numOptions = 4
mathFacts = {
    'x': 0.20,
    '+': 0.20,
    '/': 0.20,
    '-': 0.20,
    '÷': 0.10,
    '%': 0.10
}
bounds = (2, 9)

def chooseFact():
    nowLikelihood = 0.0
    chance = random.random()
    for fact, likelihood in mathFacts.items():
        nowLikelihood += likelihood
        if fact and chance <= nowLikelihood:
            return fact
    return random.choice(list(mathFacts.keys()))


def generate():
    for i in range(numQuestions):
        factoid = chooseFact()
        if factoid in ['/', '÷']:
            divisor = random.randint(*bounds)
            dividend = divisor * random.randint(*bounds)
            questionStr = f"{dividend} {factoid} {divisor}"
        else:
            questionStr = f"{random.randint(*bounds)} {factoid} {random.randint(*bounds)}"
        ans.setdefault("question", []).append(f"  {questionStr}" )    
        ans.setdefault("answer", []).append(random.randint(1, numOptions))
        ans.setdefault("options", []).append([random.randint(*bounds)**2 for _ in range(numOptions)])
        trueAnswer = mathEvaluation(ans["question"][-1] )
        locAnswer = ans["answer"][-1] - 1

        # make sure answer doesn't appear twice.
        while trueAnswer in ans["options"][-1]:
            indx = ans["options"][-1].index(trueAnswer)
            ans["options"][-1][indx] = random.randint(trueAnswer+1, (trueAnswer+1)*3)
        ans["options"][-1][ locAnswer ] = trueAnswer 

    with open(os.path.join("data", "data.json"), "w") as f:
        json.dump(ans, f)

if __name__ == "__main__":
    generate()