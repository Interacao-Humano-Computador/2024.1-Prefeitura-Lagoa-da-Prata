## Introdução

A criação inicial de um ambiente de análise requer a elaboração de uma narrativa que descreva indivíduos envolvidos em uma atividade específica. Essa narrativa pode ser textual ou visual, por meio de imagens, e deve incluir um contexto detalhado. O objetivo é representar uma situação de uso de uma aplicação, envolvendo usuários, processos e dados relevantes. Para nossa disciplina, os cenários são essenciais para avaliar a satisfação do usuário com o produto em questão e para facilitar a compreensão da atividade.

## Cenários

Para cada cenário elaborado, é importante detalhar os elementos característicos, que incluem contexto, atores, objetivos, planejamento, ações, eventos e avaliação. Os atores desses cenários são as personas criadas para o projeto.

## Metodologia

Este artefato utiliza a metodologia de Cenários, baseada em histórias sobre pessoas realizando atividades, conforme descrito por Rosson e Carroll (2002). A modelagem dos cenários segue os princípios apresentados nos slides do capítulo 6 do livro "Interação Humano Computador" de Simone Barbosa.

## Modelo de Cenário

Para a descrição dos cenários, adotamos o formato de texto estruturado, com algumas adaptações para fins de aprendizado. A Tabela 1 a seguir apresenta o molde utilizado para cada cenário:

<center>

| Elemento   | Descrição                                                        |
| ---------- | ---------------------------------------------------------------- |
| Objetivo   | Objetivo do cenário                                              |
| Contexto   | Detalhes da situação                                             |
| Recursos   | Objetos que interagem com os atores                              |
| Ator       | Pessoa participante do cenário                                   |
| Episódios  | Sequência de ações realizadas pelos atores envolvidos no cenário |
| Restrições | Possíveis impedimentos às ações dos usuários                     |
| Exceção    | Possíveis casos e eventos que fujam do comum nos episódios       |

 Tabela 1: Molde dos cenários (Fonte: FREITAS, Cainã. 2024).

</center>

## Cenários Identificados
Os cenários identificados, tendo como base as [Personas](personas.md) desenvolvidas no projeto, estão apresentados nas Tabelas a seguir:

### C01: Consultar Panorama Econômico
Abaixo se encontra a tabela que especifica o elemento e sua descrição.

<center>

| Elemento   | Descrição                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Objetivo   | Consultar a lista de medicamentos disponiveis na saúde pública do municipio.                                                                                                                                                   |
| Contexto   | Local: No trabalho <br> Tempo: Durante todo o dia <br> Pré-condições: Acesso à Internet                                                                                                                                        |
| Recursos   | Internet, computador ou celular e site da Prefeitura Municipal                                                                                                                                                                 |
| Ator       | Eduardo, um médico                                                                                                                                                                                                                      |
| Episódios  | - Eduardo acessa o site da prefeitura em seu navegador <br> - Ele navega até a seção "Serviços para o Cidadão" <br> - Eduardo procura e encontra a opção "Lista de Medicamentos Disponíveis" <br> - Eduardo clica na opção e é redirecionada para uma nova página <br> - Na nova página, Eduardo visualiza um botão ou link para acessar a lista em formato PDF <br> - Eduardo clica no botão/link para abrir o PDF <br> |
| Restrições | Fluxo de navegação intuitivo.                                                                                                                                                                                                  |
| Exceção    | Falta de internet ou de energia.                                                                                                                                                                                               |

Tabela 2: Consultar Panorama Econômico (Fonte: FREITAS, Cainã. 2024).
</center>

### C02: Acesso à Fila de Espera de Creches Municipais

<center>

| Elemento   | Descrição                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Objetivo   | Consultar quadro de vagas das creches.                                                                                                                                                   |
| Contexto   | Local: Em casa <br> Tempo: Durante a tarde <br> Pré-condições: Acesso à Internet, computador ou celular                                                                                                                                        |
| Recursos   | Internet, computador ou celular e site da Prefeitura Municipal                                                                                                                                                                 |
| Ator       | Maria, moradora da cidade                                                                                                                                                                                                                      |
| Episódios  | - Maria acessa o site da prefeitura em seu navegador <br> - Ela navega até a seção "Serviços para o Cidadão" <br> - Maria procura e encontra a opção "Fila de Espera para Creches Municipais" <br> - Ela clica na opção e é redirecionada para uma nova página <br> - Na nova página, Maria visualiza um botão ou link para acessar o quadro de vagas em formato PDF <br> - Maria clica no botão/link para abrir o PDF <br> |
| Restrições | O site da prefeitura deve possuir uma seção específica para serviços públicos e uma opção clara para acessar o quadro de vagas das cheches.                                                                                                                                                                                                  |
| Exceção    | Falta de internet ou problema de conexão com o site da prefeitura.                                                                                                                                                                                               |

Tabela 3: Consultar Panorama Econômico (Fonte: DIONIZIO, Joyce. 2024).

</center>


### C03: Consultar edital de concursos e processos seletivos
Abaixo se encontra a tabela que especifica o elemento e sua descrição.

<center>

| Elemento   | Descrição                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Objetivo   | Consultar os editais de concursos e processos seletivos.                                                                                                                                                                       |
| Contexto   | Local: Em casa <br> Tempo: Durante todo o dia <br> Pré-condições: Acesso à Internet, computador ou celular                                                                                                                     |
| Recursos   | Internet, computador ou celular e site da Prefeitura Municipal                                                                                                                                                                 |
| Ator       | Diogo, buscando realizar concursos.                                                                                                                                                                                            |
| Episódios  | - Diogo acessa o site <br> - Ele navega até "Edital" <br> - Ele clica em "Concursos e processos seletivos" <br> - Ele encontra informações que estava buscando sobre os concursos e processos seletivos <br>                   |
| Restrições | Fluxo de navegação intuitivo.                                                                                                                                                                                                  |
| Exceção    | Falta de internet, energia ou problema de conexao com o site da prefeitura.                                                                                                                                                                                               |

