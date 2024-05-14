# Análise de Tarefas

## Introdução

&emsp;&emsp;Uma análise de tarefas é utilizada para se ter um entendimento sobre qual é o trabalho dos usuários, como eles o realizam e por quê. Nesse tipo de análise, o trabalho é definido em termos dos objetivos que os usuários querem ou precisam atingir. [1]
<br>
&emsp;&emsp;No contexto da análise de tarefas, uma abordagem valiosa é a identificação da situação atual, seja ela suportada ou não por um sistema computacional. Essa análise pode ser empregada tanto para o (re)design de sistemas quanto para avaliar os resultados de intervenções que incluam a introdução de novos sistemas computacionais. Um dos passos iniciais cruciais nesse processo é a coleta dos objetivos das pessoas ao interagirem com o sistema em análise.
<br>
&emsp;&emsp;O site da Prefeitura da Lagoa da Prata é um site majoritariamente informativo, disponibilizando de uma gama de informações. O usuário pode acessar informações como: Fila de espera de creches munipais; lista de medicamentos disponíveis; calendário de eventos relacionados ao municipio; entre outros tipos de informação.

## Metodologia

&emsp;&emsp;A metodologia para o desenvolvimento das análises de tarefas foi estabelecida com o objetivo de explorar diversas técnicas, selecionando aquela mais adequada para cada tarefa em questão. As técnicas escolhidas foram a AHT (Análise Hierárquica de Tarefas) e o CMN-GOMS (Card, Moran e Newell GOMS). Essa análise é fundamental para identificar o fluxo de passos das tarefas, permitindo a identificação de áreas que necessitam de melhorias.

Para este projeto, serão utilizadas ambas as técnicas mencionadas anteriormente, realizando uma ligação direta com os cenários estabelecidos e utilizando
tarefas que podem ser associadas às personas declaradas. A forma da AHT será utilizada principalmente em tarefas complexas que não são repetitivas e podem assumir diversas dependências. Já o CMN-GOMS será utilizado como base geral para os cenários e análise das etapas para se alcançar o objetivo primário.

## HTA - Análise Hierárquica de Tarefas


&emsp;&emsp;Desenvolvida na década de 1960, a Análise Hierárquica de Tarefas (HTA) é uma ferramenta empregada para compreender as competências e habilidades necessárias para realizar tarefas complexas e não repetitivas. Além disso, é valiosa para identificar problemas de desempenho. A HTA facilita a compreensão das relações entre as ações das pessoas, os motivos que as impulsionam e as consequências caso essas ações não sejam executadas corretamente.


&emsp;&emsp;A Tabela 1 apresenta os elementos de uma análise hierárquica de tarefas.

