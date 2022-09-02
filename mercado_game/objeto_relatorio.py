from mercado_game.objeto_grafico import Grafico
import matplotlib.pyplot as plt

grafico = Grafico('PS4_GamesSales.csv')


class GraficoRelatorio(Grafico):

    def __init__(self: object, basedados: str) -> None:
        super().__init__(basedados)

    def relatorio(self):
        fig, ax = plt.subplots(figsize=(18, 15))
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
                grafico.grafico_bar()

            elif c == 2:
                grafico.grafico_boxplot()

            elif c == 3:
                grafico.grafico_distribuicao_continente()

            elif c == 4:
                grafico.grafico_vendas_america()

            elif c == 5:
                grafico.grafico_vendas_europa()

            elif c == 6:
                grafico.grafico_vendas_japao()

            else:
                grafico.grafico_vendas_mundo()

        plt.subplots_adjust(hspace=0.50, wspace=0.15)
        plt.show()

