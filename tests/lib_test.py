from dscalc.lib import sum, subtract, multiply

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


def test_multiply():
	#escolher os inputs dessa funcao
	a, b = 3, 5
	# deve saber qual é o output
	esperado = 15
	# deve ver se o que a gente consegue é o esperado
	conseguiu = multiply(a, b)
	# fazer os asserts
	assert esperado == conseguiu
	#escolher os inputs dessa funcao
	c, d = 5, 4
	# deve saber qual é o output
	expected = 20
	# deve ver se o que a gente consegue é o esperado
	got = multiply(c, d)
	# fazer os asserts
	assert expected == got

#hub create --> vai na minha conta e cria um repositorio na mao
# e faz conexao