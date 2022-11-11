from antAlgoritm import ant
import pandas as pd
from cities import City


def main():
    df = pd.read_csv('data.csv', index_col='id')
    cities = []
    for i in range(df.shape[0]):
        cities.append(City(df["latitude_dd"][i] / 100, df["longitude_dd"][i] / 100, i))
    print("Начинаем подсчет...")
    min_distance, best_way = ant(cities, 1)
    print(f"Минимальая расстояние: {min_distance}")


if __name__ == '__main__':
    main()

