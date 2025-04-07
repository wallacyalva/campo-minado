import tkinter as tk
from tkinter import messagebox
import random
#adicionado apara gerar o exe
import sys
import os

# caminho para o exe pegar as imagens
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

#funcao que limpa a tela para adicionar novos elementos
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

#funcao que mostra o menu inicial contendo as opcoes
def mostrar_menu():
    limpar_tela()
    btn_novo_jogo = tk.Button(janela, text="Novo Jogo", command=novo_jogo, height=2, width=20)
    btn_como_jogar = tk.Button(janela, text="Como Jogar", command=como_jogar, height=2, width=20)
    btn_creditos = tk.Button(janela, text="Créditos", command=creditos, height=2, width=20)

    btn_novo_jogo.pack(pady=10)
    btn_como_jogar.pack(pady=10)
    btn_creditos.pack(pady=10)

#funcao que intrui a pessoa de como jogar e deixa retornar o menu
def como_jogar():
    limpar_tela()
    texto = (
        "Como Jogar\n\n"
        "Ao iniciar será solicitado as dimensões do campo minado e a quantidade de bombas\n"
        "O tamanho do campo minado não pode ser maior que 30x30\n"
        "A quantidade de bombas deve ser maior que 2 e caber dentro das dimenções informadas\n"
        "Fique atento a não preencher errado pois depois de prosseguir não será possível retornar\n"
        "Inicie clicando em uma área: pode revelar um número, espaço vazio ou uma mina\n"
        "Números indicam quantas minas estão próximas\n"
        "Clique com o botão direito para marcar minas com bandeiras\n"
        "Você vence ao revelar todos os quadrados sem minas\n"
        "Você perde se clicar em uma mina\n"
        "Boa sorte!"
    )
    tk.Label(janela, text=texto, justify="center", font=("Arial", 12)).pack(pady=10)
    tk.Button(janela, text="Voltar", command=mostrar_menu, height=2, width=20).pack(pady=10)

#funcao que tras as informacoes de quem fez o jogo e do professor
def creditos():
    limpar_tela()
    texto = (
        "Trabalho M1 Introdução a Python\n"
        "Campo Minado\n\n"
        "Professor: Eduardo Poffo Medeiros Dias\n\n"
        "Desenvolvido por: Wallacy Alvarenga\n"
        "Código de pessoa: 6916694\n"
        "E-mail: wallacyalvarenga@univali.br"
    )
    tk.Label(janela, text=texto, justify="center", font=("Arial", 12)).pack(pady=10)
    tk.Button(janela, text="Voltar", command=mostrar_menu, height=2, width=20).pack(pady=10)


#funcao que solicita ao usuario as informacoes para criar o campo minado
def novo_jogo():
    limpar_tela()
    tk.Label(janela, text="Tamanho do campo (Ex: 10x10):", font=("Arial", 12)).pack(pady=5)
    entry_tamanho = tk.Entry(janela, font=("Arial", 12))
    entry_tamanho.pack(pady=5)
    tk.Label(janela, text="Quantidade de Bombas:", font=("Arial", 12)).pack(pady=5)
    entry_bombas = tk.Entry(janela, font=("Arial", 12))
    entry_bombas.pack(pady=5)
    tk.Button(janela, text="Prosseguir", command=lambda: validar_e_prosseguir(entry_tamanho, entry_bombas), height=2, width=20).pack(pady=10)
    tk.Button(janela, text="Voltar", command=mostrar_menu, height=2, width=20).pack(pady=5)


