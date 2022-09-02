import pandas as pd
from sklearn.preprocessing import LabelEncoder

funcao_label = LabelEncoder()


class BaseDados:

    def __init__(self, basedados):
        self.__basedados = pd.read_csv(basedados, encoding='latin-1')
        self.__basedados.dropna(inplace=True)
        self.__base = self.__basedados.loc[(self.__basedados['Year'] != 2019) &
                                           (self.__basedados['Year'] != 2020)]

        self.__analise = self.__base.groupby(by=['Year']).sum().reset_index()

        self.__america = [(self.__america / total) * 100 for self.__america, total in zip(
                            self.__analise['North America'], self.__analise['Global'])]

        self.__europa = [(self.__europa / total) * 100 for self.__europa, total in zip(
                            self.__analise['Europe'], self.__analise['Global'])]

        self.__japao = [(self.__japao / total) * 100 for self.__japao, total in zip(
                            self.__analise['Japan'], self.__analise['Global'])]

        self.__mundo = [(self.__mundo / total) * 100 for self.__mundo, total in zip(
                            self.__analise['Rest of World'], self.__analise['Global'])]

        self.__empresas = self.__base['Publisher'].unique()

        self.__vendas_america = self.__base.groupby(by=['Publisher']).sum().reset_index()[
                                ['Publisher', 'North America']].sort_values('North America', ascending=False)

        self.__vendas_europa = self.__base.groupby(by=['Publisher']).sum().reset_index()[
                                ['Publisher', 'Europe']].sort_values('Europe', ascending=False)

        self.__vendas_japao = self.__base.groupby(by=['Publisher']).sum().reset_index()[
                                ['Publisher', 'Japan']].sort_values('Japan', ascending=False)

        self.__vendas_mundo = self.__base.groupby(by=['Publisher']).sum().reset_index()[
                                ['Publisher', 'Rest of World']].sort_values('Rest of World', ascending=False)


    @property
    def basedados(self: object) -> None:
        """Base de dados completa """
        return self.__basedados

    @property
    def base(self: object) -> None:
        """Base de dados sem os anos que estão vazio"""
        return self.__base

    @property
    def base_head(self: object) -> None:
        """Retorna os cinco primeiro registro da tabela base"""
        return self.__base.head()

    @property
    def descricao(self: object) -> None:
        return self.__basedados.describe()

    @property
    def info(self: object) -> None:
        return self.__basedados.info()

    @property
    def hea(self):
        return self.__basedados.head()

    @property
    def america(self: object) -> list:
        return self.__america

    @property
    def europeu(self: object) -> list:
        return self.__europa

    @property
    def japao(self: object) -> list:
        return self.__japao

    @property
    def mundo(self: object) -> list:
        return self.__mundo

    @property
    def venda_america(self: object) -> list:
        """Retorna o total de vendas por fabricante no norte america"""
        return self.__vendas_america

    @property
    def venda_europa(self: object) -> None:
        """Retorna o total de vendas por fabricante na europa"""
        return self.__vendas_europa

    @property
    def venda_japao(self: object) -> None:
        """Retorna o total de vendas por fabricante no japan"""
        return self.__vendas_japao

    @property
    def venda_mundo(self: object) -> None:
        """Retorna o total de vendas por fabricante no restante do mundo"""
        return self.__vendas_mundo





