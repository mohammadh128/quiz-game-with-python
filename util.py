"""
Math evaluation used by app.py and generate.py
"""

def mathEvaluation(numberedQuestion):
	return eval(numberedQuestion.split()[-1].replace("x","*") )