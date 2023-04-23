import csv
import math


def ch_ost_max(nvm, h):
    f1 = pow(math.e, (nvm / -9006.167679834849))
    f2 = nvm / math.log(nvm)
    f3 = math.sqrt(nvm)
    f4 = 1.0 / math.sqrt(h)
    f5 = 1.0 / h
    f6 = 1.0 / (h*math.sqrt(h))
    f7 = math.log(h) / (h*h)
    z = 1229.571485010218 - 425.6036523678946*f1 \
        + 0.2484000717055630*f2 - 9.351219662620949*f3 \
        - 20413.22079131021*f4 + 494054.5109638379*f5 \
        - 6270543.761250133*f6 + 6611563.457691532*f7
    return z


def ch_ost_min(sigma_pril, h):
    f1 = sigma_pril**2
    f2 = sigma_pril**3
    f3 = pow(math.e, (sigma_pril / 111.0542057672787))
    z = - 13.28930495227476 + 0.001114714856481364*f1 \
        - 8.397940946547142E-06*f2 + 14.23762656838414*f3
    return z


def ch_pril(nvm, h):
    x = math.log(nvm)
    z = 1001.514778023720 + \
        x*(-103.6464965501158 + x*(-0.1849006563812434)) + \
        h*(5.087545624466923 + h*(-0.0001750450380706807)) + \
        x*h*(-0.4704503715376256)
    return z


def main():
    with open('testing_data.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            nvm = float(row.get('nvm'))
            h = float(row.get('h'))

            sigmapril = ch_pril(nvm, h)
            sigma_ost_min = ch_ost_min(sigmapril, h)
            sigma_ost_max = ch_ost_max(nvm, h)

            print(f'Sigma pril {int(sigmapril)}, sigma ost '
                  f'{int(sigma_ost_min)} - {int(sigma_ost_max)}')
            if sigma_ost_min > sigma_ost_max:
                print('------- fail --------')


if __name__ == '__main__':
    main()
