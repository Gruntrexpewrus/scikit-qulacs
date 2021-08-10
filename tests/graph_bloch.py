import numpy as np
from qulacs import Observable, QuantumState
from qulacs.gate import to_matrix_gate, X, CNOT, H, RX, RY
from skqulacs.circuit import show_blochsphere


def test_bloch():
    n = 3
    state = QuantumState(n)
    state.set_computational_basis(0b000)
    H(0).update_quantum_state(state)
    show_blochsphere(state, 0)
    RY(0, 0.1).update_quantum_state(state)
    show_blochsphere(state, 0)
    CNOT(0, 1).update_quantum_state(state)
    show_blochsphere(state, 0)
    show_blochsphere(state, 1)
    show_blochsphere(state, 2)
