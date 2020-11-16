from dscalc.lib import sum, subtract 

def test_sum():
	#escolher os inputs dessa funcao
	a, b = 2, 2
	# deve saber qual é o output
	esperado = 4
	# deve ver se o que a gente consegue é o esperado
	conseguiu = sum(a, b)
	# fazer os asserts
	assert esperado == conseguiu
	#escolher os inputs dessa funcao
	c, d = 5, 4
	# deve saber qual é o output
	expected = 9
	# deve ver se o que a gente consegue é o esperado
	got = sum(c, d)
	# fazer os asserts
	assert expected == got

def test_subtract():
	#escolher os inputs dessa funcao
	a, b = 2, 2
	# deve saber qual é o output
	esperado = 0
	# deve ver se o que a gente consegue é o esperado
	conseguiu = subtract(a, b)
	# fazer os asserts
	assert esperado == conseguiu
	#escolher os inputs dessa funcao
	c, d = 5, 4
	# deve saber qual é o output
	expected = 1
	# deve ver se o que a gente consegue é o esperado
	got = subtract(c, d)
	# fazer os asserts
	assert expected == got

