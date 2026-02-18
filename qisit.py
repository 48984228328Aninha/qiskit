from qiskit import QuantumCircuit
from qiskit.circuit import QuantumRegister, ClassicalRegister

qc = QuantumCircuit(2)
qc.qubits

qr1 = QuantumRegister(2, "qreq1")
qr2 = QuantumRegister(1, "qreq2")
qr3 = ClassicalRegister(3, "creg1")

combined_circ = QuantumCircuit(qr1, qr2, qr3)

combined_circ.qubits

combined_circ.h(qr1)

combined_circ.measure(qr1[0], qr3[0])
combined_circ.measure(qr1[1], qr3[1])
combined_circ.measure(qr2[0], qr3[2])

print(combined_circ.draw)

desired_qubit = qr2[0]
print("Index:", combined_circ.find_bit(desired_qubit).index)
print("Register", combined_circ.find_bit(desired_qubit).registers)