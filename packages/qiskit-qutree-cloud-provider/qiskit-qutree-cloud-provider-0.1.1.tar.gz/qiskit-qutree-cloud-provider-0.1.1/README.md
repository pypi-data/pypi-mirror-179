# Qiskit QuTree Cloud Provider

## Usage

```python
from qiskit import QuantumCircuit
from qiskit_qutree_cloud_provider import QuTreeCloudProvider

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

backend = QuTreeCloudProvider().get_backend()
r = backend.run(qc, vbond_dim=64, shots=100).result()
print(r.get_counts())
```

## Develop

In a Python virtual environment,
```bash
pip install '.[dev]'
pre-commit install
```

To regenerate the gRPC classes,
```bash
make gen
```
