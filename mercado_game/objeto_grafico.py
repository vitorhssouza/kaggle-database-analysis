from mercado_game.objeto_dados import BaseDados
import matplotlib.pyplot as plt


import seaborn as sns

paletas_cores = sns.color_palette('Dark2', 8)


class Layout:

    def __init__(self, titulo: str = '', tamanho: tuple = (10, 5), y_label: str = ' ', x_label: str = ' ',
                 estilo: str = ' ', legenda=' ', tamanho_titulo: int = 0, posicao_titulo: str = 'left',
                 subtitulo: str = ''):
        self.__titulo = titulo
        self.__tamanho = tamanho
        self.__y_label = y_label
        self.__x_label = x_label
        self.__estilo = estilo
        self.__legenda = legenda
        self.__tamanho_titulo = tamanho_titulo
        self.__posicao_titulo = posicao_titulo
        self.__subtitulo = subtitulo

    def layout_bar(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo, loc='left', fontsize=14)
        plt.ylabel(self.__y_label)
        grafico = Grafico('PS4_GamesSales.csv')
        grafico.grafico_bar()
        plt.show()

    def layout_distribuicao(self):
        plt.figure(figsize=(self.__tamanho))
        plt.style.use(self.__estilo)
        plt.title(self.__titulo, loc=self.__posicao_titulo, fontsize=self.__tamanho_titulo)
        plt.ylabel(self.__y_label)
        grafico_distribuicao = Grafico('PS4_GamesSales.csv')
        grafico_distribuicao.grafico_distribuicao()
        plt.show()

    def layout_boxplot(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        grafico_boxplot = Grafico('PS4_GamesSales.csv')
        grafico_boxplot.grafico_boxplot()
        plt.show()

    def layout_distribuicao_continente(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        plt.xlabel(self.__x_label)
        plt.ylabel(self.__y_label)
        grafico_continente = Grafico('PS4_GamesSales.csv')
        grafico_continente.grafico_distribuicao_continente()
        plt.legend(['America N', 'Europa', ' Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.225, -0.089), ncol=4)
        plt.show()

    def layout_venda_america(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        plt.ylabel(self.__y_label, fontsize=14)
        plt.xlabel(self.__x_label, fontsize=14)
        grafico_america = Grafico('PS4_GamesSales.csv')
        grafico_america.grafico_vendas_america()
        plt.legend(fontsize=12)
        plt.show()

    def layout_venda_europa(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        plt.ylabel(self.__y_label, fontsize=14)
        plt.xlabel(self.__x_label, fontsize=14)
        grafico_europa = Grafico('PS4_GamesSales.csv')
        grafico_europa.grafico_vendas_europa()
        plt.legend(fontsize=12)
        plt.show()

    def layout_venda_japao(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        plt.ylabel(self.__y_label, fontsize=14)
        plt.xlabel(self.__x_label, fontsize=14)
        grafico_japao = Grafico('PS4_GamesSales.csv')
        grafico_japao.grafico_vendas_japao()
        plt.legend(fontsize=12)
        plt.show()

    def layout_venda_mundo(self):
        plt.figure(figsize=(self.__tamanho))
        plt.title(self.__titulo)
        plt.ylabel(self.__y_label, fontsize=14)
        plt.xlabel(self.__x_label, fontsize=14)
        grafico_mundo = Grafico('PS4_GamesSales.csv')
        grafico_mundo.grafico_vendas_mundo()
        plt.legend(fontsize=12)
        plt.show()


class Grafico(BaseDados):

    def __init__(self: object, basedados: str) -> None:
        super().__init__(basedados)
        self.__grafico_bar = ''
        self.__grafico_distribuicao = ''
        self.__grafico_boxplot = ''
        self.__grafico_distribuicao_continente = ''
        self.__grafico_continente_america = ''
        self.__grafico_continente_europa = ''
        self.__grafico_continente_japao = ''
        self.__grafico_continente_mundo = ''
        self.__grafico_vendas_america = ''
        self.__grafico_vendas_europa = ''
        self.__grafico_vendas_japao = ''
        self.__grafico_vendas_mundo = ''

    def grafico_bar(self: object) -> None:
        self.__grafico_bar = sns.barplot(data=self._BaseDados__base, x='Year', y='Global',
                                         ci=None, color='#69b3a2', estimator=sum)
        return self.__grafico_bar

    def grafico_distribuicao(self: object) -> None:
        self.__grafico_distribuicao = sns.kdeplot(self._BaseDados__base['Global'], shade=True, bw=1,
                                                  color='#96a8a8', linewidth=2.5)
        return self.__grafico_distribuicao

    def grafico_boxplot(self: object) -> None:
        self.__grafico_boxplot = sns.boxplot(data=self._BaseDados__base, x='Year', y='Global')

        return self.__grafico_boxplot

    def grafico_distribuicao_continente(self: object) -> None:
        largura_barra = 0.85

        grupos = [0, 1, 2, 3, 4, 5]

        # plot america
        self.__grafico_continente_america = plt.bar(grupos, self._BaseDados__america, width=largura_barra, color='#b5ffb0', edgecolor='white')

        # plot da europa
        self.__grafico_continente_europa = plt.bar(grupos, self._BaseDados__europa, bottom=self._BaseDados__america, width=largura_barra,
                         color='#f9bc86', edgecolor='white')

        # plot japão
        self.__grafico_continente_japao =plt.bar(grupos, self._BaseDados__japao, bottom=[a + b for a, b in zip(self._BaseDados__america, self._BaseDados__europa)],
                        width=largura_barra, color='#a3acff', edgecolor='white')

        # plot resto do mundo
        self.__grafico_continente_mundo = plt.bar(grupos, self._BaseDados__mundo, bottom=[a + b + c for a, b, c in zip(self._BaseDados__america, self._BaseDados__europa,
                                                                                      self._BaseDados__japao)],
                        width=largura_barra, color='#d3acfe', edgecolor='white')

        plt.xticks(grupos, self._BaseDados__analise['Year'])

        total = [self.__grafico_continente_america, self.__grafico_continente_europa, self.__grafico_continente_japao,
                 self.__grafico_continente_mundo]
        return total

    def grafico_vendas_america(self: object) -> None:
        grupos = list(range(1, 11))
        top_vendas = self._BaseDados__vendas_america['North America'][:10].values
        top_fabricante = self._BaseDados__vendas_america['Publisher'][:10].values
        self.__grafico_vendas_america = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
        return self.__grafico_vendas_america

    def grafico_vendas_europa(self: object) -> None:
        grupos = list(range(1, 11))
        top_vendas = self._BaseDados__vendas_europa['Europe'][:10].values
        top_fabricante = self._BaseDados__vendas_europa['Publisher'][:10].values
        self.__grafico_vendas_europa = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
        return self.__grafico_vendas_europa

    def grafico_vendas_japao(self: object) -> None:
        grupos = list(range(1, 11))
        top_vendas = self._BaseDados__vendas_japao['Japan'][:10].values
        top_fabricante = self._BaseDados__vendas_japao['Publisher'][:10].values
        self.__grafico_vendas_japao = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
        return self.__grafico_vendas_japao

    def grafico_vendas_mundo(self: object) -> None:
        grupos = list(range(1, 11))
        top_vendas = self._BaseDados__vendas_mundo['Rest of World'][:10].values
        top_fabricante = self._BaseDados__vendas_mundo['Publisher'][:10].values
        self.__grafico_vendas_mundo = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
        return self.__grafico_vendas_mundo


















