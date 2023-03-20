from random import randint
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def main():

    path = '01.07.2022_1661699294.xlsx'
    tube_data = pd.read_excel(path)
    columns_to_drop = [
        'Посторонние источники тока (трамвайные пути и т.п.)', 'СКЗ',
       'Адрес 7-ег', 'К-т старения, год-1', '№ газопровода', 'Дата', 'Грунт',
       
    ]
    tube_data = tube_data.drop(columns=columns_to_drop).dropna().reset_index(drop=True)

    
    y_cols = [
        'Ост срок службы изоляции'
    ]
    x_tube = tube_data.drop(columns=y_cols)
    y_tube = tube_data[y_cols]
    
    x_train, x_test, y_train, y_test = train_test_split(x_tube, y_tube, 
                                                    train_size=0.8, 
                                                    random_state=777)
    
    tube_life_predictor = LinearRegression(n_jobs=-1)
    tube_life_predictor.fit(X=x_train, y=y_train)
    
    predicted_y = tube_life_predictor.predict(x_test)
    
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, predicted_y))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(y_test, predicted_y))
    
    plt.scatter(y_test, predicted_y)
    plt.show()
    
    print(x_tube.columns)




if __name__ == "__main__":
    main()
