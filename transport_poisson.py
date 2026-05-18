from pyomo.environ import *

def solve_transport():
    model = ConcreteModel(name="Transport_Poisson")

    model.I = Set(initialize=['Nouadhibou'])
    model.J = Set(initialize=['Central', 'Sebkha', 'Toujounine'])

    offre   = {'Nouadhibou': 500}
    demande = {'Central': 200, 'Sebkha': 150, 'Toujounine': 150}
    couts   = {
        ('Nouadhibou', 'Central'):    10,
        ('Nouadhibou', 'Sebkha'):     12,
        ('Nouadhibou', 'Toujounine'): 15
    }

    model.x = Var(model.I, model.J, domain=NonNegativeReals)

    def obj_rule(model):
        return sum(couts[i,j] * model.x[i,j] for i in model.I for j in model.J)
    model.obj = Objective(rule=obj_rule, sense=minimize)

    def supply_rule(model, i):
        return sum(model.x[i,j] for j in model.J) == offre[i]
    model.supply = Constraint(model.I, rule=supply_rule)

    def demand_rule(model, j):
        return sum(model.x[i,j] for i in model.I) >= demande[j]
    model.demand = Constraint(model.J, rule=demand_rule)

    solver = SolverFactory('glpk')
    result = solver.solve(model)

    if result.solver.termination_condition == TerminationCondition.optimal:
        print("\n--- Plan de Transport ---")
        cout_total = 0
        for i in model.I:
            for j in model.J:
                val = model.x[i, j].value
                if val and val > 0:
                    cout = couts[i, j] * val
                    print(f"  {i} → {j} : {val:.0f} unités  (coût : {cout:.0f})")
                    cout_total += cout
        print(f"\nCoût total : {cout_total:.0f}")
    else:
        print(f"Échec du solveur : {result.solver.termination_condition}")

if __name__ == "__main__":
    solve_transport()
