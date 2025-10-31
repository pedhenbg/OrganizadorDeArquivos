import os
from pathlib import Path

MAPA_PASTAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Musica": [".mp3", ".wav"],
    
}
while True:
    print("===============Organizador de arquivos em python===============")
    print("----------------------------------------------------Por Pedro Gonçalves.")
    try:
        pasta_alvo = Path(input("Digite o caminho da pasta a ser organizada:"))


        print("Analisando arquivos")
        for item in pasta_alvo.iterdir():
            if not item.is_file() :
                continue
            encontrou_pasta = False

            for pasta_destino, extensoes in MAPA_PASTAS.items():
                if item.suffix in extensoes:
                    pasta_destino_final = pasta_alvo / pasta_destino
                    if not pasta_destino_final.exists():
                        pasta_destino_final.mkdir()
                    item.rename(pasta_destino_final / item.name)
                    print(f"DECISÃO:Mover '{item.name}' para a pasta '{pasta_destino}'")
                    encontrou_pasta = True
                    break
            if not encontrou_pasta:
                print(f"DECISÃO:Mover '{item.name}' para a pasta 'Outros'")
                pasta_outros = pasta_alvo / "Outros"
                if not pasta_outros.exists():
                        pasta_outros.mkdir()
                item.rename(pasta_outros / item.name)
        print("---Arquivos movidos com sucesso---")
        break

    except(FileNotFoundError):
        input("Pasta não encontrada.")    