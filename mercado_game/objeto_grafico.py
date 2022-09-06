from mercado_game.objeto_dados import BaseDados
from time import sleep
import matplotlib.pyplot as plt
import seaborn as sns

paletas_cores = sns.color_palette('Dark2', 8)


class Layout:

    def __init__(self, titulo: str = '', tamanho: tuple = (10, 5), y_label: str = ' ', x_label: str = ' ',
                 estilo: str = ' ', legenda=' ', tamanho_titulo: int = 0, posicao_titulo: str = 'left',
                 subtitulo: str = '',  cor_fundo: str = ''):
        self.__titulo = titulo
        self.__tamanho = tamanho
        self.__y_label = y_label
        self.__x_label = x_label
        self.__estilo = estilo
        self.__legenda = legenda
        self.__tamanho_titulo = tamanho_titulo
        self.__posicao_titulo = posicao_titulo
        self.__subtitulo = subtitulo
        self.__cor_fundo = cor_fundo

    def layout_bar(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo, loc='left', fontsize=14)
            plt.ylabel(self.__y_label)
            grafico = Grafico('PS4_GamesSales.csv')
            grafico.grafico_bar()
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=11)
            plt.ylabel('Quantidade Vendas', fontsize=8)
            grafico = Grafico('PS4_GamesSales.csv')
            grafico.grafico_bar()

    def layout_distribuicao(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.style.use(self.__estilo)
            plt.title(self.__titulo, loc=self.__posicao_titulo, fontsize=self.__tamanho_titulo)
            plt.ylabel(self.__y_label)
            grafico_distribuicao = Grafico('PS4_GamesSales.csv')
            grafico_distribuicao.grafico_distribuicao()
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=11)
            plt.ylabel(self.__y_label)
            plt.xlabel(self.__x_label)
            grafico_distribuicao = Grafico('PS4_GamesSales.csv')
            grafico_distribuicao.grafico_distribuicao()

    def layout_boxplot(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            grafico_boxplot = Grafico('PS4_GamesSales.csv')
            grafico_boxplot.grafico_boxplot()
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=11)
            #plt.ylabel(self.__y_label)
            grafico = Grafico('PS4_GamesSales.csv')
            grafico.grafico_boxplot()

    def layout_distribuicao_continente(self, opcao: int = 2):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            plt.xlabel(self.__x_label)
            plt.ylabel(self.__y_label)
            grafico_continente = Grafico('PS4_GamesSales.csv')
            grafico_continente.grafico_distribuicao_continente()
            plt.legend(['America N', 'Europa', ' Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.225, -0.089), ncol=4)
            #plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=10)
            #plt.xlabel(self.__x_label, fontsize=7)
            plt.ylabel(self.__y_label, fontsize=7)
            grafico = Grafico('PS4_GamesSales.csv')
            grafico.grafico_distribuicao_continente()

    def layout_venda_america(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            plt.ylabel(self.__y_label, fontsize=14)
            plt.xlabel(self.__x_label, fontsize=14)
            grafico_america = Grafico('PS4_GamesSales.csv')
            grafico_america.grafico_vendas_america()
            plt.legend(fontsize=12)
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=10)
            plt.ylabel(self.__y_label, fontsize=7)
            grafico_america = Grafico('PS4_GamesSales.csv')
            grafico_america.grafico_vendas_america(2)
            plt.xticks(rotation=45, ha='right', fontsize=5)

    def layout_venda_europa(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            plt.ylabel(self.__y_label, fontsize=14)
            plt.xlabel(self.__x_label, fontsize=14)
            grafico_europa = Grafico('PS4_GamesSales.csv')
            grafico_europa.grafico_vendas_europa()
            plt.legend(fontsize=12)
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=10)
            plt.ylabel(self.__y_label, fontsize=7)
            grafico_europa = Grafico('PS4_GamesSales.csv')
            grafico_europa.grafico_vendas_europa(2)
            plt.xticks(rotation=45, ha='right', fontsize=5)

    def layout_venda_japao(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            plt.ylabel(self.__y_label, fontsize=14)
            plt.xlabel(self.__x_label, fontsize=14)
            grafico_japao = Grafico('PS4_GamesSales.csv')
            grafico_japao.grafico_vendas_japao()
            plt.legend(fontsize=12)
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=10)
            plt.ylabel(self.__y_label, fontsize=7)
            grafico_japao = Grafico('PS4_GamesSales.csv')
            grafico_japao.grafico_vendas_japao(2)
            plt.xticks(rotation=45, ha='right', fontsize=5)

    def layout_venda_mundo(self, opcao: int = 1):
        if opcao == 1:
            plt.figure(figsize=(self.__tamanho))
            plt.title(self.__titulo)
            plt.ylabel(self.__y_label, fontsize=14)
            plt.xlabel(self.__x_label, fontsize=14)
            grafico_mundo = Grafico('PS4_GamesSales.csv')
            grafico_mundo.grafico_vendas_mundo()
            plt.legend(fontsize=12)
            plt.show()
        else:
            plt.title(self.__titulo, loc='left', fontsize=10)
            plt.ylabel(self.__y_label, fontsize=7)
            grafico_japao = Grafico('PS4_GamesSales.csv')
            grafico_japao.grafico_vendas_japao(2)
            plt.xticks(rotation=45, ha='right', fontsize=5)

    def layout_relatorio(self, opcao: int = 1):
        fig, ax = plt.subplots(figsize=(self.__tamanho))
        ax.set_facecolor(self.__cor_fundo)
        fig.set_facecolor(self.__cor_fundo)
        plt.style.use(self.__estilo)
        plt.suptitle(self.__titulo, fontsize=18, color='#404040', fontweight=400)
        if opcao == 1:
            grafico_relatorio = GraficoRelatorio()
            grafico_relatorio.relatorio1()
            plt.subplots_adjust(hspace=0.35, wspace=0.15)
            rodape = '''
                                 Esse relatório foi elaborado no treinamento "Python para Análise de Dados"
                                 está dispónivel no canal do youtube @Data Viking
                                 by: Vitor Souza
                               '''
            fig.text(0.5, -0.01, rodape, ha='center', va='bottom', size=12, color='#938ca1')
            plt.show()
        else:
            grafico_relatorio2 = GraficoRelatorio()
            grafico_relatorio2.relatorio2()
            plt.subplots_adjust(hspace=0.35, wspace=0.15)
            rodape = '''
                                             Esse relatório foi elaborado no treinamento "Python para Análise de Dados"
                                             está dispónivel no canal do youtube @Data Viking
                                             by: Vitor Souza
                                           '''
            fig.text(0.5, -0.01, rodape, ha='center', va='bottom', size=12, color='#938ca1')



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
        self.__grafico_distribuicao = sns.kdeplot(self._BaseDados__base['Global'], shade=True, bw_adjust=3,
                                                  color='#96a8a8', linewidth=2.5)
        return self.__grafico_distribuicao

    def grafico_boxplot(self: object) -> None:
        self.__grafico_boxplot = sns.boxplot(data=self._BaseDados__base, x='Year', y='Global')

        return self.__grafico_boxplot

    def grafico_distribuicao_continente(self: object, opcao: int = 1) -> None:
        largura_barra = 0.85

        grupos = [0, 1, 2, 3, 4, 5]

        # plot america
        self.__grafico_continente_america = plt.bar(grupos, self._BaseDados__america, width=largura_barra, color='#b5ffb0', edgecolor='white')

        # plot da europa
        self.__grafico_continente_europa = plt.bar(grupos, self._BaseDados__europa, bottom=self._BaseDados__america, width=largura_barra,
                         color='#f9bc86', edgecolor='white')

        # plot japão
        self.__grafico_continente_japao = plt.bar(grupos, self._BaseDados__japao, bottom=[a + b for a, b in zip(self._BaseDados__america, self._BaseDados__europa)],
                        width=largura_barra, color='#a3acff', edgecolor='white')

        # plot resto do mundo
        self.__grafico_continente_mundo = plt.bar(grupos, self._BaseDados__mundo, bottom=[a + b + c for a, b, c in zip(self._BaseDados__america, self._BaseDados__europa,
                                                                                      self._BaseDados__japao)],
                        width=largura_barra, color='#d3acfe', edgecolor='white')

        plt.xticks(grupos, self._BaseDados__analise['Year'])

        return plt.show()

    def grafico_vendas_america(self: object, opcao: int = 1) -> None:
        if opcao == 1:
            grupos = list(range(1, 11))
            top_vendas = self._BaseDados__vendas_america['North America'][:10].values
            top_fabricante = self._BaseDados__vendas_america['Publisher'][:10].values
            self.__grafico_vendas_america = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
            return self.__grafico_vendas_america
        else:
            top_vendas = self._BaseDados__vendas_america['North America'][:10].values
            top_fabricante = self._BaseDados__vendas_america['Publisher'][:10].values
            self.__grafico_vendas_america = plt.bar(top_fabricante, top_vendas, color='#f44e3f', width=0.3)
            return self.__grafico_vendas_america

    def grafico_vendas_europa(self: object, opcao: int = 1) -> None:
        if opcao == 1:
            grupos = list(range(1, 11))
            top_vendas = self._BaseDados__vendas_europa['Europe'][:10].values
            top_fabricante = self._BaseDados__vendas_europa['Publisher'][:10].values
            self.__grafico_vendas_europa = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
            return self.__grafico_vendas_europa
        else:
            top_vendas = self._BaseDados__vendas_europa['Europe'][:10].values
            top_fabricante = self._BaseDados__vendas_europa['Publisher'][:10].values
            self.__grafico_vendas_europa = plt.bar(top_fabricante, top_vendas, color='#f44e3f', width=0.3)
            return self.__grafico_vendas_europa

    def grafico_vendas_japao(self: object, opcao: int = 1) -> None:
        if opcao == 1:
            grupos = list(range(1, 11))
            top_vendas = self._BaseDados__vendas_japao['Japan'][:10].values
            top_fabricante = self._BaseDados__vendas_japao['Publisher'][:10].values
            self.__grafico_vendas_japao = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
            return self.__grafico_vendas_japao
        else:
            top_vendas = self._BaseDados__vendas_japao['Japan'][:10].values
            top_fabricante = self._BaseDados__vendas_japao['Publisher'][:10].values
            self.__grafico_vendas_japao = plt.bar(top_fabricante, top_vendas, color='#f44e3f', width=0.3)
            return self.__grafico_vendas_japao

    def grafico_vendas_mundo(self: object, opcao: int = 1) -> None:
        if opcao == 1:
            grupos = list(range(1, 11))
            top_vendas = self._BaseDados__vendas_mundo['Rest of World'][:10].values
            top_fabricante = self._BaseDados__vendas_mundo['Publisher'][:10].values
            self.__grafico_vendas_mundo = plt.bar(grupos, top_vendas, color='#f44e3f', width=0.3, label=top_fabricante)
            return self.__grafico_vendas_mundo
        else:
            top_vendas = self._BaseDados__vendas_mundo['Rest of World'][:10].values
            top_fabricante = self._BaseDados__vendas_mundo['Publisher'][:10].values
            self.__grafico_vendas_mundo = plt.bar(top_fabricante, top_vendas, color='#f44e3f', width=0.3)
            return self.__grafico_vendas_mundo


class GraficoRelatorio:

    def relatorio1(self):
        linhas = 6
        colunas = 2
        for c in range(1, 7):
            if c != 3 and c != 4:
                plt.subplot(linhas, colunas, c)
                if c == 1:
                    layout_bar = Layout(titulo='Quantidade de Vendas Globais (mi)', y_label='Quantidade Vendas')
                    layout_bar.layout_bar(2)
                elif c == 2:
                    layout_box = Layout(titulo='Análise Da Distribuição Das Vendas Global (mi)', y_label='Quantidade Vendas')
                    layout_box.layout_boxplot(2)

                elif c == 5:
                    layout_distribuicao = Layout(titulo='Distribuição das Vendas Globais',
                                                 y_label='Density', x_label='Global')
                    layout_distribuicao.layout_distribuicao(2)
                elif c == 6:
                    layout_continente = Layout(titulo='Análise da Distribuição Por Continentes',
                                               y_label='Distribuição')
                    layout_continente.layout_distribuicao_continente(2)

        layout = Layout(tamanho=(18, 15), cor_fundo='#f5f5f5', estilo='seaborn',
                        titulo='Python para Análise de Dados \n Projeto prático 5 - Análise Mercado de Games PS4')
        layout.layout_relatorio(2)

    def relatorio2(self):
        linhas = 6
        colunas = 2
        for c in range(1, 7):
            if c != 3 and c != 4:
                plt.subplot(linhas, colunas, c)
                if c == 1:
                    layout_america = Layout(titulo='Top 10 - Editora na America do Norte', y_label='Vendas')
                    layout_america.layout_venda_america(2)
                elif c == 2:
                    layout_europa = Layout(titulo='Top 10 - Editora na Europa',
                                           y_label='Vendas')
                    layout_europa.layout_venda_europa(2)

                elif c == 5:
                    layout_japao = Layout(titulo='Top 10 - Editora Japão',
                                                 y_label='Density', x_label='Global')
                    layout_japao.layout_venda_japao(2)
                elif c == 6:
                    layout_mundo = Layout(titulo='Top 10 - Editora no Restante do Mundo',
                                          y_label='Distribuição')
                    layout_mundo.layout_venda_mundo(2)




















