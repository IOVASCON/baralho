import tkinter as tk
from tkinter import messagebox
from utils import baralho

def jogar():
    """
    Função chamada quando o botão 'Jogar' é clicado. 
    Gera mãos aleatórias para os jogadores, compara e exibe o resultado.
    """
    mao_a, mao_b = baralho.gerar_maos()
    cartas_a = baralho.exibir_cartas(mao_a)
    cartas_b = baralho.exibir_cartas(mao_b)
    pontos_a, pontos_b = baralho.comparar_maos(mao_a, mao_b)
    resultado = baralho.determinar_vencedor(pontos_a, pontos_b)

    resultado_texto = (
        f"Jogador A: {cartas_a}\n"
        f"Jogador B: {cartas_b}\n\n"
        f"{resultado}"
    )
    
    # Exibe o resultado em uma caixa de mensagem
    messagebox.showinfo("Resultado", resultado_texto)

# Configuração da janela principal do Tkinter
root = tk.Tk()
root.title("Jogo de Cartas")
root.geometry("400x300")

# Criação de um título
titulo = tk.Label(root, text="Jogo de Cartas", font=("Helvetica", 16))
titulo.pack(pady=20)

# Criação do botão 'Jogar' que chama a função jogar
botao_jogar = tk.Button(root, text="Jogar", command=jogar, font=("Helvetica", 14))
botao_jogar.pack(pady=20)

# Inicia o loop principal da aplicação
root.mainloop()
