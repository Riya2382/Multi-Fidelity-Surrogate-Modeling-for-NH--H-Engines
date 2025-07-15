
---

## 📂 Key Files

### 🧠 `mf_surrogates/co_kriging.py`
```python
import numpy as np
import pandas as pd
from emukit.multi_fidelity.models import GPyMultiFidelityModel
from emukit.model_wrappers import GPyModelWrapper
import GPy

# Load data
low_fidelity = pd.read_csv('../data/processed/low_fidelity.csv')
high_fidelity = pd.read_csv('../data/processed/high_fidelity.csv')

# Combine
X_low = low_fidelity[['NH3_ratio', 'H2_ratio']].values
Y_low = low_fidelity['NOx_emission'].values.reshape(-1, 1)
X_high = high_fidelity[['NH3_ratio', 'H2_ratio']].values
Y_high = high_fidelity['NOx_emission'].values.reshape(-1, 1)

# Create GP models
kernel = GPy.kern.RBF(input_dim=2)
gpy_low = GPy.models.GPRegression(X_low, Y_low, kernel)
gpy_high = GPy.models.GPRegression(X_high, Y_high, kernel)

# Wrap and train
mf_model = GPyMultiFidelityModel([gpy_low, gpy_high])
mf_model.optimize()

# Save model
mf_model.save_model('mf_surrogate_model.pkl')
print("Multi-fidelity surrogate model saved.")
