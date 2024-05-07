# Análise de Tarefas

## Introdução

&emsp;&emsp;Uma análise de tarefas é utilizada para se ter um entendimento sobre qual é o trabalho dos usuários, como eles o realizam e por quê. Nesse tipo de análise, o trabalho é definido em termos dos objetivos que os usuários querem ou precisam atingir. [1]
<br>
&emsp;&emsp;No contexto da análise de tarefas, uma abordagem valiosa é a identificação da situação atual, seja ela suportada ou não por um sistema computacional. Essa análise pode ser empregada tanto para o (re)design de sistemas quanto para avaliar os resultados de intervenções que incluam a introdução de novos sistemas computacionais. Um dos passos iniciais cruciais nesse processo é a coleta dos objetivos das pessoas ao interagirem com o sistema em análise.
<br>
&emsp;&emsp;O site da Prefeitura da Lagoa da Prata é um site majoritariamente informativo, disponibilizando de uma gama de informações. O usuário pode acessar informações como: Fila de espera de creches munipais; lista de medicamentos disponíveis; calendário de eventos relacionados ao municipio; entre outros tipos de informação.

## Metodologia

&emsp;&emsp;A metodologia para o desenvolvimento das análises de tarefas foi estabelecida com o objetivo de explorar diversas técnicas, selecionando aquela mais adequada para cada tarefa em questão. As técnicas escolhidas foram a AHT (Análise Hierárquica de Tarefas) e o CMN-GOMS (Card, Moran e Newell GOMS). Essa análise é fundamental para identificar o fluxo de passos das tarefas, permitindo a identificação de áreas que necessitam de melhorias.

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


### Análise da Tarefa HTA 1: XXXXXXXXX

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
### Análise da Tarefa CNM-GOMS 4: Buscar vagas de emprego
```
Goal 0: Buscar quais vagas estão disponíveis para emprego no município
  Goal 1: Encontrar serviços de pessoa física
    METHOD 1.A: Encontrar através do menu "Serviços para o Cidadão"
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até ícone de "Menu" com todas as abas do site
        OP: Clicar no item menu "VAGAS DE EMPREGO"
  Goal 2: Verificar uma vaga ideal
    OP: Na nova página, percorrer pelo arquivo.
```





## Historico de revisão

|    Data    | Versão |              Descrição               |                   Autor(es)                   | Data de revisão |                  Revisor(es)                  |
| :--------: | :----: | :---------------------------------:  | :-------------------------------------------: | :-------------: | :-------------------------------------------: |
| 06/05/2024 | `1.0`  |        Criação do documento          |  [Cainã Freitas](https://github.com/freitasc) |  07/05/2024     | [Lucas Meireles](https://github.com/Katuner)  |
| 06/05/2024 | `1.1`  |        Adição de Análise de Tarefas  |  [Joyce Dionizio](https://github.com/joycejdm)|      |  |
| 06/05/2024 | `1.2`  |        Adição de Análise de Tarefas 3|  [Augusto Duarte](https://github.com/Augcamp) |      |  |
| 06/05/2024 | `1.3`  |        Adição de Análise de Tarefas 4|  [Lucas Meireles](https://github.com/Katuner) |      |  |