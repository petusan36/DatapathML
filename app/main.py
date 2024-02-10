import argparse
import sys

import pandas as pd
import pickle
import datawrangling as dw


def main():
    parser = argparse.ArgumentParser(description="Captura del nombre del archivo")
    parser.add_argument("archivo")
    args = parser.parse_args()
    if len(args.archivo) > 0:
        df_test = pd.read_csv('data/' + args.archivo, sep=',')
        labelpasstest = df_test['PassengerId']
        df_test = dw.organizadata(df_test)

        with open('model/model.pkl', 'rb') as f:
            classifier = pickle.load(f)

        y_pred_test = classifier.predict(df_test)
        y_pred_test = pd.Series(y_pred_test)
        y_pred_test = y_pred_test.map({1: 'True', 0: False})
        y_pred_test = y_pred_test.to_list()
        resultado = pd.DataFrame({'PassengerId': labelpasstest, 'Transported': y_pred_test})

        print(resultado)
    else:
        print("Archivo invalido")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())
#    print("Hola Mundo")
