# OrganizadorDeArquivos
Um script de automação em Python que organiza uma pasta (como Downloads) movendo arquivos para subpastas com base em sua extensão (.png, .pdf, etc.).
# 📂 Organizador de Pastas Automático

Este é um script de automação em Python criado para organizar qualquer pasta "bagunçada" (como a pasta de Downloads). Ele analisa todos os arquivos, identifica suas extensões (como `.pdf`, `.png`, `.mp4`) e os move automaticamente para subpastas categorizadas (como `Documentos`, `Imagens`, `Videos`).

Este projeto foi construído para praticar conceitos fundamentais de Python, como manipulação do sistema de arquivos, dicionários e tratamento de erros.

## ✨ Funcionalidades

* **Organização por Tipo:** Move arquivos baseado em extensões personalizáveis.
* **Criação Dinâmica de Pastas:** Cria automaticamente as pastas de destino (`Imagens`, `Documentos`, etc.) se elas não existirem.
* **Agrupamento Inteligente:** Arquivos não reconhecidos (ex: `.zip`, `.exe`) são movidos com segurança para uma pasta "Outros".
* **Robusto e Seguro:** O script pede o caminho e verifica se a pasta existe antes de tentar organizar, pedindo para o usuário tentar novamente em caso de erro.

## 🚀 Como Usar

1.  Baixe (ou clone) os arquivos deste repositório.
2.  Tenha o [Python 3](https://www.python.org/downloads/) instalado.
3.  Abra seu terminal (CMD, PowerShell, etc.) e navegue até a pasta onde você salvou o script.
4.  Execute o script:
    ```bash
    python organizador_de_arquivos.py
    ```
5.  Quando solicitado, cole o caminho completo da pasta que você deseja organizar e pressione Enter.

## 📸 Exemplo de Uso

**Pasta "Bagunçada" (Antes):**
C:\MINHA_BAGUNÇA

├── relatorio_final.pdf ├── foto_ferias.png ├── video_aula.mp4 └── instalador.exe


**Executando o Script:**
Digite o caminho da pasta a ser organizada: C:\MINHA_BAGUNÇA
Analisando arquivos...
DECISÃO: Mover 'relatorio_final.pdf' para a pasta 'Documentos'
DECISÃO: Mover 'foto_ferias.png' para a pasta 'Imagens'
DECISÃO: Mover 'video_aula.mp4' para a pasta 'Videos'
DECISÃO: Mover 'instalador.exe' para a pasta 'Outros'

Pasta "Organizada" (Depois):
C:\MINHA_BAGUNÇA\
├── Documentos\
│   └── relatorio_final.pdf
├── Imagens\
│   └── foto_ferias.png
├── Videos\
│   └── video_aula.mp4
└── Outros\
    └── instalador.exe
