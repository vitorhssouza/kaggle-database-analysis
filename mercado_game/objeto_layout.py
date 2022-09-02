"""#import seaborn as sns
import matplotlib.pyplot as plt

from mercado_game.objeto_grafico import Grafico


class Layout(Grafico):

    def __init__(self, basedados: str, grafico: str, layout: str) -> None:
        super().__init__(basedados, grafico)
        self.__layout = layout

    def layout_barra(self):
        plt.figure(figsize=(10, 5))
        plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=14)
        #self.__layout = self._Grafico__grafico
        plt.ylabel('Quantidade Vendas')
        return plt.show()

"""