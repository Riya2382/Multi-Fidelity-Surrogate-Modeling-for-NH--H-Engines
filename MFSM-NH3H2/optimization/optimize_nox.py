from pymoo.optimize import minimize
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_problem
from pymoo.core.problem import Problem
import pickle

# Load surrogate model
with open('../mf_surrogates/mf_surrogate_model.pkl', 'rb') as f:
    mf_model = pickle.load(f)

class EngineProblem(Problem):
    def __init__(self):
        super().__init__(n_var=2, n_obj=1, n_constr=0, xl=[0, 0], xu=[1, 1])

    def _evaluate(self, X, out, *args, **kwargs):
        preds = mf_model.predict(X)
        out["F"] = preds[:, 0]  # Minimize NOx

problem = EngineProblem()
algorithm = NSGA2(pop_size=40)

res = minimize(problem, algorithm, ('n_gen', 50), seed=1, verbose=True)
print("Optimal NH3-H2 ratios:", res.X)
