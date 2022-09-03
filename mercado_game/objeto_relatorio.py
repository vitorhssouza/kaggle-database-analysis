from mercado_game.objeto_grafico import Grafico
import matplotlib.pyplot as plt

grafico = Grafico('PS4_GamesSales.csv')


class GraficoRelatorio(Grafico):

    def __init__(self: object, basedados: str) -> None:
        super().__init__(basedados)

    def relatorio(self):
        fig, ax = plt.subplots(figsize=(25, 18))
        colunas = 2
        linhas = 4

        # cor de fundo
        cor_fundo = '#f5f5f5'
        ax.set_facecolor(cor_fundo)
        fig.set_facecolor(cor_fundo)

        # Estilo dos graficos
        plt.style.use('seaborn')

        # incluindo subtitulo
        plt.suptitle('Python para Análise de Dados \n Projeto prático 5 - Análise Mercado de Games PS4', fontsize=22,
                     color='#404040', fontweight=600)

        for c in range(1, 8):
            plt.subplot(linhas, colunas, c)

            if c == 1:
                plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=11)
                grafico.grafico_bar()
                plt.ylabel('Quantidade Vendas', fontsize=8)

            elif c == 2:
                plt.title('Análise da Distribuição Global (mi)', loc='left', fontsize=11)
                grafico.grafico_boxplot()

            elif c == 3:
                plt.title('Análise da Distribuição Por Continentes', loc='left', fontsize=11)
                grafico.grafico_distribuicao_continente()
                plt.ylabel('Distribuição %', fontsize=8)

            elif c == 4:
                plt.title('Top 10 - Fabricante na America do Norte', loc='left', fontsize=11)
                plt.xlabel('Top 10 Editora', fontsize=8)
                plt.ylabel('Vendas', fontsize=8)
                grafico.grafico_vendas_america()

            elif c == 5:
                plt.title('Top 10 - Fabricante na Europa', loc='left', fontsize=11)
                plt.xlabel('Top 10 Editora', fontsize=8)
                plt.ylabel('Vendas', fontsize=8)
                grafico.grafico_vendas_europa()

            elif c == 6:
                plt.title('Top 10 - Fabricante no Japão', loc='left', fontsize=11)
                plt.xlabel('Top 10 Editora', fontsize=8)
                plt.ylabel('Vendas', fontsize=8)
                grafico.grafico_vendas_japao()

            else:
                plt.title('Top 10 - Fabricante no restante do mundo', loc='left', fontsize=11)
                plt.xlabel('Top 10 Editora', fontsize=8)
                plt.ylabel('Vendas', fontsize=8)
                grafico.grafico_vendas_mundo()
                plt.xticks(rotation=65)
                plt.legend(self._BaseDados__vendas_mundo['Publisher'][:10].values, fontsize=7)

        plt.subplots_adjust(hspace=0.50, wspace=0.15)
        plt.show()

