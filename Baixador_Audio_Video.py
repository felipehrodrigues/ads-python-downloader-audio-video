import yt_dlp
import tkinter as tk
import os

def baixarAudio(link):
    
    caminhoDownload = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(caminhoDownload, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        
        
def baixarVideoCompleto(link):
    
    caminhoDownload = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(caminhoDownload, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        
    
def informacoesVideoBaixado(link):
    ydl_opts = {
        'format': 'bestaudio'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        informacoes = ydl.extract_info(link, download=False)
        
        nome = informacoes.get('title')
        duracao = informacoes.get('duration')
        autor = informacoes.get('uploader')
        
        informacoesBaixado = f"Titulo: {nome}\nAutor: {autor}\nDuração: {duracao // 60}m {duracao % 60}s "
        
    
    detalhes.delete("1.0", tk.END)
    detalhes.insert(tk.END, informacoesBaixado)
    
def baixarLinkAudio():
    link = colarLink.get()
    if link:
        informacoesVideoBaixado(link)
        baixarAudio(link)
    else:
        print("Link com erro")
        
def baixarLinkVideoCompleto():
    link = colarLink.get()
    if link:
        informacoesVideoBaixado(link)
        baixarVideoCompleto(link)
    else:
        print("Link com erro")

textoLegal = "\nEsta aplicação foi desenvolvida exclusivamente para fins educacionais e de testes pessoais. O uso deste software para baixar conteúdos do YouTube ou outras plataformas pode violar os termos de serviço dessas plataformas, especialmente no caso de materiais protegidos por direitos autorais. O desenvolvedor não se responsabiliza por qualquer uso inadequado desta ferramenta. Ao utilizar esta aplicação, você concorda em usar de forma ética e legal, respeitando os direitos dos criadores de conteúdo e os termos de uso das plataformas envolvidas."

janela = tk.Tk()
janela.title("Baixar áudio do youtube")
janela.geometry("1000x600")
janela.resizable(False, False)
janela.configure(bg="#121212", pady=15, padx=15)

titulo = tk.Label(janela, text="Cole o Link para baixar Audio e/ou Video", font=("Verdana" , 15), bg="#121212", fg="#E0E0E0", pady=10 )
titulo.pack(pady=20)

colarLink = tk.Entry(janela, width=150, bg="#252525", fg="#00FFAB" )
colarLink.pack()

botao = tk.Button(janela, text="Download do Video", command=baixarLinkVideoCompleto, pady=5, padx=5, width=20, bg="#ffffff", fg="#121212")
botao.pack(pady=5)

botao = tk.Button(janela, text="Download do Áudio", command=baixarLinkAudio, pady=5, padx=5, width=20, bg="#ffffff", fg="#121212")
botao.pack(pady=5)

detalhes = tk.Text(janela, pady=5, bg="#1A1A1A", fg="#E0E0E0", height=10)
detalhes.pack(pady=10)

infosLegais = tk.Text(janela, bg="#1A1A1A", fg="#E0E0E0", padx=10, pady=15, width=150)
infosLegais.insert(tk.END, textoLegal)
infosLegais.pack()

janela.mainloop()

