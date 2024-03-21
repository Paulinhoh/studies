# Git e Github - Studies

## O que é versionamento de Código

É um sistema de controle de versão, que controla as versões de um arquivo ao longo do tempo.

- Registra o histórico de atualização de um arquivo;
- Gerencia quais foram as alterações, a data, o autor, etc...
- Organização, controle e segurança.

## Tipos de Sistemas de Controle de Versão

Dentre os sistemas de Controle de Versão ( VCS ), temos:

- VCS Centralizado ( CVCS )
  - Ex.: CVS, Subversion
- VCS Distribuídos ( DVCS )
  - Ex.: Git, Mercurial

### VCS Centralizado ( CVCS ):

Onde o banco de versões são salvos em um único servidor central, onde se acontecer algo e por um acaso o servidor ficar offline não se pode mexer no arquivo, com isso foi criado VCS Distribuídos.

### VCS Distribuídos ( DVCS ):

Onde os arquivos são no servidor central também são duplicados para os computadores locais de todos os desenvolvedores do projeto.
Clona o repositório completo, o que inclui o histórico de versões.

- Cada clone é como um backup
- Possibilita um fluxo de trabalho flexível
- Possibilidade de trabalhar sem conexão á rede

## O que é Git

Sistema de Controle de Versão Distribuído

- Gratuito e Open Source ( Código Aberto )
- Ramificações ( branching ) e fusões ( merging ) eficientes
- Leve e rápido

### Documentação: [Git - Documentation](https://git-scm.com/doc)

### Breve Histórico do Git:

2002 → O projeto de núcleo ( kernel ) do Linux, que é Open Source, começa a utilizar o BitKeeper, um DVCS proprietário.

2005 → Após alguns conflitos com a comunidade, o BitKeeper rescinde a licença gratuita. O que leva a Linux Torvalds, o criador do Linux, e sua equipe a desenvolverem sua própria ferramenta, o Git.

## O que é GitHub

Plataforma de hospedagem de código para controle de versão com Git, e colaboração.

- Comunidade ativa
- Utilizado mundialmente
- Mascote “Octocat”

### Documentação: [Documentação de ajuda do GitHub.com](https://docs.github.com/pt)

### Breve Histórico do GitHub:

2008 → Desenvolvido por Chris Wanstrath, J. Hyett, Tom Preston-Werner e Scott Chacon.

2018 → Vitima de um dos maiores ataques de DDoS ( ataque distribuído de negação de serviço ); Comprado pela Microsoft Corporation por US $ 7,5 bilhões.

## Configuraçãos e Autenticação Git

### Configurações iniciais

```bash
git config --global user.name "username"    # seta um username
git config --global user.email "email"      # seta um email
git config --global init.defaultBranch main # chama a branch principal de main

git config --global --list                  # lista as configs feitas
```

### Autenticando via Token

```bash
github.com → settings → Developer settings → Personal access tokens → token ( classic )


git config --global credential.helper cache # para salvar só durante um tempo
git config --global credential.helper store # para para sempre na maquina

git clone URL
# ira pedir o usuario do github e a senha que no lugar coloca o token
```

## Comandos Git

### Criando e clonando repositórios

```bash
git init # inicializa um repositório local com git
git remote add origin URL # para vincular um repositorio local com o do github
git branch -M main # muda o nome da brandh master para main
--------------------------------------------------------------------------------------------
git clone URL # clona um repositorio existente do github e ja inicializa o git
git clone URL NOVO-NOME # clone já com um novo nome
git clone URL --branch NOME-BRANCH --single-branch # clona do repositorio somente esta branch
```

### Salvando alterações no Repositório Local

```bash
git add ARQUIVO # Adiciona o arquivo a área de commit
git status # Mostra os status
git commit -m"MENSAGEM" # Commita os arquivos adicionados
git log # Mostra o commit
```

### Desfazendo alterações no Repositório Local

```bash
rm -rf .git # Exclui o arquivo Git
git restore ARQUIVO # Restaura o arquivo ao ultimo estado
git commit --amend -m"NOVA-MENSAGEM" # Altera a mensagem do Commit
git reset --ESCOLHA HASH # Retorna para um determinado commit
	--soft  # volta para o commit desejado e ja adiciona os arquivos no git add
	--mixed # volta para o commit desejado mas não adiciona os arquivos no git add
	--hard  # # volta para o commit desejado mas exclui os arquivos que não estavam no commit
git reset NOME-ARQUIVO  # tira o arquivo do git add
git restore --staged NOME-ARQUIVO # tira o arquivo do git add
```

### Enviando e baixando alterações com o Repositório Remoto

```bash
git push -u origin main # envia os arquivos para o github
git pull # puxa as alterações do github para o repositório local
```

### Trabalhando com Branches - Criando, mesclando, deletando e tratando conflitos

De maneira simples, uma Branch ( em tradução, “Ramo” ), é uma ramificação do seu projeto.

- É um ponteiro móvel para um commit no histórico do repositório;
- Quando você cria uma nova Branch a partir de outra existente, a nova se inicia apontando para o mesmo commit da Branch que estava quando foi criada.

```bash
git checkout -b NOME-BRANCH # Cria uma nova branch e altera para ela
git checkout NOME-BRANCH # altera entre as branchs
git branch -v # mostra o ultimo commit de cada branch
git merge NOME-BRANCH # mescla esta branch com a branch em que esta atualmente
git branch # lista as branchs
git branch -d NOME-BRANCH # exclui a branch
```

### Trabalhando com Branches - Comandos Úteis no Dia a Dia

```bash
git fetch origin main # baixa os arquivos do github mais não mescla
git diff BRANCH1 BRANCH2 # mostra as diferenças entre as branchs
git merge origin/main
----------------------------------------------------------------------------------------------
git clone URL --branch NOME-BRANCH --single-branch # clona do repositorio somente esta branch
----------------------------------------------------------------------------------------------
git stash ARQUIVO # arquiva algo
git stash list # lista arquivos arquivados
git stash pop # tras o ultimo arquivo arquivado e exclui da pilha
git stash apply # tras o ultimo arquivo arquivado e mantem na pilha
```

## Padronização de Commit

| Tipo de Commit | Descrição                                                             |
| -------------- | --------------------------------------------------------------------- |
| feat           | Adiciona uma nova funcionalidade ao projeto.                          |
| fix            | Corrige um bug ou problema no projeto.                                |
| docs           | Altera a documentação do projeto. Ex.: README, comentários no código. |
| style          | Realiza mudanças na aparência, sem alterar a funcionalidade.          |
| refactor       | Realiza mudanças no código que não alteram a funcionalidade.          |
| test           | Adiciona ou modifica testes no projeto.                               |
