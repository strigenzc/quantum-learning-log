"""
hello_quantum.py
----------------
A simple script to demonstrate quantum entanglement (Bell State) using Qiskit.
This serves as the 'Hello, World' of quantum computing.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Create a Quantum Circuit with 2 Qubits and 2 Classical Bits
qc = QuantumCircuit(2, 2)

# 2. Put Qubit 0 into Superposition (The "spinning coin" state)
# H = Hadamard gate
qc.h(0)

# 3. Entangle Qubit 0 with Qubit 1
# CX = Controlled-NOT gate (equivalent to a quantum CNOT)
qc.cx(0, 1)

# 4. Measure both qubits into their corresponding classical bits
qc.measure([0, 1], [0, 1])

# 5. Initialize the local simulator
simulator = AerSimulator()

# 6. Run the experiment 1,000 times (shots) to gather statistical data
job = simulator.run(qc, shots=1000)
result = job.result()

# 7. Print the measured states
counts = result.get_counts()
print("\n--- Quantum Experiment Results ---")
print("Measurement counts (State: Occurrences):", counts)
print("------------------------------------\n")