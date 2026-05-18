from pyomo.environ import *

def solve_routing():
    model = ConcreteModel(name="Routage_Eau")

    points = [0, 1, 2, 3]
    dist = {
        (0,1): 5, (0,2): 8, (0,3): 10,
        (1,0): 5, (1,2): 4, (1,3): 7,
        (2,0): 8, (2,1): 4, (2,3): 3,
        (3,0): 10, (3,1): 7, (3,2): 3
    }

    model.x = Var(dist.keys(), domain=Binary)
    model.u = Var(points, bounds=(0, len(points)-1), domain=NonNegativeReals)

    def obj_rule(model):
        return sum(dist[i,j] * model.x[i,j] for (i,j) in dist.keys())
    model.obj = Objective(rule=obj_rule, sense=minimize)

    model.cons1 = ConstraintList()
    for i in points:
        model.cons1.add(sum(model.x[i,j] for j in points if (i,j) in dist) == 1)
        model.cons1.add(sum(model.x[j,i] for j in points if (j,i) in dist) == 1)

    model.mtz = ConstraintList()
    n = len(points)
    for i in points:
        for j in points:
            if i != 0 and j != 0 and i != j and (i,j) in dist:
                model.mtz.add(model.u[i] - model.u[j] + n * model.x[i,j] <= n - 1)

    model.u[0].fix(0)

    solver = SolverFactory('glpk')
    result = solver.solve(model)

    if result.solver.termination_condition == TerminationCondition.optimal:
        print("\n--- Itinéraire Optimal ---")
        distance_totale = 0
        for (i, j) in dist.keys():
            if model.x[i, j].value and round(model.x[i, j].value) == 1:
                print(f"  Point {i} → Point {j}  (distance : {dist[i,j]})")
                distance_totale += dist[i, j]
        print(f"Distance totale : {distance_totale}")
    else:
        print(f"Échec du solveur : {result.solver.termination_condition}")

if __name__ == "__main__":
    solve_routing()