| Elemento | Descrição | 
| --                           | ---- | 
| Tarefa: | Uma parte do trabalho que requer realização, frequentemente definida em termos de objetivos e subobjetivos. |
| Objetivo: | Um estado específico, um estado final, determinado por eventos ou por valores observáveis de variáveis, que servem como critério para alcançar o objetivo. |
| Subobjetivo:| Uma subdivisão de objetivos complexos, usada para identificar quais subobjetivos são mais difíceis de alcançar, já que limitam ou até mesmo impedem o alcance do objetivo principal. |
| Plano: | Define os subobjetivos necessários para alcançar um objetivo maior e a ordem em que esses subobjetivos devem ser alcançados. |
| Operação: | As circunstâncias em que o objetivo é ativado (entrada), as atividades ou ações que contribuem para alcançá-lo e as condições que indicam o seu alcance (feedback). |
<div align="center">
<p> <b>Tabela 1</b>: Elementos de uma HTA (Fonte: FREITAS, Cainã. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/elementosHTA.png" width="100%">

<div align="center">
<p> <b>Figura 1</b>: Elementos de um diagrama HTA </p>
</div>

<p align="justify">

&emsp;&emsp;Os planos podem possuir relações entre os subobjetivos, como: sequência fixa (um objetivo deve ser atingido antes do próximo); regra de seleção ou decisão (quais objetivos que deverão ser atin-gidos dependem das circunstâncias); ou em paralelo (mais de um objetivo deve ser atingido ao mesmo tempo). A Figura 1 apresenta a forma gráfica de representação dessas relações.
</p>


### Análise da Tarefa HTA 1: Fazer Download da Última Movimentação de uma Licitação

| Objetivos / Operações                                | Relações      | Problemas / Recomendações                                                                                                      |
|------------------------------------------------------|---------------|----------------------------------------------------------|
| 0. Fazer Download da Última Movimentação de uma Licitação |1 > 2|       Input: Acesso ao site de Lagoa da Prata, Credenciais de login (usuário e senha). <br> Plano: Realizar login no site, Navegar para a seção de editais de licitações, Selecionar o edital desejado, Acessar o edital, Navegar para a seção de movimentações do edital, Fazer download da última movimentação. <br> Feedback: Download concluído da última movimentação.|
|   1. Realizar login no site   | 1 > 2|    Plano: informar o cpf e depois a senha do gov.br. <br> Feedback: tela menu de Serviços Registrato. |
|     1.1 Informar CPF | |           |
|     1.2 Informar senha do gov.br   | |  |
|   2. Navegar para a seção de editais de licitações ||   Plano: Clicar no botão que leva a tela de editais de licitações <br>Feedback: Tela que seleciona qual tela sobre os editais você quer ir  |
|     2.1 Clicar no botão que leva a editais de licitações |  |     |
|   2.2 Selecionar a página de editais de licitações   | | |
|   2.3 Clicar no botão que leva a tela de editais de licitações   | | |
|   3. Buscar o edital desejado com a ferramenta de consulta | |   Plano: Usar a ferramenta de consulta  <br>Feedback: Aparecer o edital esperado na tela de pesquisa |
|     3.1. Inserir nome do edital ou outra característica | |  |
|     3.2. Clicar em "Consultar"                       | |  |
|   3.3 Acessar o edital selecionado                    | |        Plano: Acessar o edital para download   |
|     3.4. Clicar no botão que leva ao edital selecionado | |  |
|   4. Navegar para a seção de movimentações do edital | |    Plano: Navegar até a seção de movimentação, fazer download da movimentação|
|     4.1. Clicar no botão que leva à seção de movimentações do edital | |                         |
|     4.2. Clicar no botão de download do último movimento da licitação | |      

<div align="center">
<p> <b>Tabela 2</b>: HTA da Tarefa: Fazer Download da Última Movimentação de uma Licitação (Fonte: Heler, Lucas. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA1.png" width="100%">
<div align="center">
<p> <b>Figura 2</b>: Diagrama HTA da Tarefa: Fazer Download da Última Movimentação de uma Licitação </p>
</div>

## CNM-GOMS

&emsp;&emsp;O GOMS (Goals, Operators, Methods, and Selection Rules - Objetivos, Operadores, Métodos e Regras de Seleção) é um conjunto de modelos utilizados para análise de tarefas. O CMN-GOMS (Card, Moran e Newell GOMS) é um desses modelos e consiste em uma hierarquia bem definida de objetivos representados em forma de programa, permitindo assim uma análise executável. (Barbosa e Silva, 2010)

## Legenda
| Termo    | Tradução         | Descrição                                                             |
| -------- | ---------------- | --------------------------------------------------------------------- |
| Goal     | Objetivo         | O que o usuário quer realizar utilizando o sistema                    |
| OP       | Operador         | Ações concretas que o site permite que o usuário faça                 |
| METHOD   | Método           | Sequência de subobjetivos e operadores para atingir um objetivo maior |
| SEL.RULE | Regra de seleção | Tomada de decisão sobre qual método utilizar                          |

### Análise da Tarefa CNM-GOMS 1: Consultar quantidade de DIPIRONA na lista de medicamentos disponíveis
```
Goal 0: Consultar lista de medicamentos disponíveis
  Goal 1: Encontrar serviços de pessoa física
    METHOD 1.A: Encontrar através do menu GOVERNO
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até menu "SERVIÇOS PARA O CIDADÃO"
        OP: Levar cursor até menu "LISTA DE MEDICAMENTOS DISPONIVEIS"
        OP: Levar cursor até botão "ACESSAR"
        OP: Clicar com o botão esquerdo do mouse
    METHOD 1.B: Encontrar através da aba de pesquisa
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "medicamentos"
        OP: Levar cursor até botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até "LISTA DE MEDICAMENTOS DISPONIVEIS"
  Goal 2: Pesquisar medicamento
    OP: Apertar botões "CTRL" + "F"
    OP: Digitar "DIPIRONA"
    OP: Consultar valor no lado direito da lista
```

### Análise da Tarefa CNM-GOMS 2: Consultar Quadro de Vagas das Creches Municipais
```

Goal 0: Consultar quadro de vagas das creches municipais
  Goal 1: Encontrar serviços de pessoa física
    METHOD 1.A: Encontrar através do menu "Serviços para o Cidadão"
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até menu "SERVIÇOS PARA O CIDADÃO"
        OP: Levar cursor até menu "FILA DE ESPERA PARA CRECHES MUNICIPAIS"
        OP: Levar cursor até botão "ACESSAR"
        OP: Clicar com o botão esquerdo do mouse
    METHOD 1.B: Encontrar através da aba de pesquisa
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "creches"
        OP: Levar cursor até botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até "FILA DE ESPERA PARA CRECHES MUNICIPAIS"
  Goal 2: Acessar quadro de vagas
    OP: Na nova página, visualizar um botão ou link para acessar o quadro de vagas em formato PDF
    OP: Clicar no botão/link para abrir o PDF
```

### Análise da Tarefa CNM-GOMS 3: Visualizar e baixar editais de concursos e processos seletivos
```

Goal 0: Visualizar e baixar editais de concursos e processos seletivos
  Goal 1: Acessar o site da prefeitura municipal
    METHOD: Acessar atráves do menu “EDITAIS”
        OP: Levar o cursor do mouse até o menu “EDITAIS” 
        OP: Localizar Concursos e Processos Seletivos
        OP: Levar o cursor do mouse até Concursos e Processos Seletivos
        OP: Clicar com o botão esquerdo do mouse
  Goal 2: Visualizar e baixar editais de concursos e processos seletivos
    OP: Localizar o edital desejado
    OP: Clicar com o botão esquerdo do mouse 
    OP: Localizar “Arquivos”
    OP: Levar o cursor do mouse até “Arquivos”
    OP: Clicar com o botão esquerdo do mouse
    OP: Na nova página, localizar “EDITAL” na parte inferior para acessar o PDF
    OP: Clicar no botão/link para abrir o PDF
```
### Análise da Tarefa CNM-GOMS 4: Gerar novo evento no site
```
Goal 0: Criar um novo evento público no site
  Goal 1: Receber informações de intenção de um novo evento
    METHOD 1.A: Verificar mensagens sobre eventos já preparados
        OP: Acessar mensagens dos encarregados de eventos
        OP: Confirmar informações do evento
    METHOD 1.B: Verificar a intenção de um indivíduo externo a realizar um evento
    (SEL. RULE: Caso não tenha 1.B)
      OP: Acessar a caixa de email
      OP: Acessar um email e verificar os dados
  Goal 2: Confirmar a disponibilidade do local na data e horário
    
    Goal 3: Acessar a aba de eventos
      OP: Acessar a página inicial do site
      OP: Mover o mouse até o menu geral
      OP: Selecionar "Eventos", abaixo do tópico "A nossa cidade"
    
    METHOD 2.A: Verificação separada
      OP: Mover a página até que se veja algum evento
      OP: Comparar o local e data do evento com o que se deseja registrar
      OP: Mover a página até o próximo evento e repetir
    METHOD 2.B: Verificação pelo calendário
      OP: Movimentar o mouse até a data inicial no calendário
      OP: Verificar se algum evento irá aparecer
      OP: Clicar no evento para confirmar horário e local
  Goal 4: Registrar evento
    OP: Movimentar o mouse até o botão de adicionar
    OP: Escolher o arquivo de imagem
    OP: Preencher os campos de data inicial e término
    OP: Adicionar uma descrição ao evento
    OP: Clicar para publicar o evento
```

### Análise da Tarefa CNM-GOMS 5: Gerar relatório de licitações em aberto em CSV
```
Goal 0: Gerar relatório de licitações em aberto
  OP. 0.1: Abrir o site da prefeitura municipal da Lagoa da Prata em um navegador web.
  Goal 1: Abrir buscador
    Op. 1.1: Mover cursor até o menu suspenso na aba "EDITAIS"
    Op. 1.2: Clicar na opção "Licitações"
  Goal 2: fazer busca
    Op. 2.1: Mover o cursor na até a busca detalhada na aba "Situação"
    Op. 2.2: Clicar com o botão esquerdo para abrir as opções
    Op. 2.3: Clicar na opção "Aberto"
    Op. 2.4: Mover cursor até o botão "Buscar"
    Op. 2.5: Clicar com o botão esquerdo no botão "Buscar"
  Goal 3: Baixar arquivo CSV
    Op. 3.1: Mover cursor até botão "CSV"
    Op. 3.2: CLicar no botão "CSV"

 

```

## Historico de revisão

|    Data    | Versão |             Descrição              |                   Autor(es)                   | Data de revisão |                 Revisor(es)                  |
| :--------: | :----: | :--------------------------------: | :-------------------------------------------: | :-------------: | :------------------------------------------: |
| 06/05/2024 | `1.0`  |        Criação do documento        | [Cainã Freitas](https://github.com/freitasc)  |   07/05/2024    | [Lucas Meireles](https://github.com/Katuner) |
| 06/05/2024 | `1.1`  |    Adição de Análise de Tarefas    | [Joyce Dionizio](https://github.com/joycejdm) |   07/05/2024    | [Pedro Lucas](https://github.com/lucasdray)  |
| 06/05/2024 | `1.2`  |   Adição de Análise de Tarefas 3   | [Augusto Duarte](https://github.com/Augcamp)  |   07/05/2024    | [Pedro Lucas](https://github.com/lucasdray)  |
| 06/05/2024 | `1.3`  |   Adição de Análise de Tarefas 4   | [Lucas Meireles](https://github.com/Katuner)  |   07/05/2024    | [Pedro Lucas](https://github.com/lucasdray)  |
| 07/05/2024 | `1.4`  |   Adição de Análise de Tarefas 5   |  [Pedro Lucas](https://github.com/lucasdray)  |   07/05/2024    | [Lucas Heler](https://github.com/akaeboshi)  |
| 07/05/2024 | `1.5`  | Adição de Análise de Tarefas HTA 1 |  [Lucas Heler](https://github.com/akaeboshi)  |   07/05/2024    | [Pedro Lucas](https://github.com/lucasdray)  |
| 10/05/2024 | `1.6`  | Edição de Análise de Tarefa e correção pós entrega |  [Lucas Meireles](https://github.com/Katuner)  |       |   |
