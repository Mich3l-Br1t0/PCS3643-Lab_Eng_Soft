# PCS3643-Lab_Eng_Soft Grupo 04 

## Nomes:
- Michel Brito - 11257755 
- Pedro Henrique Rodrigues de Viveiros - 11804035 
- Victor de Almeida Santana - 11806718 

## **Passo 1: Instalar Python 3.10.X**
- Onde instalar: https://www.python.org/downloads/
- (Windows) Adicionar ao path. 

## **Passo2: Configuração**
- Clonar repositório na pasta desejada. 
- Via Powershell entrar na pasta PCS-LAB_ENG_SOFT.
- Criar ambiente virtual: 
  - Atualizar versão do pip: `python -m pip install --upgrade pip`
  - Instalação do ambiente virtual: `python -m venv env`
- Ativação do ambiente virtual: 
  - Executar o script: `.\env\scripts\Activate.ps1`
  - ! Uma vez que está no ambiente virtual, há uma indicação (env) antes do caminho atual no terminal. !
 ## *Rodando a aplicação:* 
 - Com o ambiente virtual ativado, digitar: `python manage.py runserver`

 ## Configurando o linter e formatter
 1. Rodar o comando `pip install ´r requirements.txt`
 2. Instalar pre-commit com o comando `pre-commit install`
 3. Ir nas configurações da extensão do Python para VSCode e, pesquisando *Formatting* selecionar o *black* como formatter padrão
 4. (OPCIONAL) Ir nas configurações gerais do VSCode e, pesquisando *Format on save* habilitar a checkbox
 5. Usar o atalho Ctrl+Shift+P para selecionar linter e escolher o flake8
 4. Para formatar todos os arquivos, utilizar o comando `black .`
