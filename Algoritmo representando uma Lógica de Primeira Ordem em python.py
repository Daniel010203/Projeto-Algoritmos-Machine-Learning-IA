from sympy import symbols, ForAll, Exists, And, Or, Not

# Definir variáveis
x, y = symbols('x y')

# Predicados
P = symbols('P', integer=True)
Q = symbols('Q', integer=True)

# Fórmulas de lógica de primeira ordem
formula1 = ForAll(x, P(x) >> Q(x))  # Para todo x, se P(x) então Q(x)
formula2 = Exists(x, P(x) & Q(x))  # Existe x tal que P(x) e Q(x)
formula3 = Or(P(x), Not(Q(y)))      # P(x) ou não Q(y)

# Exemplo de avaliação
modelo = {P(1): True, P(2): False, Q(1): True, Q(2): True}

print(f"A fórmula 1 é verdadeira no modelo? {formula1.subs(modelo)}")
print(f"A fórmula 2 é verdadeira no modelo? {formula2.subs(modelo)}")
print(f"A fórmula 3 é verdadeira no modelo? {formula3.subs(modelo)}")

# Neste exemplo, usamos sympypara criar fórmulas de lógica de primeira ordem e avaliá-las em um modelo específico. Observe que as variáveis P​​e Qsão tratadas como predicadas sobre inteiros. Você pode adaptar isso para representar predicados específicos do seu domínio.
#
# Se você estiver trabalhando com lógica de primeira ordem em contextos mais complexos, você pode precisar de bibliotecas mais especializadas ou ferramentas dedicadas. Este exemplo é uma introdução básica usando sympy.


Este código demonstra o uso da biblioteca SymPy em Python para manipulação e avaliação de expressões de lógica de primeira ordem. Vamos analisar linha por linha:

1. **`from sympy import symbols, ForAll, Exists, And, Or, Not`**: Importa símbolos e operadores lógicos necessários da biblioteca SymPy.
2. **`x, y = symbols('x y')`**: Define símbolos `x` e `y` para representar variáveis na lógica de primeira ordem.
3. **`P = symbols('P', integer=True)` e `Q = symbols('Q', integer=True)`**: Define os símbolos `P` e `Q` como predicados com a opção `integer=True`, indicando que eles representam funções inteiras.
4. **`formula1 = ForAll(x, P(x) >> Q(x))`**: Define uma fórmula de lógica de primeira ordem onde para todo `x`, `P(x)` implica `Q(x)` (`>>` representa a implicação lógica).
5. **`formula2 = Exists(x, P(x) & Q(x))`**: Define uma fórmula de lógica de primeira ordem onde existe algum `x` tal que `P(x)` e `Q(x)` são verdadeiros (`&` representa a conjunção lógica).
6. **`formula3 = Or(P(x), Not(Q(y)))`**: Define uma fórmula de lógica de primeira ordem onde `P(x)` é verdadeiro ou `Q(y)` é falso (`Or` representa a disjunção lógica e `Not` a negação).
7. **`modelo = {P(1): True, P(2): False, Q(1): True, Q(2): True}`**: Define um modelo que atribui valores de verdade aos predicados `P` e `Q` para os elementos 1 e 2.
8. **`print(f"A fórmula 1 é verdadeira no modelo? {formula1.subs(modelo)}")`**: Avalia se a `formula1` é verdadeira no modelo fornecido e imprime o resultado.
9. **`print(f"A fórmula 2 é verdadeira no modelo? {formula2.subs(modelo)}")`**: Avalia se a `formula2` é verdadeira no modelo fornecido e imprime o resultado.
10. **`print(f"A fórmula 3 é verdadeira no modelo? {formula3.subs(modelo)}")`**: Avalia se a `formula3` é verdadeira no modelo fornecido e imprime o resultado.
Isso basicamente executa uma série de testes para verificar se as expressões lógicas são verdadeiras ou falsas em relação a um modelo específico, fornecendo saídas correspondentes para cada teste.
