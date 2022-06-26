
def mathEvaluation(numberedQuestion):
	"""
	Math evaluation of "7x8" used by app.py and generate.py
	"""
	return eval(numberedQuestion.replace("x","*").replace("÷", "/") )