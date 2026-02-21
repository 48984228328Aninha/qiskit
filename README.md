# QISKIT
Um repositório para estudar a linguagem qiskit e construir circuitos utilizando um hardware comum. Meu objetivo é ir do zero até o mais avançado neste repositório, sempre documentando minhas mudanças, é público e com o intuito de fazer outras pessoas aprenderem junto.

### - Link da documentação oficial utilizada para estudo: 
- https://quantum.cloud.ibm.com/docs/pt/guides/construct-circuits
### - Link da documentação para transpilador: 
- https://quantum.cloud.ibm.com/docs/pt/guides/construct-circuits
### - Link para documentação do estimador: 
- https://quantum.cloud.ibm.com/docs/pt/guides/get-started-with-primitives
### - Link documentação Qiskit supino:
- https://github.com/qiskit/benchpress

- Site utilizado: IBM Quantum Learning.

# Bibliotecas
- QuantumCircuit
- QuantumRegister
- ClassicalRegister

# Explicação simples antes de mexer com qubits.
- A computação clássica usa bits como 0 e 1.
- A computação quântica funciona como uma bússola, o estado será definido por um ponto em uma esfera e para mudar é necessário fazer uma rotação (imagine um plano cartesiano 3D com eixos x,y e z)
- U3 é uma matriz que leva a qualquer ponto somente com três coordenadas: U3(a, b, c)
a = rotação para cima
b = rotação para os lados
c = fase (ângulo)

<div align=center>
<img width="156" height="106" alt="image" src="https://github.com/user-attachments/assets/fca0817e-1fef-457f-a49d-35a9a83837bd" />
</div>


- É como se fosse ponteiros de um relógio! 

Primeiro passo
- [x] Criar um circuito com 2 qubits.
- Passo a passo: importar a biblioteca QuantumCircuit, sem registradores a princípio.
```
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.qubits
```
- [x] Criar um circuito utilizando QuantumRegister, similar a um registrador onde irão ficar os qubits.
```
from qiskit.circuit import QuantumRegister, ClassicalRegister

qr1 = QuantumRegister(2, "qreq1")
qr2 = QuantumRegister(1, "qreq2")
qr3 = QuantumRegister(3, "creg1")
```
- [x] Criar uma parte para guardar um bit clássico usando ClassicalRegister e guardar resultado das medições.
```
  qr3 = ClassicalRegister(3, "creg1")
```
- [x] Criar um circuito utilizando os três registradores.
- Passo a passo: utilizar a biblioteca  QuantumRegister
```
qr1 = QuantumRegister(2, "qreq1")
qr2 = QuantumRegister(1, "qreq2")
qr3 = ClassicalRegister(3, "creg1")

combined_circ = QuantumCircuit(qr1, qr2, qr3)

combined_circ.qubits
```

- [x] Encontrar índice e registro de um qubit com find_bit()
- Passo a passo: combined_circ.qubits() mostra todos os qubits.
```
desired_qubit = qr2[0]
print("Index:", combined_circ.find_bit(desired_qubit).index)
print("Register", combined_circ.find_bit(desired_qubit).registers)
```

- [x] Listar tudo o que existe no circuito e salvar em data
```
combined_circ.x(0)
combined_circ.data
```

- [x] Aplicar Hadamard, uma porta lógica.
```
combined_circ.h(qr1)
```

- [x] Medição de qubit
```
combined_circ.measure(qr1[0], qr3[0])
combined_circ.measure(qr1[1], qr3[1])
combined_circ.measure(qr2[0], qr3[2])
```

- [x] Localizar o primeiro registrador, focar no objeto dentro dele (o qubit) e acessar o circuito interno
```
qc.data[0].operation.definition.draw("mpl")
```

# Próximos passos:
- [] criar entrelaçamento
- [] circuito Bell State
- [] Percorrer qc.data em loop
- [] Listar todas as portas do circuito
- [] Modificar instruções manualmente
- [] Aplicar shots
- [] Bell State, ver 50/50

---------------------------------------------------------------------------

```
author: Amanda Rodrigues de Siqueira
```

