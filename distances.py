
import csv


# Parse data from a csv file to create a 2D array of distance information: the weighted adjacency matrix.
# This constructor is called from main.py.
class Distances:
    def __init__(self):
        self.distance_matrix = []
        with open('csvs/distancesCSV.csv') as distances:
            reader = csv.reader(distances)
            for row in reader:
                float_row = [float(value) if value.strip() != '' else '' for value in row]
                self.distance_matrix.append(float_row)


# Instantiates the weighted adjacency matrix above and forwards it to the calling entity, in this case dijkstra.py.
def GetMatrix():
    var = Distances()
    matrix = var.distance_matrix
    return matrix
