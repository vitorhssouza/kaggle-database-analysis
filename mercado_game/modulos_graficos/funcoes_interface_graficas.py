from mercado_game.objeto_dados import BaseDados
from mercado_game.objeto import Layout

from time import sleep

dados = BaseDados('PS4_GamesSales.csv')


def linha(tamanho: int = 90) -> None:
    print(tamanho * '=')


def menu() -> None:
    """Interface gráfica do usuário """
    linha()
    print('ANÁLISE MERCADO DE GAME'.center(90))
    linha()
    print('1  - BASE DE DADOS\n'
          '2  - DESCRIÇÃO BASE DE DADOS\n'
          '3  - INFORMAÇÃO BASE DE DADOS\n'
          '4  - GRÁFICO COM VALOR DE VENDAS NO ANO\n'
          '5  - DISTRIBUIÇÃO DAS VENDAS GLOBAIS\n'
          '6  - GRÁFICO COM ANÁLISE DA DISTRIBUIÇÃO GLOBAL DE VENDAS\n'
          '7  - GRÁFICO COM A DISTRUIBUIÇÃO DE VENDAS POR CONTINENTES\n'
          '8  - TOP 10 FABRICANTE DA AMÉRICA DO NORTE\n'
          '9  - TOP 10 FABRICANTE DA EUROPA\n'
          '10 - TOP 10 FABRICANTE DO JAPÃO\n'
          '11 - TOP 10 FABRICANTE DO RESTO DO MUNDO\n'
          '12 - RELATÓRIO CONTÉNDO TODOS OS GRÁFICOS\n'
          '13 - SAIR DO SISTEMA')

    opcao: int = int(input('Informe sua opção: '))
    escolha_opcao(opcao)


def escolha_opcao(opcao: int) -> None:
    """Função que recebe a escolha do usuário e interage com o sistema"""
    if opcao == 1:
        print(dados.basedados)
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 2:
        print(dados.descricao)
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 3:
        print(dados.info)
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 4:
        print('Imprimindo o gráfico com a quantidade de vendas globais e a base de dados com os 5 primeiros registros')
        sleep(2)
        print(dados.base_head)
        layout = Layout(titulo='Quantidade de Vendas Globais (mi)', tamanho=(10, 5), y_label='Quantidade Vendas',
                        tamanho_titulo=14, posicao_titulo='left')
        layout.layout_bar()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 5:
        print('Imprimindo o gráfico de distribuição das vendas')
        sleep(2)

        layout = Layout(titulo='Distribuição Das Vendas Globais', tamanho=(12, 5), estilo='ggplot',
                        tamanho_titulo=16, posicao_titulo='left')
        layout.layout_distribuicao()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 6:
        print('Imprimindo o gráfico boxplot de análise de distribuição das vendas')
        sleep(2)
        layout = Layout(titulo='Análise Da Distribuição Das Vendas Global (mi)', tamanho=(12, 5),
                        tamanho_titulo=16, posicao_titulo='left')
        layout.layout_boxplot()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 7:
        print('Imprimindo o gráfico contendo a distribuição das vendas dos continentes durante cada ano')
        sleep(2)
        layout = Layout(titulo='Análise Da Distribuição Das Vendas Global (mi)', tamanho=(12, 5),
                        tamanho_titulo=16, x_label='Grupo', y_label='Distribuição %')
        layout.layout_distribuicao_continente()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 8:
        print('Imprimindo os top 10 fabricante da américa do norte')
        sleep(2)
        print(dados.venda_america[:10])
        layout = Layout(titulo='Top 10 - Fabricante na America do Norte', tamanho=(15, 6),
                        tamanho_titulo=16, y_label='Vendas', x_label='Top 10 Editora')
        layout.layout_venda_america()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 9:
        print('Imprimindo os top 10 fabricante da Europa')
        sleep(2)
        print(dados.venda_europa[:10])
        layout = Layout(titulo='Top 10 - Fabricante na Europa', tamanho=(15, 6),
                        tamanho_titulo=16, y_label='Vendas', x_label='Top 10 Editora')
        layout.layout_venda_europa()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 10:
        print('Imprimindo os top 10 fabricante da Europa')
        sleep(2)
        print(dados.venda_japao[:10])
        layout = Layout(titulo='Top 10 - Fabricante no Japão', tamanho=(15, 6),
                        tamanho_titulo=16, y_label='Vendas', x_label='Top 10 Editora')
        layout.layout_venda_japao()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 11:
        print('Imprimindo os top 10 fabricante do restante do mundo')
        sleep(2)
        print(dados.venda_mundo[:10])
        layout = Layout(titulo='Top 10 - Fabricante no Restante do Mundo', tamanho=(15, 6),
                        tamanho_titulo=16, y_label='Vendas', x_label='Top 10 Editora')
        layout.layout_venda_mundo()
        print('Voltando ao menu')
        sleep(2)
        menu()
    elif opcao == 12:
        print('Imprimindo os relátorio contendo os gráficos')
        sleep(2)
        layout_relatorio = Layout(tamanho=(18, 15), cor_fundo='#f5f5f5', estilo='seaborn',
                                  titulo='Python para Análise de Dados \n Projeto prático 5 - Análise Mercado de Games'
                                         ' PS4')
        layout_relatorio.layout_relatorio()
        menu()
    elif opcao == 13:
        print('Saindo do sistema')
        sleep(1)
        exit()
    else:
        print('Opção inválida!! Tente novamente')
        menu()

