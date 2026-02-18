from qiskit import QuantumCircuit
from qiskit.circuit import QuantumRegister, ClassicalRegister

qc = QuantumCircuit(2)
qc.qubits

qr1 = QuantumRegister(2, "qreq1")
qr2 = QuantumRegister(1, "qreq2")
qr3 = QuantumRegister(3, "creg1")

combined_circ = QuantumCircuit(qr1, qr2, qr3)

combined_circ.qubits