#função que valida todas as informacoes para nao ter nenhum bug e cria o campo minado
def validar_e_prosseguir(entry_tamanho, entry_bombas):
    global qtd_bombas_salvas, linhas, colunas, botoes, matriz, bombas
    tamanho = entry_tamanho.get()
    bombas = entry_bombas.get()
    qtd_bombas_salvas = bombas

    if not tamanho:
        messagebox.showerror("Erro", "Informe o tamanho do campo.")
        return

    if 'x' not in tamanho:
        messagebox.showerror("Erro", "O formato deve ser LxC, ex: 10x10.")
        return

    partes = tamanho.lower().split('x')
    if len(partes) != 2:
        messagebox.showerror("Erro", "Formato inválido. Use LxC.")
        return

    try:
        linhas = int(partes[0])
        colunas = int(partes[1])
    except ValueError:
        messagebox.showerror("Erro", "As dimensões devem ser números inteiros.")
        return

    if not (2 <= linhas <= 30 and 2 <= colunas <= 30):
        messagebox.showerror("Erro", "As dimensões devem estar entre 2 e 30.")
        return

    if not bombas:
        messagebox.showerror("Erro", "Informe a quantidade de bombas.")
        return

    try:
        bombas = int(bombas)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade de bombas deve ser um número inteiro.")
        return

    total_celulas = linhas * colunas
    if bombas < 1 or bombas >= total_celulas:
        messagebox.showerror("Erro", "Quantidade de bombas deve ser entre 1 e (linhas x colunas - 1).")
        return

    botoes = []
    matriz = criar_matriz(linhas, colunas)
    adicionar_bombas(matriz, bombas)
    iniciar_jogo(linhas, colunas)

#cria uma matriz base onde ficara as bombas
def criar_matriz(linhas, colunas):
    return [[0 for _ in range(colunas)] for _ in range(linhas)]

#cria as bombas e colocar elas na matriz
def adicionar_bombas(matriz, qtd_bombas):
    linhas = len(matriz)
    colunas = len(matriz[0])
    bombas_adicionadas = 0

    while bombas_adicionadas < qtd_bombas:
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        if matriz[i][j] != '💣':
            matriz[i][j] = '💣'
            atualizar_vizinhos(matriz, i, j)
            bombas_adicionadas += 1

#atualiza os valores em volta da bomba
def atualizar_vizinhos(matriz, linha, coluna):
    linhas, colunas = len(matriz), len(matriz[0])
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < linhas and 0 <= j < colunas:
                if matriz[i][j] != '💣':
                    matriz[i][j] += 1

#imprime os botoes do campo minado e adiciona as funcoes de clique
def iniciar_jogo(linhas, colunas):
    limpar_tela()
    global frame_jogo
    frame_jogo = tk.Frame(janela)
    frame_jogo.pack(pady=20)

    frame_campo = tk.Frame(frame_jogo)
    frame_campo.pack()

    for i in range(linhas):
        linha_botoes = []
        for j in range(colunas):
            btn = tk.Button(frame_campo, image=img_nada, width=20, height=20)
            btn.grid(row=i, column=j)
            btn.config(command=lambda i=i, j=j: clique_esquerdo(i, j))
            btn.bind("<Button-3>", lambda e, i=i, j=j: clique_direito(e, i, j))
            linha_botoes.append(btn)
        botoes.append(linha_botoes)

#acao de elecionar um campo vazio
def clique_esquerdo(linha, coluna):
    valor = matriz[linha][coluna]
    botoes[linha][coluna].config(command=lambda: None)
    botoes[linha][coluna].unbind("<Button-3>")
    match valor:
        case '💣':
            botoes[linha][coluna].config(image=img_bomba_perda)
            revelar_campo_minado(False)
        case 0:
            revelar_vizinhos_zeros(linha, coluna)
        case _:
            imagem = globals().get(f"img_n{valor}_bomba")
            botoes[linha][coluna].config(image=imagem)
    verificar_vitoria()

#coloca a bandeirinha onde acha que e bomba
def clique_direito(event, linha, coluna):
    current_image = botoes[linha][coluna].cget('image')
    if current_image == str(img_bandeira):
        botoes[linha][coluna].config(image=img_nada)
    else:
        botoes[linha][coluna].config(image=img_bandeira)
    verificar_vitoria()

