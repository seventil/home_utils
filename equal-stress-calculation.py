import csv
import numpy as np


def get_data_from_csv(path):
    data = []
    with open(path, newline='') as f:
        csvfile = csv.reader(f, delimiter=',')
        for row in csvfile:
            data.append(row)
    return data


def calculate_equal_stress(main_stress):
    t = np.eye(3)
    t[0, 0] = main_stress[0]
    t[1, 1] = main_stress[1]
    t[2, 2] = main_stress[2]
    beta = -6.24e-12
    gamma = 1.97e-19

    r = ((-3*beta)/(4*gamma))/1e6
    d = t-(1/3)*(np.trace(t))*np.eye(3)
    b = np.array([[1], [0], [0]])
    tmA = np.sqrt(b.T@(((r*np.eye(3)) - (3/2)*d)**2)@b)

    if b.T@d@b <= (2*r)/3:
        teq = r-tmA
    else:
        teq = r + tmA

    return teq[0, 0]


def main():
    path = 'stress_data.csv'
    output = []
    stresses_to_transform = get_data_from_csv(path)
    for values in stresses_to_transform:
        result = (values, calculate_equal_stress(values))
        print(result)
        output.append(result)


if __name__ == '__main__':
    main()
