import pandas as pd

df = pd.read_csv("F1DriversDataset.csv", sep=",")

class Formula:

    #anos em atividade dos pilotos da Fórmula 1
    def anos_atividade():
        print(df.sort_values('Years_Active', ascending=False))

    #pilotos que já foram campeões
    def campeoes():
        print(df[df['Champion'] == True])

piloto = Formula
piloto.anos_atividade()
piloto.campeoes()