#verifica se todo o campo minado foi preenchido corretamente
def verificar_vitoria():
    bandeiras_corretas = True
    campos_revelados = True

    for i in range(linhas):
        for j in range(colunas):
            botao = botoes[i][j]
            valor = matriz[i][j]
            imagem_atual = botao.cget('image')

            if valor == '💣':
                if imagem_atual != str(img_bandeira):
                    bandeiras_corretas = False
            else:
                if imagem_atual == str(img_bandeira) or imagem_atual == str(img_nada):
                    campos_revelados = False

    if bandeiras_corretas or campos_revelados:
        revelar_campo_minado(True)

#revela todos os campos proximos que estao com 0 para exibir
def revelar_vizinhos_zeros(linha, coluna):
    visitados = set()
    fila = [(linha, coluna)]

    while fila:
        i, j = fila.pop(0)
        if (i, j) in visitados:
            continue
        visitados.add((i, j))
        if botoes[i][j].cget('image') == str(img_bandeira):
            continue
        valor = matriz[i][j]
        botoes[i][j].config(command=lambda: None)
        botoes[i][j].unbind("<Button-3>")
        if valor == 0:
            botoes[i][j].config(image=img_n0_bomba)
            for x in range(max(0, i - 1), min(linhas, i + 2)):
                for y in range(max(0, j - 1), min(colunas, j + 2)):
                    if (x, y) not in visitados:
                        fila.append((x, y))
        else:
            imagem = globals().get(f"img_n{valor}_bomba")
            if imagem:
                botoes[i][j].config(image=imagem)

#mostra todo o campo minado e exibe a mensagem final
def revelar_campo_minado(isWin):
    for i in range(linhas):
        for j in range(colunas):
            valor = matriz[i][j]
            botao = botoes[i][j]
            botao.config(command=lambda: None)
            botao.unbind("<Button-3>")
            if botao.cget('image') == str(img_bandeira):
                continue
            if valor == '💣':
                    if isWin:
                        botao.config(image=img_bandeira)
                    else:
                        botao.config(image=img_bomba_perda)
            elif isinstance(valor, int):
                if valor == 0:
                    botao.config(image=img_n0_bomba)
                else:
                    imagem = globals().get(f"img_n{valor}_bomba")
                    if imagem:
                        botao.config(image=imagem)
    if isWin :
        messagebox.showinfo("Vitória", "Parabéns! Você venceu o jogo!")
    else:
        messagebox.showinfo("Você perdeu", "Você clicou em uma bomba!")

    frame_botoes = tk.Frame(frame_jogo)
    frame_botoes.pack(pady=10)

    btn_tentar_novamente = tk.Button(frame_botoes, text="Jogar Novamente", height=2, width=20,
                                     command=lambda: validar_e_prosseguir_simples())
    btn_voltar_menu = tk.Button(frame_botoes, text="Voltar ao Menu", height=2, width=20, command=mostrar_menu)

    btn_tentar_novamente.pack(side="left", padx=10)
    btn_voltar_menu.pack(side="right", padx=10)


#recria o campo minado caso de vitoria ou derota
def validar_e_prosseguir_simples():
    global botoes, matriz, linhas, colunas, bombas
    botoes = []
    matriz = criar_matriz(linhas, colunas)
    adicionar_bombas(matriz, bombas)
    iniciar_jogo(linhas, colunas)

#cria a janela de exibicao com as informações
janela = tk.Tk()
janela.title("Campo minado")
janela.geometry("1200x800")

#importa as imagens para o projeto 
img_nada = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'botaoNada.png'))
img_bandeira = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'bandeira.png'))
img_bomba_perda = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'bombaPerda.png'))
img_n0_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N0.png'))
img_n1_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N1.png'))
img_n2_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N2.png'))
img_n3_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N3.png'))
img_n4_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N4.png'))
img_n5_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N5.png'))
img_n6_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N6.png'))
img_n7_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N7.png'))
img_n8_bomba = tk.PhotoImage(file=os.path.join(base_path, 'imagens', 'N8.png'))

#inicia o app
mostrar_menu()
janela.mainloop()