Tabela 4: Consultar edital de concursos e processos seletivos (Fonte: DUARTE, Augusto. 2024).
</center>

### C04: Gerar evento pelo site
Abaixo se encontra a tabela que especifica o elemento e sua descrição.

<center>

| Elemento   | Descrição                                                                                                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Objetivo   | Gerar evento cultural e publicar no site da prefeitura                                                                                                                                                                       |
| Contexto   | Local: Em escritório <br> Tempo: Turno da tarde <br> Pré-condições: Acesso à Internet, computador ou celular                                                                                                                     |
| Recursos   | Internet, computador e site da Prefeitura Municipal                                                                                                                                                                 |
| Ator       | Diego, verificando a caixa de mensagens e confirmando a intenção de um ator externo à realizar um evento.                                                                                                                                                                                            |
| Episódios  | - Diego acessa o email de contato <br> - Ele verifica um email que contém informações sobre a intenção de realização de um evento <br> - Ele repassa as informações aos superiores <br> - Ele recebe a resposta e indica ao remetente inicial a decisão <br> Em caso negativo, ele informa os motivos e finaliza sua função <br> Em caso positivo, ele reconfirma as informações, monta uma imagem para publicação e valida com o remetente inicial <br> Diego acessa o site da prefeitura <br> Ele navega ao menu completo e acessa a área de "Eventos" <br> Ele aperta no botão para adicionar um evento <br> Ele preenche os dados de imagem, data de ínicio e término e adiciona uma descrição ao evento <br> Por fim, ele confirma os dados novamente e realiza a postagem.   |
| Restrições | Fluxo de navegação intuitivo, confirmação de dados de superiores.                                                                                                                                                                                                  |
| Exceção    | Falta de internet, energia ou problema de conexao com o site da prefeitura, indivíduos secundários inalcançáveis.                                                                                                                                                                                               |

Tabela 5: Gerar evento pelo site (Fonte: MEIRELES, Lucas. 2024).
</center>

### C05: Gerar listagem de editais de licitação
A tabela abaixo especifica o elemento assim como a descrição do cenário especificado.

<center>

| Elemento   | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objetivo   | gerar listagem de editais de licitação                                                                                                                                                                                                                                                                                                                                                                                                   |
| Contexto   | Local: Na empresa <br> Tempo: Durante o período de trabalho <br> Pré-condições: Acesso à Internet, computador ou celular                                                                                                                                                                                                                                                                                                                 |
| Recursos   | Internet, computador ou celular e site da Prefeitura Municipal da Lagoa da Prata                                                                                                                                                                                                                                                                                                                                                         |
| Ator       | Maria Arlete, buscando uma listagem dos editais de licitação em aberto.                                                                                                                                                                                                                                                                                                                                                                  |
| Episódios  | - Maria Arlete acessa o site <br> - Ela navega até o menu suspenso e passa o mouse em "Editais" <br> - Ela clica na opção "Licitações" <br> - Ela move o cursor até a tabela de busca na aba "Situação" <br> - Ela clica na opção e seleciona "Abertos" <br> - Ela move o cursor até o botão "Buscar" <br> - Ela clica no botão "Buscar" <br> - Ela move o cursor até o botão CSV <br> - Ela clica no botão CSV, baixando o arquivo <br> |
| Restrições | Fluxo de navegação intuitivo.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Exceção    | Falta de internet, energia ou problema de conexao com o site da prefeitura.                                                                                                                                                                                                                                                                                                                                                              |

Tabela 6: Cadastrar filho na creche (Fonte: DOURADO, Pedro Lucas. 2024).
</center>

## Bibliografia
[1] CENÁRIOS: Rastreamento de Cenários. [S. l.]. Disponível em: http://www-di.inf.puc-rio.br/~julio/bnncap3.pdf. Acesso em: 06/05/2024.

## Historico de revisão

|    Data    | Versão |            Descrição             |                   Autor(es)                   | Data de revisão |                 Revisor(es)                 |
| :--------: | :----: | :------------------------------: | :-------------------------------------------: | :-------------: | :-----------------------------------------: |
| 06/05/2024 | `1.0`  |       Criação do documento       | [Cainã Freitas](https://github.com/freitasc)  |   06/05/2024    | [Pedro Lucas](https://github.com/lucasdray) |
| 06/05/2024 | `1.1`  |        Adição de Cenário         | [Joyce Dionizio](https://github.com/joycejdm) |   06/05/2024    | [Pedro Lucas](https://github.com/lucasdray) |
| 06/05/2024 | `1.2`  |        Adição de Cenário         | [Augusto Duarte](https://github.com/Augcamp)  |   06/05/2024    | [Pedro Lucas](https://github.com/lucasdray) |
| 06/05/2024 | `1.3`  |        Adição de Cenário         | [Lucas Meireles](https://github.com/Katuner)  |   06/05/2024    | [Pedro Lucas](https://github.com/lucasdray) |
| 06/05/2024 | `1.4`  | Adição de Cenário e Bibliografia |  [Pedro Lucas](https://github.com/lucasdray)  |   07/05/2024    |   [Augusto Duarte](https://github.com/Augcamp)                                          |
| 10/05/2024 | `1.5`  |        Correção pós entrega e edição de cenário         | [Lucas Meireles](https://github.com/Katuner)  |      |  |