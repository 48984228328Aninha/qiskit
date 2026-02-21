from qiskit import QuantumCircuit
from qiskit.circuit import QuantumRegister, ClassicalRegister
from qiskit.circuit.library import HGate

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



desired_qubit = qr2[0]
print("Index:", combined_circ.find_bit(desired_qubit).index)
print("Register", combined_circ.find_bit(desired_qubit).registers)

combined_circ.x(0)
combined_circ.data
print(combined_circ.draw)

qc.data[0].operation.definition.draw("mpl")


qc = QuantumCircuit(1)
qc.append(
    HGate(),
    [0],
)
qc.draw("mpl")

qc_a = QuantumCircuit(4)

qc_a.x(0)

qc_b = QuantumCircuit(2, name="qc_b")
qc_b.y(0)
qc_b.y(1)

combined = qc_a.compose(qc_b, qubits=[1,3])
combined.draw("mpl")