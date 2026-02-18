# QISKIT
Um repositório para estudar a linguagem qiskit e construir circuitos utilizando um hardware comum. Meu objetivo é ir do zero até o mais avançado neste repositório, sempre documentando minhas mudanças.

### - Link da documentação oficial utilizada para estudo: 
- https://quantum.cloud.ibm.com/docs/pt/guides/construct-circuits
### - Link da documentação para transpilador: 
-https://quantum.cloud.ibm.com/docs/pt/guides/construct-circuits
### - Link para documentação do estimador: 
-https://quantum.cloud.ibm.com/docs/pt/guides/get-started-with-primitives

- Site utilizado: IBM Quantum Learning.

# Bibliotecas
- QuantumCircuit
- QuantumRegister
- ClassicalRegister

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
Passo a passo: utilizar a biblioteca  QuantumRegister
```
qr1 = QuantumRegister(2, "qreq1")
qr2 = QuantumRegister(1, "qreq2")
qr3 = ClassicalRegister(3, "creg1")

combined_circ = QuantumCircuit(qr1, qr2, qr3)

combined_circ.qubits
```

- [x] Encontrar índice e registro de um qubit com find_bit()
Passo a passo: combined_circ.qubits() mostra todos os qubits.
```
desired_qubit = qr2[0]
print("Index:", combined_circ.find_bit(desired_qubit).index)
print("Register", combined_circ.find_bit(desired_qubit).registers)
```

