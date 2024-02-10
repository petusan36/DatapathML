import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer


def booltonum(dataset) -> int:
    x = int(dataset)
    return x


def getcolumnsbytype(dataset, type_column: int = 1) -> list:
    types = ['float64', 'int64']
    columns_list = []
    for col in dataset.columns:
        if type_column == 1:
            if dataset[col].dtypes in types:
                columns_list.append(col)
        else:
            if dataset[col].dtypes not in types:
                columns_list.append(col)
    return columns_list


def fillwithmean(dataset):
    newset = pd.DataFrame()
    for col in dataset.columns:
        newset[col] = dataset[col].fillna(dataset[col].mean())
    return newset


def fillwithmode(dataset):
    newset = pd.DataFrame()
    for col in dataset.columns:
        newset[col] = dataset[col].fillna(dataset[col].mode()[0])
    return newset


def aplicadummies(dataset, column_names):
    dataset = pd.get_dummies(dataset, columns=column_names, dtype='int64')
    for column_name in column_names:
        cnames = dataset.columns[dataset.columns.str.startswith(column_name) == True]
        dataset = dataset.drop(cnames[len(cnames) - 1], axis=1)
    return dataset


def organizadata(dataset):
    dataset.drop(['Name', 'PassengerId', 'Cabin'], axis=1, inplace=True)

    columns_numeric = getcolumnsbytype(dataset)
    columns_str = getcolumnsbytype(dataset, 0)
    dataset[columns_numeric] = fillwithmean(dataset[columns_numeric])
    dataset[columns_str] = fillwithmode(dataset[columns_str])

    column_names = ['HomePlanet', 'Destination']
    dataset = aplicadummies(dataset, column_names)
    dataset['VIP'] = dataset['VIP'].apply(booltonum)
    dataset['CryoSleep'] = dataset['CryoSleep'].apply(booltonum)

    scaling = StandardScaler()
    dataset['Age'] = scaling.fit_transform(dataset['Age'].values.reshape(-1, 1))

    pt = PowerTransformer(method='yeo-johnson', standardize=True)
    c = ['RoomService', 'Spa', 'FoodCourt', 'ShoppingMall', 'VRDeck', 'Age', 'VIP', 'HomePlanet_Earth',
         'HomePlanet_Europa',
         'Destination_PSO J318.5-22', 'Destination_55 Cancri e']
    for i in c:
        dataset[i] = pt.fit_transform(dataset[i].values.reshape(-1, 1))
    return dataset
