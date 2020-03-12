from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import pandas as pd
import csv
import numpy as np




def create_data_model():
    data = {}
    with open('lin318.distances', newline='') as f:
        reader = csv.reader(f)
        data['distance_matrix'] = list(reader)

    data['distance_matrix'].pop(0)
    data['depot'] = 0
    return data


def print_solution(manager, routing, assignment):
    print('Objective: {} miles'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {}, '.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           1, data['depot'])

    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(data['distance_matrix'][from_node][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    assignment = routing.SolveWithParameters(search_parameters)

    if assignment:
        print_solution(manager, routing, assignment)


if __name__ == '__main__':
    main()