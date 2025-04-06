# 🧨 Campo Minado em Python

Este projeto é uma implementação gráfica do clássico jogo **Campo Minado**, desenvolvida em **Python** utilizando a biblioteca **Tkinter**. O jogo permite ao usuário escolher o tamanho do campo e a quantidade de bombas, oferecendo uma experiência personalizada e desafiadora.

## 🎮 Como Jogar

- Ao iniciar o jogo, informe as **dimensões do campo** (máximo de 30x30) e a **quantidade de bombas**.
- Clique com o botão esquerdo para revelar um campo.
- Clique com o botão direito para **marcar** uma bomba com uma bandeira 🚩.
- O jogo termina quando:
  - Você revela todas as células **sem bombas** (vitória).
  - Você clica em uma bomba (derrota).

## 🧠 Regras

- Números indicam quantas bombas existem ao redor daquela célula.
- Zonas sem bombas revelam automaticamente áreas adjacentes.
- O número de bombas deve ser menor que o total de células do campo.

## 🖼️ Recursos Visuais

O jogo utiliza imagens para representar:
- Células vazias
- Números de 1 a 8
- Bombas
- Bandeiras

As imagens estão localizadas na **pasta `imagens/`** e são carregadas dinamicamente, compatíveis com versões executáveis geradas por ferramentas como o PyInstaller.

## 🛠️ Requisitos

- Python 3.10 ou superior
- Tkinter (incluído nas versões padrão do Python)
- Imagens da pasta `imagens/` (botaoNada.png, bandeira.png, bombaPerda.png, N0.png a N8.png)


## 👨‍🏫 Créditos

- Trabalho da disciplina Introdução à Programação com Python.
- Professor: Eduardo Poffo Medeiros Dias
- Aluno: Wallacy Alvarenga

## 📁 Estrutura do Projeto

```plaintext
Campo-Minado/
├── projeto.py
├── icone.ico
├── imagens/
│   ├── botaoNada.png
│   ├── bandeira.png
│   ├── bombaPerda.png
│   ├── N0.png
│   ├── N1.png
│   └── ... N8.png
```

## ▶️ Executando o Projeto

### Via código:
```bash
python projeto.py
```

### Via Executável (.exe):
Este projeto pode ser convertido para .exe com PyInstaller:
```bash
python -m pyinstaller --onefile --noconsole --add-data "imagens;imagens" --icon="icone.ico" projeto.py
```