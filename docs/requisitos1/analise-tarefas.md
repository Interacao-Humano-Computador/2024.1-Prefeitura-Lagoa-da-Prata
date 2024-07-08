# Análise de Tarefas

## Introdução

Segundo Bruno Silva e Simone Barbosa [1], uma análise de tarefas é utilizada para se ter um entendimento sobre qual é o trabalho dos usuários, como eles o realizam e por quê. Nesse tipo de análise, o trabalho é definido em termos dos objetivos que os usuários querem ou precisam atingir.

No contexto da análise de tarefas, uma abordagem valiosa é a identificação da situação atual, seja ela suportada ou não por um sistema computacional. Essa análise pode ser empregada tanto para o (re)design de sistemas quanto para avaliar os resultados de intervenções que incluam a introdução de novos sistemas computacionais. Um dos passos iniciais cruciais nesse processo é a coleta dos objetivos das pessoas ao interagirem com o sistema em análise.

O site da [Prefeitura da Lagoa da Prata](https://www.lagoadaprata.mg.gov.br/) é majoritariamente informativo, disponibilizando de uma gama de informações. O usuário pode acessar informações como: Fila de espera de creches munipais; lista de medicamentos disponíveis; calendário de eventos relacionados ao municipio; entre outros tipos de informação.

## Metodologia

A metodologia para o desenvolvimento das análises de tarefas foi estabelecida com o objetivo de explorar diversas técnicas, selecionando aquela mais adequada para cada tarefa em questão. As técnicas escolhidas foram a AHT (Análise Hierárquica de Tarefas) [2] e o CMN-GOMS (Card, Moran e Newell GOMS) [3]. Essa análise é fundamental para identificar o fluxo de passos das tarefas, permitindo a identificação de áreas que necessitam de melhorias.

Para este projeto, serão utilizadas ambas as técnicas mencionadas anteriormente, realizando uma ligação direta com os [Cénarios](cenarios.md) estabelecidos e utilizando tarefas que podem ser associadas às personas declaradas. A forma da AHT será utilizada principalmente em tarefas complexas que não são repetitivas e podem assumir diversas dependências. Já o CMN-GOMS será utilizado como base geral para os cenários e análise das etapas para se alcançar o objetivo primário.

## HTA - Análise Hierárquica de Tarefas

Desenvolvida na década de 1960, a Análise Hierárquica de Tarefas (HTA) é uma ferramenta empregada para compreender as competências e habilidades necessárias para realizar tarefas complexas e não repetitivas. Além disso, é valiosa para identificar problemas de desempenho. A HTA facilita a compreensão das relações entre as ações das pessoas, os motivos que as impulsionam e as consequências caso essas ações não sejam executadas corretamente.

A Tabela 1 abaixo apresenta os elementos de uma análise hierárquica de tarefas.

<center>

**Tabela 1** - Elementos de uma HTA

| Elemento     | Descrição                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tarefa:      | Uma parte do trabalho que requer realização, frequentemente definida em termos de objetivos e subobjetivos.                                                                          |
| Objetivo:    | Um estado específico, um estado final, determinado por eventos ou por valores observáveis de variáveis, que servem como critério para alcançar o objetivo.                           |
| Subobjetivo: | Uma subdivisão de objetivos complexos, usada para identificar quais subobjetivos são mais difíceis de alcançar, já que limitam ou até mesmo impedem o alcance do objetivo principal. |
| Plano:       | Define os subobjetivos necessários para alcançar um objetivo maior e a ordem em que esses subobjetivos devem ser alcançados.                                                         |
| Operação:    | As circunstâncias em que o objetivo é ativado (entrada), as atividades ou ações que contribuem para alcançá-lo e as condições que indicam o seu alcance (feedback).                  |

 *Fonte: [FREITAS, Cainã](https://github.com/freitasc). 2024.*

</center>


Os planos podem possuir relações entre os subobjetivos, como: sequência fixa (um objetivo deve ser atingido antes do próximo); regra de seleção ou decisão (quais objetivos que deverão ser atin-gidos dependem das circunstâncias); ou em paralelo (mais de um objetivo deve ser atingido ao mesmo tempo). A Figura 1 apresenta a forma gráfica de representação dessas relações.

<center>

**Figura 1** - Elementos de um diagrama HTA
<img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/elementosHTA.png" width="100%">

 *Fonte: [FREITAS, Cainã](https://github.com/freitasc). 2024.*

</center>






### Análise da Tarefa HTA 1: Cadastrar e acompanhar uma reclamação na ouvidoria - Cainã
Abaixo se encontra a tabela 2 e figura 2 referentes a tarefa de Cadastrar e acompanhar uma reclamação na ouvidoria, ambas feitas pelo integrante do grupo [Cainã Freitas](https://github.com/freitasc):

<center>

**Tabela 2** - HTA da Tarefa: Cadastrar e uma reclamação na ouvidoria

| Objetivos / Operações                              | Relações | Problemas / Recomendações                                                                                                                                                                                                                                                              |
| -------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0. Cadastrar e consultar uma reclamação cadastrada** | 1 > 2    | **Input:** Acesso ao site de Lagoa da Prata, Credenciais de login (usuário e senha). <br> **Plano:** Realizar login no site, Navegar até a Ouvidoria, Cadastrar reclamação desejada, Acessar a reclamação na lista, Acompanhar status. <br> **Feedback:** Status da reclamação cadastrada emitido. |
| **1. Acessar a página de cadastrar manifestação na ouvidoria**                       | 1 / 2    | **Plano:** Navegar até o menu de transparência, escolher a opção "Ouvidoria" e acessar a página de cadastrar manifestação <br>**Feedback:** Tela da ouvidoria que mostra opção de cadastrar manifestação                                                       |
| 1.1 Acessar o menu de transparência ao clicar em "Serviços para a Transparência"                  |          |                                                                                                                                                                                                                                                                                        |
| 1.2 Selecionar o cadastro de manifestação                  |          |                                                                                                                                                                                                                                                                                        |
| **2. Cadastrar Reclamação**                            | 1 > 2    | **Plano:** Cadastrar uma reclamação através do formulário  <br>**Feedback:** Caixa de aviso avisando que a reclamação foi cadastrada                                                                                                                                                           |
| 2.1. Selecionar tipo, secretaria e assunto         |          |                                                                                                                                                                                                                                                                                        |
| 2.2. Preencher texto de reclamação                 |          |                                                                                                                                                                                                                                                                                        |
| 2.3. Preencher campos opcionais                    | 1 / 2    | **Plano:** Cadastrar (ou não) campos adicionais do formulário  <br>**Feedback:** Campo adicional presente na pagina de acompanhamento                                                                                                                                                          |
| *2.3.1 Preencher endereço*                           |          |                                                                                                                                                                                                                                                                                        |
| *2.3.2 Solicitar Sigilo*                             |          |                                                                                                                                                                                                                                                                                        |
| 2.4. Resolver Captcha                              |          |                                                                                                                                                                                                                                                                                        |
| **3. Fazer login**                                                                                         | 1 / 2    | **plano:** Login pelo GOV.BR informar CPF e senha ou login pela Prefeitura Munincipal de Lagoa da Prata informar cpf/cnpj/email e senha <br> **Feedback:**: mensagem com status de usuário logado                                                                                                                                                                                                   |
| 3.1 Fazer login pela Prefeitura Munincipal de Lagoa da Prata                                               | 1 / 2    | **plano:** Realizar cadastro informando: email, senha, nome completo, CPF, confirmar a declaração da veracidade dos dados; ou realizar login informando CPF ou email e senha                                                                                                                                                                                                                                                                                                                                       |
| *3.1.1 Fazer login pelo Prefeitura Munincipal de Lagoa da Prata com cadastro feito anteriormente*          |          |                                                                                                                                                                                                                                                                                                                                         |
| *3.1.2 Fazer cadastro pela Prefeitura Munincipal de Lagoa da Pratacaso não possuir conta e realizar login* |          |                                                                                                                                                                                                                                                                                                                                         |
| 3.2 Fazer login pelo GOV.BR                                                                                | 1 / 2    |  **plano:** Realizar cadastro informando CPF, realizando HCaptcha, escolher um banco para realizar login; ou Realizar login informando CPF e senha.                                                                                                                                                                                                                                                                                                                                       |
| *3.2.1 Fazer cadastro no GOV.BR caso não possuir conta e realizar login*                                   |          |                                                                                                                                                                                                                                                                                                                                         |
| *3.2.2 Fazer login pelo GOV.BR com cadastro feito anteriormente*                                           |          |                                                                                                                                                                                                                                                                                                                                         |
| 4. Consultar status da reclamação                  | 1 > 2    | Plano: Acompanhar status da reclamação recem registrada  <br>Feedback: Campo de status presente na pagina de acompanhamento                                                                                                                                                            |
| 4.1. Selecionar "meus protocolos"                  |          |                                                                                                                                                                                                                                                                                        |
| 4.2. Selecionar reclamação cadastrada              |          |                                                                                                                                                                                                                                                                                        |
| 4.3. Conferir status                               |          |                                                                                                                                                                                                                                                                                        |

 *Fonte: [FREITAS, Cainã](https://github.com/freitasc). 2024.*


**Figura 2** - Diagrama HTA da Tarefa: Cadastrar e acompanhar uma reclamação na ouvidoria
<img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA_ouvidoria.png" width="100%">

w*Fonte: [FREITAS, Cainã](https://github.com/freitasc). 2024.*

</center>


### Análise da Tarefa HTA 2: Cadastro Antecipado de Aluno - Joyce

Abaixo se encontra a tabela 3 e figura 3 referentes a tarefa de Cadastro Antecipado de Aluno, ambas feitas pelo integrante do grupo [Joyce Dionizio](https://github.com/joycejdm):

<center>

**Tabela 3** - HTA da Tarefa: Cadastro Antecipado de Aluno

### Tabela 3 - HTA da Tarefa: Cadastro Antecipado de Aluno

| Objetivos / Operações                                | Relações      | Problemas / Recomendações                                                                                                      |
|------------------------------------------------------|---------------|----------------------------------------------------------|
| 0. Realizar cadastro antecipado de aluno para matrícula escolar | 1 > 2 | Input: Acesso ao site da Prefeitura de Lagoa da Prata, Dados do aluno, Dados do responsável, Dados sócio-econômicos. <br> Plano: Navegar até a seção de serviços do cidadão, selecionar "Cadastro Antecipado de Aluno", preencher dados do aluno, preencher dados do responsável, preencher dados sócio-econômicos, gravar dados, confirmar gravação. <br> Feedback: Confirmação de cadastro bem-sucedido. |
| 1. Acessar o site da prefeitura de Lagoa da Prata   | 1 > 2 | Plano: Abrir o navegador e acessar o site da prefeitura. <br> Feedback: Site da prefeitura carregado. |
| 1.1 Abrir o navegador e acessar o site da Prefeitura de Lagoa da Prata |  | Recomenda-se usar um navegador compatível com o site e garantir uma conexão estável com a internet. |
| 2. Navegar para a seção de "Serviços do Cidadão" e selecionar "Cadastro Antecipado de Aluno" |1 > 2 | Plano: Encontrar e clicar na opção "Cadastro Antecipado de Aluno" no menu "Serviços do Cidadão". <br> Feedback: Página de Cadastro Antecipado de Aluno aberta. |
| 2.1 Encontrar o menu "Serviços do Cidadão" |  | O menu "Serviços do Cidadão" deve ser claramente identificado. |
| 2.2 Clicar na opção "Cadastro Antecipado de Aluno" |  | A opção deve ser funcional e redirecionar corretamente. |
| 3. Preencher formulário com dados do aluno | 1 > 2 | Plano: Inserir os dados obrigatórios no formulário do aluno. <br> Feedback: Formulário do aluno preenchido corretamente. |
| 3.1 Inserir dados obrigatórios no formulário do aluno |  | Campos devem ser claros e permitir a inserção de informações sem erros. |
| 3.2 Conferir os dados inseridos |  | Verificação dos dados antes de prosseguir. |
| 4. Preencher formulário com dados do responsável | 1 > 2 | Plano: Inserir os dados obrigatórios no formulário do responsável. <br> Feedback: Formulário do responsável preenchido corretamente. |
| 4.1 Inserir dados obrigatórios no formulário do responsável |  | Campos devem ser claros e permitir a inserção de informações sem erros. |
| 4.2 Conferir os dados inseridos |  | Verificação dos dados antes de prosseguir. |
| 5. Preencher formulário com dados sócio-econômicos | 1 > 2 | Plano: Inserir os dados obrigatórios no formulário sócio-econômico. <br> Feedback: Formulário sócio-econômico preenchido corretamente. |
| 5.1 Inserir dados obrigatórios no formulário sócio-econômico |  | Campos devem ser claros e permitir a inserção de informações sem erros. |
| 5.2 Conferir os dados inseridos |  | Verificação dos dados antes de prosseguir. |
| 6. Gravar os dados do cadastro e confirmar gravação | 1 + 2 | Plano: Verificar todas as informações, clicar em "Finalizar Cadastro" e confirmar. <br> Feedback: Dados salvos no sistema e confirmação exibida. |
| 6.1 Verificar todas as informações inseridas |  | Revisão de dados para evitar erros. |
| 6.2 Clicar no botão "Finalizar Cadastro" e confirmar |  | Botão deve ser claramente identificável e funcional. |

*Fonte: [DIONIZIO, Joyce](https://github.com/joycejdm). 2024.*


**Figura 3** - Diagrama HTA da Tarefa: Cadastro Antecipado de Aluno
<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/hta_matricula.jpg" width="100%">
*Fonte: [DIONIZIO, Joyce](https://github.com/joycejdm). 2024.*
</center>

### Análise da Tarefa HTA 3: Acessar o módulo de Contra Cheque e consultar processos do servidor  - Augusto
Abaixo se encontra a tabela 4 e figura 4 referentes a tarefa de Acessar o módulo de Contra Cheque e consultar processos do servidor , ambas feitas pelo integrante do grupo [Augusto Duarte](https://github.com/Augcamp):

<center>

**Tabela 4** - HTA da Tarefa: Acessar o módulo de Contra Cheque e consultar processos do servidor

|    Objetivos/Operações    |    Relações    |    Problemas e recomendações    |
| :-----------------------: | ------------------------------- | ------------------------------- | 
| 0. Acessar o módulo de Contra Cheque e consultar processos do servidor  |  | **input:** Localização e acesso ao modulo. | 
| 1. Selecionar a opção "Contra Cheque" | 1>2 | **input:** Escolha da opção para iniciar o processo de consulta. |
| 2. Preencher os campos requeridos de login | 2>3 |  **input:** Inserção de dados pessoais. |
| 3. Selecionar a opção "Processo Digital" |3>4 |  **input:** Escolha da opção para iniciar o acompanhamento dos processos. |
| 4. Escolher o processo  |4>5 |  **input:** Seleção do processo desejado. |
| 5. Acompanhar o status do processo | | **feedback:** Informação sobre o processo e resultados. |
 
*Fonte: [DUARTE, Augusto](https://github.com/Augcamp). 2024.*


**Figura 4** - Diagrama HTA da Tarefa: Acessar o módulo de Contra Cheque e consultar processos do servidor
<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA2.png" width="100%">

*Fonte: [DUARTE, Augusto](https://github.com/Augcamp). 2024.*

</center>

### Análise da Tarefa HTA 4: Registrar e verificar o panorama de saúde da cidade - Lucas Heler
Abaixo se encontra a tabela 5 e figura 5 referentes a tarefa de Registrar e verificar o panorama de saúde da cidade, ambas feitas pelo integrante do grupo [Lucas Meireles](https://github.com/Katuner):

<center>
**Tabela 5** - HTA da Tarefa: Registrar e verificar o panorama de saúde da cidade


| Objetivos / Operações                                          | Relações | Problemas / Recomendações                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. Registrar e verificar o panorama de saúde da cidade         | 1 > 2    | Input: Acesso ao site de Lagoa da Prata, Credenciais de login (usuário e senha). <br> Plano: Realizar login no site, Navegar para a página de estado de saúde, Registrar estado de saúde, Verificar panorama de saúde da cidade. <br> Feedback: Status do estado de saúde emitido. |
| 1. Realizar login no site                                      | 1 > 2    | Plano: informar o cpf e depois a senha do gov.br.                                                                                                                                                                                                                                  |
| 1.1 Informar CPF                                               |          |                                                                                                                                                                                                                                                                                    |
| 1.2 Informar senha do gov.br                                   |          |                                                                                                                                                                                                                                                                                    |
| 2. Navegar para a página de estado de saúde                    | 1 / 2    | Plano: selecionar uma das opções, entre ir até pagina através do menu hamburguer e ir até a pagina pela aba de pesquisa                                                                                                                                                            |
| 2.1 Ir através do menu hamburguer                              |          |                                                                                                                                                                                                                                                                                    |
| 2.2 Ir através da aba de pesquisa                              |          |                                                                                                                                                                                                                                                                                    |
| 3. Registrar estado de saúde                                   | 1 > 2    | Plano: Selecionar se está bem ou não, em caso negativo, realizar os registros                                                                                                                                                                                                      |
| 3.1. Registrar que não se sente mal                            |          |                                                                                                                                                                                                                                                                                    |
| 3.2. Registrar que se sente mal                                | 1 > 2    | Plano: registrar os dados de sintomas e locais                                                                                                                                                                                                                                     |
| 3.2.1 Confirmar endereço                                       |          |                                                                                                                                                                                                                                                                                    |
| 3.2.2 Registrar os sintomas                                    |          |                                                                                                                                                                                                                                                                                    |
| 3.2.3 Registrar se deseja marcar uma consulta                  | 1 / 2    |                                                                                                                                                                                                                                                                                    |
| 3.2.3.1 Não marcar consulta                                    |          |                                                                                                                                                                                                                                                                                    |
| 3.2.3.2 Marcar consulta                                        | 1 > 2    |                                                                                                                                                                                                                                                                                    |
| 3.2.3.2.1 Selecionar horário da consulta                       |          |                                                                                                                                                                                                                                                                                    |
| 3.2.4 Registrar locais que esteve presente                     |          |                                                                                                                                                                                                                                                                                    |
| 4. Verificar panorama de saúde da cidade                       |          |                                                                                                                                                                                                                                                                                    |
| 4.1. Navegar pelo mapa interativo                              | 1 / 2    |                                                                                                                                                                                                                                                                                    |
| 4.1.1 Visualizar as informações resumidas pelo mapa            |          |                                                                                                                                                                                                                                                                                    |
| 4.1.2 Selecionar uma área do mapa e verificar dados detalhados |          |                                                                                                                                                                                                                                                                                    |

*Fonte: [MEIRELES, Lucas](https://github.com/Katuner). 2024.*

**Figura 5** - Diagrama HTA da Tarefa: Registrar e verificar o panorama de saúde da cidade

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA_Saude.png" width="100%">
*Fonte: [MEIRELES, Lucas](https://github.com/Katuner). 2024.*

</center>

### Análise da Tarefa HTA 5: Solicitar vistoria de local com água parada
Abaixo se encontra tanto a tabela 6 e imagem 6 representando o diagrama HTA relacionado a tarefa Solicitar vistoria de local com água parada, ambos foram elaborados levando em consideração a [persona Maria Arlete](/requisitos1/personas/#maria-arlete) e o [cenario C03](/requisitos1/cenarios/#c03-solicitar-vistoria-de-local-com-agua-parada).
<center>
**Tabela 6** - HTA da Tarefa: Solicitar vistoria de local com água parada

| Objetivos / Operações                                                                                      | Relações | Problemas / Recomendações                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0. Solicitar vistoria de local com água parada**                                                         | 1 > 2    | **input:** formulário de solicitação de vistoria <br> **plano:** acessar a página; ler as informações de uma solicitação; escolher forma de login; enviar a solicitação; baixar a solicitação <br> **feedback:** Nova solicitação aparece aparece para a Secretária de Saúde na lista de solicitações de vistoria de água parada como pendente <br> **recomendação:** status da vistoria ser disponbilizada para pessoa que realizou login e em uma pagina mostrando todas as vistorias realizadas.                                                                                                                                                                                                                                                                                                                                      |
| **1. Acessar a página de Solicitar vistoria de local com água parada**                                     | 1 / 2    | **ação:** Acessar o menu "hamburguer" ou acessar o menu "serviços para o Cidadão" ou pesquisar na aba de pesquisas                                                                                                                                                                                                                                                                                                                                      |
| 1.1 Encontrar pelo menu "hamburguer" na aba Serviços                                                       | 1 / 2    | **ação:** Passar o dispositivo apontador por cima do botão para abrir o menu suspenso; ou Clicar no botão para ele abrir                                                                                                                                                                                                                                                                                                                                         |
| 1.1.1 Acessar o menu passando o dispositivo apontador em cima                                              |          |                                                                                                                                                                                                                                                                                                                                         |
| 1.1.2 Acessar o menu clicando no botão "hamburguer"                                                        |          |                                                                                                                                                                                                                                                                                                                                         |
| 1.2 Encontrar na página inicial ao clicar em "Serviços para o Cidadão"                                     |          |                                                                                                                                                                                                                                                                                                                                         |
| 1.3 Encontrar pela aba de pesquisa                                                                         |          |                                                                                                                                                                                                                                                                                                                                         |
| **2. Fazer leitura das informações da solicitação**                                                        |          |                                                                                                                                                                                                                                                                                                                                         |
| **3. Fazer login**                                                                                         | 1 / 2    | **plano:** Login pelo GOV.BR informar CPF e senha ou login pela Prefeitura Munincipal de Lagoa da Prata informar cpf/cnpj/email e senha                                                                                                                                                                                                   |
| 3.1 Fazer login pela Prefeitura Munincipal de Lagoa da Prata                                               | 1 / 2    | **plano:** Realizar cadastro informando: email, senha, nome completo, CPF, confirmar a declaração da veracidade dos dados; ou realizar login informando CPF ou email e senha                                                                                                                                                                                                                                                                                                                                       |
| *3.1.1 Fazer login pelo Prefeitura Munincipal de Lagoa da Prata com cadastro feito anteriormente*          |          |                                                                                                                                                                                                                                                                                                                                         |
| *3.1.2 Fazer cadastro pela Prefeitura Munincipal de Lagoa da Pratacaso não possuir conta e realizar login* |          |                                                                                                                                                                                                                                                                                                                                         |
| 3.2 Fazer login pelo GOV.BR                                                                                | 1 / 2    |  **plano:** Realizar cadastro informando CPF, realizando HCaptcha, escolher um banco para realizar login; ou Realizar login informando CPF e senha.                                                                                                                                                                                                                                                                                                                                       |
| *3.2.1 Fazer cadastro no GOV.BR caso não possuir conta e realizar login*                                   |          |                                                                                                                                                                                                                                                                                                                                         |
| *3.2.2 Fazer login pelo GOV.BR com cadastro feito anteriormente*                                           |          |                                                                                                                                                                                                                                                                                                                                         |
| 3.3 Solicitar anonimamente                                                                                 |          |                                                                                                                                                                                                                                                                                                                                         |
| **4. Enviar Solicitação de vistoria de local com água parada**                                             | 1 > 2    | **input:** Preencher os campos: logradouro, número, complemento, CEP, descrição; Selecionar qual tipo de ímovel: residencial, abandonado, desocupado, público, terreno baldio murado, terreo baldio não murado, ferro velho, borracharia, desmanche, recicladoras, cemitérios, obras, parques ou praças, outros; Clicar no botão enviar |
| 4.1. Preencher o formulário nos campos com informações                                                     |          |                                                                                                                                                                                                                                                                                                                                         |
| 4.2. Responder o reCaptcha                                                                                 |          |                                                                                                                                                                                                                                                                                                                                         |
| 4.3 Clicar no botão Enviar                                                                                 |          |                                                                                                                                                                                                                                                                                                                                         |
| **5. Baixar os dados da solicitação**                                                                      | 1 / 2    | **plano:** Visualizar a solicitação, logo depois baixar a solicitação                                                                                                                                                                                                                                                                   |
| 5.1 Visualizar a confirmação da solicitação                                                                |          |                                                                                                                                                                                                                                                                                                                                         |
| 5.2 Clicar no botão para baixar a solicitação                                                              |          |                                                                                                                                                                                                                                                                                                                                         |

*Fonte: [DOURAOD, Pedro Lucas](https://github.com/lucasdray). 2024.*


**Figura 6** - Diagrama HTA da Tarefa: Solicitar vistoria de local com água parada
<img   src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA_solicitacao.png" >
*Fonte: [DOURAOD, Pedro Lucas](https://github.com/lucasdray). 2024.*
</center>

## CNM-GOMS

O GOMS (Goals, Operators, Methods, and Selection Rules - Objetivos, Operadores, Métodos e Regras de Seleção) é um conjunto de modelos utilizados para análise de tarefas [1]. O CMN-GOMS (Card, Moran e Newell GOMS) é um desses modelos e consiste em uma hierarquia bem definida de objetivos representados em forma de programa, permitindo assim uma análise executável. (Barbosa e Silva, 2010) [1]

### Motivo da escolha
Com base na fala do entrevistado encontrada na [entrevista](entrevista.md) com relação a utilizar apenas serviços específicos do site da Prefeitura, foi decidido utilizar o CNM-GOMS pois, essa análise se aplica principalmente a situações em que os usuários realizam tarefas que já dominam [1].
Além disso como a maioria das tárefas análisadas são propostas de implementações para o site com esse método de análise podemos identificar pontos específicos em que os usuários podem se confundir ou cometer erros, erros esses que podem passar despercebidos na criação de uma funcionalidade nova para o site.

### Legenda
Abaixo segue a tabela 07 que contém a legenda do seignificado de GOMS, contendo o termo, tradução e descrição de cada todos sendo retirados do livro Interação Humano Computador de Bruno Silva e Simone Barbosa [1]:

<center>

**Tabela 07** - Legenda GOMS

| Termo    | Tradução         | Descrição                                                             |
| -------- | ---------------- | --------------------------------------------------------------------- |
| Goal     | Objetivo         | O que o usuário quer realizar utilizando o sistema                    |
| OP       | Operador         | Ações concretas que o site permite que o usuário faça                 |
| METHOD   | Método           | Sequência de subobjetivos e operadores para atingir um objetivo maior |
| SEL.RULE | Regra de seleção | Tomada de decisão sobre qual método utilizar                          |

*Fonte: [DOURADO, Pedro Lucas](https://github.com/lucasdray)

</center>

Abaixo estão listadas as análises de tarefas utilizando CNM-GOMS e o autor da análise:

### Análise da Tarefa CNM-GOMS 1: Cadastro Antecipado de Aluno - (Fonte: DIONIZIO, Joyce. 2024).

```
Goal 0: Realizar cadastro antecipado de aluno para matrícula escolar
  Goal 1: Acessar o site da Prefeitura de Lagoa da Prata
    METHOD 1.A: Acessar o site diretamente
    (SEL.RULE: preferência do usuário)
        OP: Abrir o navegador
        OP: Digitar o URL do site da Prefeitura de Lagoa da Prata
        OP: Pressionar Enter
  Goal 2: Navegar para a seção de "Serviços do Cidadão" e selecionar "Cadastro Antecipado de Aluno"
    METHOD 2.A: Navegar através do menu
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até menu "Serviços do Cidadão"
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até a opção "Cadastro Antecipado de Aluno"
        OP: Clicar com o botão esquerdo do mouse
  Goal 3: Preencher formulário com dados do aluno
    METHOD 3.A: Inserir dados obrigatórios no formulário do aluno
        OP: Digitar nome do aluno
        OP: Digitar data de nascimento do aluno
        OP: Digitar endereço do aluno
        OP: Digitar outros dados obrigatórios
  Goal 4: Preencher formulário com dados do responsável
    METHOD 4.A: Inserir dados obrigatórios no formulário do responsável
        OP: Digitar nome do responsável
        OP: Digitar CPF do responsável
        OP: Digitar endereço do responsável
        OP: Digitar outros dados obrigatórios
  Goal 5: Preencher formulário com dados sócio-econômicos
    METHOD 5.A: Inserir dados obrigatórios no formulário sócio-econômico
        OP: Digitar renda familiar
        OP: Digitar outros dados sócio-econômicos
  Goal 6: Gravar os dados do cadastro
    METHOD 6.A: Salvar os dados inseridos
        OP: Verificar todas as informações inseridas
        OP: Clicar no botão "Finalizar Cadastro"
  Goal 7: Confirmar gravação dos dados
    METHOD 7.A: Confirmar a finalização do cadastro
        OP: Verificar balão de confirmação
        OP: Clicar em "Voltar para a Página Inicial" no balão de confirmação
```


### Análise da Tarefa CNM-GOMS 2: Registrar e verificar o panorama de saúde da cidade - (Fonte: MEIRELES, Lucas. 2024).
```
Goal 0: Registrar e verificar o panorama de saúde da cidade
  Goal 1: Encontrar Registro de Estado de Saúde
    METHOD 1.A: Encontrar através do menu "hamburguer"
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até menu "hamburguer"
        OP: Levar cursor até botão "Registro de Estado de Saúde"
        OP: Clicar com o botão esquerdo do mouse
    METHOD 1.B: Encontrar através da aba de pesquisa
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "Saúde"
        OP: Levar cursor até botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até "Registro de Estado de Saúde"
        OP: Clicar com o botão esquerdo do mouse
    
    Goal 2: Registrar Estado de Saúde:
      OP: Levar cursor até botão "Registrar estado de saúde"
        METHOD 2.A: Usuário não possui sintomas de doença
        (SEL.RULE: estado de saúde atual do usuário)
      OP: Levar cursor até caixa "Me sinto bem"
      OP: Clicar com o botão esquerdo do mouse
      OP: Verificar o endereço do morador
      OP: Levar cursor até o botão "Endereço correto"
      OP: Clicar com o botão esquerdo do mouse
        METHOD 2.B: Usuário possui sintomas de doença
        (SEL.RULE: estado de saúde atual do usuário)
      OP: Levar cursor até caixa "Não me sinto bem"
      OP: Clicar com o botão esquerdo do mouse
      OP: Verificar o endereço do morador
      OP: Levar cursor até o botão "Endereço correto"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar o cursor até a caixa seletora de sintomas
      OP: Clicar com o botão esquerdo nas caixas de sintomas que condizem com o que o usuário sente
      OP: Levar o cursor até a caixa de seleção de "Desejo marcar uma consulta"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar o cursor até o mapa da cidade encontrado na área "Locais que estive recentemente"
      OP: Levar o cursor até as áreas que foram frequentadas pelo usuário nos últimos dias
      OP: Clicar com o botão esquerdo do mouse em cada área que o usuário esteve
      OP: Levar cursor até a caixa "Prosseguir"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar o cursor até a tabela de horários
      OP: Clicar com o botão esquerdo do mouse nos horários disponíveis para o usuário
      OP: Levar o cursor até a caixa "Prosseguir"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar cursor até caixa "OK"
      OP: Clicar com o botão esquerdo do mouse

    Goal 3: Verificar o panorama de saúde da cidade
      OP: Levar o cursor até o mapa interativo no centro da página
      OP: Clicar e arrastar com o botão esquerdo do mouse para movimentar o mapa
      OP: Posicionar o cursor sobre o círculo no mapa interativo
      OP: Realizar a leitura dos sintomas frequentes na área do círculo
      OP: Clicar com o botão esquerdo do mouse no círculo
      OP: Realizar a leitura dos dados de números de pessoas que registraram cada tipo de sintoma
    
    
```


### Análise da Tarefa CNM-GOMS 3: Cadastrar e acompanhar status de uma reclamação na ouvidoria - (Fonte: FREITAS, Cainã. 2024).
```
Goal 0: Cadastrar e acompanhar status de uma reclamação
  Goal 1: Encontrar cadastro de reclamação na Ouvidoria
      OP: Levar cursor até botão "Serviços para a Transparência"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar cursor até botão "Ouvidoria"
      OP: Clicar com o botão esquerdo do mouse
      OP: Levar cursor até botão "Cadastre sua Manifestação"
      OP: Clicar com o botão esquerdo do mouse

  Goal 2: Cadastrar Reclamação na ouvioria:
    METHOD 2.A: Preencher formulario de cadastro de reclamação
      OP: Levar cursor até botão "Cadastrar Manifestação"
      OP: Clicar com o botão esquerdo do mouse
      OP: Ele navega até o formulário de "Solicitação"
      OP: Levar cursor até caixa "Tipo"
      OP: Clicar com o botão esquerdo do mouse
      OP: Clicar com o botão esquerdo do mouse em "Reclamação"
      OP: Levar cursor até caixa "Secretaria/Departamento"
      OP: Clicar com o botão esquerdo do mouse
      OP: Clicar com o botão esquerdo do mouse em "Conselho Municipal de Educação"
      OP: Levar cursor até caixa "Assunto"
      OP: Clicar com o botão esquerdo do mouse
      OP: Clicar com o botão esquerdo do mouse em "OUVIDORIA GERAL - RECLAMAÇÃO"
      OP: Levar cursor até caixa "Forma de Resposta"
      OP: Clicar com o botão esquerdo do mouse
      OP: Clicar com o botão esquerdo do mouse em "Consulta no Site"
      OP: Levar cursor até caixa "Solicitação"
      OP: Clicar com o botão esquerdo do mouse
      OP: Escrever toda a reclamação necessária para relatar o ocorrido

    METHOD 2.B: Preencher cambos opcionais com local do ocorrido
    (SEL.RULE: campos opcionais para o usuário)
      OP: Levar cursor até caixa "Anexar Arquivos"
      OP: Clicar com o botão esquerdo do mouse
      OP: Escolhe um arquivo para ser anexado
      OP: Navegar até a aba de "Local da Ocorrência"
      OP: Levar cursor até caixa "Bairro"
      OP: Clicar com o botão esquerdo do mouse
      OP: Clicar com botão esquerdo do mouse no bairro da escola
      OP: Levar cursor até caixa "Logradouro"
      OP: Clicar com o botão esquerdo do mouse
      OP: Escrever o Logradouro da escola
      OP: Levar cursor até caixa "Número"
      OP: Clicar com o botão esquerdo do mouse
      OP: Escrever o Número da escola

    METHOD 2.C: Enviar Reclamação
      OP: Levar cursor até caixa de captcha
      OP: Clicar com o botão esquerdo do mouse
      OP: Resolver captcha simples
      OP: Levar cursor até botão "Cadastrar"
      OP: Clicar com o botão esquerdo do mouse
    
  Goal 3: Fazer login
    Method 3.A: Fazer login pela Prefeitura Munincipal de Lagoa da Prata
    (SEL. RULE: usuário tem preferencia por usar esse login e/ou já possui conta )
      Method 3.A.A: Fazer login pelo Prefeitura Munincipal de Lagoa da Prata com cadastro feito anteriormente
      (SEL. RULE: usuário já possui conta )
        Method 3.A.A.A: Fazer login em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.A.A.1: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.3: desloca o cursor até o aba "CPF/CNPJ/email"
          OP. 3.A.A.A.4: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.5: preenche o campo usuário com CPF ou email
          OP. 3.A.A.A.6: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.7: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.8: preenche o campo senha
          OP. 3.A.A.A.9: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.10: desloca o cursor até o botão "Entrar"
          OP. 3.A.A.A.10: clica com o botão esquerdo do dispositivo apontador

        Method 3.A.A.B: Fazer login em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: clicar no botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica na aba "CPF/CNPJ/email"
          OP. 3.A.A.A.3: preenche o campo usuário com CPF ou email
          OP. 3.A.A.B.4: clicar na aba "Senha"
          OP. 3.A.A.A.5: preenche o campo usuário com senha
          OP. 3.A.A.B.6: clicar no botão "Entrar"

      Method 3.A.B: Fazer cadastro pela Prefeitura Munincipal de Lagoa da Pratacaso não possuir conta e realizar login
      (SEL. RULE: usuário não possui conta )
        Method 3.A.A.A: Fazer cadastro em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.A.A.1: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.3: desloca o cursor até a opção "Cadastrar-se"
          OP. 3.A.A.A.4: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.5: preenche os campos e realiza o cadastro no site da Prefeitura
          OP. 3.A.A.A.6: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.7: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.8: desloca o cursor até o aba "CPF/CNPJ/email"
          OP. 3.A.A.A.9: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.10: preenche o campo usuário com CPF ou email
          OP. 3.A.A.A.11: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.12: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.13: preenche o campo senha
          OP. 3.A.A.A.14: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.15: desloca o cursor até o botão "Entrar"
          OP. 3.A.A.A.16: clica com o botão esquerdo do dispositivo apontador

    Method 3.B: Fazer login pelo GOV.BR
    (SEL. RULE: usuário tem preferencia por usar esse login e/ou já possui conta )
      Method 3.B.A: Realizar login
      (SEL. RULE: usuário já possui conta )
       Method 3.A.B.A: Fazer login em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.B.A.1: desloca o cursor até o botão "Entrar com GOV.BR"
          OP. 3.A.B.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.B.A.4: desloca o cursor até o botão "Entrar como {NOME DO USUÁRIO}"
          OP. 3.A.B.A.5: clica com o botão esquerdo do dispositivo apontador
         
        Method 3.A.A.B: Fazer login em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: desce a página até a aba de login
          OP. 3.A.B.A.2: clica no botão "Entrar com GOV.BR"
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.A.B.4: desce a página até a aba de login
          OP. 3.A.B.A.5: clica no botão "Entrar como {NOME DO USÁRIO}"
         
      Method 3.B.B: Cadastrar e realizar login
      (SEL. RULE: usuário não possui conta )
       Method 3.A.B.A: Fazer cadastro em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.B.A.1: desloca o cursor até o botão "Entrar com GOV.BR"
          OP. 3.A.B.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.B.A.3: realiza cadastro no site do GOV.BR
          OP. 3.A.B.A.4: realiza login no site do GOV.BR
          OP. 3.A.B.A.5: desloca o cursor até o botão "Entrar como {NOME DO USUÁRIO}"
          OP. 3.A.B.A.6: clica com o botão esquerdo do dispositivo apontador
         
        Method 3.A.A.B: Fazer cadastro em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: desce a página até a aba de login
          OP. 3.A.B.A.2: clica no botão "Entrar com GOV.BR"
          OP. 3.A.B.A.3: realiza cadastro no site do GOV.BR
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.A.B.4: desce a página até a aba de login
          OP. 3.A.B.A.5: clica no botão "Entrar como {NOME DO USÁRIO}"

  Goal 4: Acompanhar status de reclamação cadastrada
    OP: Levar cursor até botão "Meus Protocolos"
    OP: Levar cursor até protocolo cadastrado anteriormente
    OP: Clicar com o botão esquerdo do mouse
    OP: Navegar até status da reclamação
    OP: Acompanhar status
```
 


### Análise da Tarefa CNM-GOMS 4: Acessar o modulo de contra cheque e consultar processos do servidor (Fonte: DUARTE, Augusto. 2024).
```
Goal 0: Acessar o modulo de contra cheque e consultar processos do servidor
  Goal 1: Acessar página do Contra Cheque
    METHOD 1.A: Acessar utilizando CPF
    (SEL.RULE: preferência do usuário)
      OP: Levar cursor até o menu "Contra Cheque"
      OP: Clicar com o botão esquerdo do mouse
      OP: Inserir informações pessoas utilizando CPF
      OP: Levar o cursor até “Validar”
      OP: Clicar com o botão esquerdo do mouse
    METHOD 1.B: Acessar utilizando matrícula 
    (SEL.RULE: preferência do usuário)
      OP: Levar cursor até o menu "Contra Cheque"
      OP: Clicar com o botão esquerdo do mouse
      OP: Inserir informações pessoas utilizando matrícula
      OP: Levar o cursor até “Validar”
      OP: Clicar com o botão esquerdo do mouse
  Goal 2: Consultar processos do servidor
    OP: Levar o cursor do mouse até "Processo Digital"
    OP: Clicar com botão esquerdo do mouse
	  OP: Levar o cursor do mouse até “Nº do processo”
	  OP: Clicar com o botão esquerdo do mouse 
```

### Análise da Tarefa CNM-GOMS 5: Informar luminária queimada no Município (Fonte: HELER, Lucas. 2024).
```
Goal 0: Informar luminária queimada no Município
  Goal 1: Acessar a página sobre iluminação pública
    METHOD 1.A: Encontrar pelo MENU "hamburguer"
    (SEL.RULE: preferência do usuário)
      METHOD 1.A.1: Encontrar pelo MENU "hamburguer" sem necessidade de clicar
      (SEL.RULE: Largura da página maior que 1000px)
        OP: Mover cursor ao MENU "hamburguer"
        OP: Mover cursor a "Iluminação Pública"
        OP: Clicar com botão esquerdo
      METHOD 1.A.2: Encontrar pelo MENU "hamburguer" com necessidade de clicar
      (SEL.RULE: Largura da página igual ou menor que 1000px)
          OP: Mover cursor ao MENU "hamburguer"
          OP: Clicar com o botão esquerdo
          OP: Mover cursor ao indicador de menu suspenso de "Serviços Online"
          OP: Clicar com o botão esquerdo para abrir as opções
          OP: Morver cursor a "Iluminação Pública"
          OP: Clicar com o botão esquerdo

    METHOD 1.B: Encontrar pela aba de pesquisa
    (SEL.RULE: preferência do usuário)
      METHOD 1.B.1: Realizar a pesquisa clicando sem clicar no botão de pesquisa
      (SEL.RULE: Obrigatoriamente quando a largura da página é igual ou menor que 1000px; preferência do usuário)
        OP: Mover cursor à barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "iluminação pública"
        OP: Apertar enter no teclado
        OP: Mover cursor a opção "Serviços" em registros encontrados
        OP: Clicar com o botão esquerdo do mouse
        OP: Mover cursor ao resultado "Iluminação Pública"
        OP: Clicar com o botão esquerdo do mouse
      METHOD 1.B.2: Realizar a pesquisa clicando no botão de pesquisa
      (SEL.RULE: Disponível quando a largura da página é maior que 1000px; preferência do usuário)
        OP: Mover cursor à barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "iluminação pública"
        OP: Mover cursor ao botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Mover cursor a opção "Serviços" em registros encontrados
        OP: Clicar com o botão esquerdo do mouse
        OP: Mover cursor ao resultado "Iluminação Pública"
        OP: Clicar com o botão esquerdo do mouse

    METHOD 1.C: Encontrar pelo acesso rápido disponível na página inicial
    (SEL.RULE: preferência do usuário)
      OP: Mover cursor até "Iluminação Pública A LÂMPADA QUEIMOU?!"
      OP: Clicar com o botão esquerdo

  Goal 2: Preencher formulário "Iluminação Pública - Troca de Lâmpadas"
      OP: Mover cursor até espaços disponíveis para preenchimento escrito
      OP: Clicar com o botão esquerdo do mouse
      OP: Digitar informações requeridas
      OP: Mover cursor do mouse até opção de tipo de defeito identificado
      OP: Clicar com o botão esquerdo do mouse
      OP: Mover cursor até a "box" do reCAPTCHA
      OP: Clicar com o botão esquerdo do mouse
      OP: Mover cursor ate botão "ENVIAR"
      OP: Clicar com o botão esquerdo do mouse

  Goal 3: Ver protocolo de solicitação
      OP: Visualizar o protocolo apresentado pelo site
      OP: Mover cursor até botão "OK"
      OP: Clicar com o botão esquerdo do mouse

  Goal 4: Acompanhar protocolo de solicitação em "Acompanhe sua solicitação"
      OP: Mover cursor até espaço disponível para preenchimento escrito
      OP: Clicar com botão esquerdo do mouse
      OP: Digitar informação requerida
      OP: Mover cursor até botão "CONSULTAR"
      OP: Clicar com o botão esquerdo do mouse
      OP: Visualizar a situação e atualizações do protocolo
```

### Análise da Tarefa CNM-GOMS 6: Solicitar vistoria de água parada (Fonte: DOURADO, Pedro Lucas. 2024).
```
  Goal 0: Solicitar vistoria de água parada

  Goal 1: Acessar a página de Solicitar vistoria de local com água parada
    Method 1.A: Encontrar pelo menu "hamburguer" na aba Serviços a qualquer momento
    (SEL. RULE: usuário está em qualquer página e quer um acesso rapido a parte de serviços)
      Method 1.A.A: Acessar o menu passando o dispositivo apontador em cima
      (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador (ex: computadores (PCs e Notebooks)))
        OP. 1.A.A.1: deslocar o cursor até o menu "hamburguer"
        OP. 1.A.A.2: ao abrir o menu localizar a aba "Serviços"
        OP. 1.A.A.3: deslocar o cursor até a opção "Solicitar vistoria de local com água parada"
        OP. 1.A.A.4: clicar com o botão esquerdo do dispositvo apontador na opção "Solicitar vistoria de local com água parada"

      Method 1.A.B: Acessar o menu clicando no botão "hamburguer"
      (SEL. RULE: usuário está usando dispositivos moveis (ex: Smartphones e Tablets))
        OP. 1.A.B.1: clicar no menu "hamburguer"
        OP. 1.A.B.2: ao abrir o menu localizar a aba "Serviços"
        OP. 1.A.B.3: clicar na opção "Solicitar vistoria de local com água parada"
    
    Method 1.B: Encontrar na página inicial ao clicar em "Serviços para o Cidadão"
    (SEL. RULE: usuário está na página inicial )
      Method 1.B.A:	Acessar "serviços para o cidadão" com dispositivo apontador
      (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador (ex: computadores (PCs e Notebooks)))
        OP. 1.B.A.1: girar a roda do mouse para baixo
        OP. 1.B.A.2: deslocar o cursor até o botão "Serviços para o Cidadão"
        OP. 1.B.A.3: clicar com o botão esquerdo do dispostivo apontador
        OP. 1.B.A.4: deslocar o cursor até o opção "Solicitar vistoria de local com água parada"
        OP. 1.B.A.5: clicar com o botão esquerdo do dispostivo apontador

      Method 1.B.A:	Acessar "serviços para o cidadão" em telas touchscreen
      (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
        OP. 1.B.A.1: arrastar a tela para baixo
        OP. 1.B.A.2: clicar no botão "Serviços para o Cidadão"
        OP. 1.B.A.3: clicar na opção "Solicitar vistoria de local com água parada"


    Method 1.C: Encontrar pela aba de pesquisa
    (SEL. RULE: usuário não sabe onde localizar o serviço e deseja fazer a busca )
      Method 1.C.A:	Fazer busca com computadores (PCs e Notebooks)
      (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador e teclado ( mecânico ou virtual))
        OP. 1.C.A.1: deslocar cursor até a aba de pesquisa
        OP. 1.C.A.2: clicar com o botão esquerdo do dispositivo apontador
        OP. 1.C.A.3: usar teclado e digitar "Solicitar vistoria de local com água parada" ou algo parecido
        OP. 1.C.A.4: apertar tecla "Enter"

      Method 1.C.B:	Fazer busca em telas touchscreen
      (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
        OP. 1.C.B.1: rolar a tela para cima
        OP. 1.C.B.1: clicar na aba de pesquisa
        OP. 1.C.B.1: digitar "Solicitar vistoria de local com água parada" ou algo parecido
        OP. 1.C.B.1: clicar no botão de lupa

  Goal 2: Fazer leitura das informações da solicitação

  Goal 3: Fazer login
    Method 3.A: Fazer login pela Prefeitura Munincipal de Lagoa da Prata
    (SEL. RULE: usuário tem preferencia por usar esse login e/ou já possui conta )
      Method 3.A.A: Fazer login pelo Prefeitura Munincipal de Lagoa da Prata com cadastro feito anteriormente
      (SEL. RULE: usuário já possui conta )
        Method 3.A.A.A: Fazer login em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.A.A.1: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.3: desloca o cursor até o aba "CPF/CNPJ/email"
          OP. 3.A.A.A.4: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.5: preenche o campo usuário com CPF ou email
          OP. 3.A.A.A.6: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.7: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.8: preenche o campo senha
          OP. 3.A.A.A.9: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.10: desloca o cursor até o botão "Entrar"
          OP. 3.A.A.A.10: clica com o botão esquerdo do dispositivo apontador

        Method 3.A.A.B: Fazer login em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: clicar no botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica na aba "CPF/CNPJ/email"
          OP. 3.A.A.A.3: preenche o campo usuário com CPF ou email
          OP. 3.A.A.B.4: clicar na aba "Senha"
          OP. 3.A.A.A.5: preenche o campo usuário com senha
          OP. 3.A.A.B.6: clicar no botão "Entrar"

      Method 3.A.B: Fazer cadastro pela Prefeitura Munincipal de Lagoa da Pratacaso não possuir conta e realizar login
      (SEL. RULE: usuário não possui conta )
        Method 3.A.A.A: Fazer cadastro em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.A.A.1: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.3: desloca o cursor até a opção "Cadastrar-se"
          OP. 3.A.A.A.4: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.5: preenche os campos e realiza o cadastro no site da Prefeitura
          OP. 3.A.A.A.6: desloca o cursor até o botão "Entrar com login Munincipal"
          OP. 3.A.A.A.7: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.8: desloca o cursor até o aba "CPF/CNPJ/email"
          OP. 3.A.A.A.9: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.10: preenche o campo usuário com CPF ou email
          OP. 3.A.A.A.11: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.12: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.A.A.13: preenche o campo senha
          OP. 3.A.A.A.14: desloca o cursor até o aba "Senha"
          OP. 3.A.A.A.15: desloca o cursor até o botão "Entrar"
          OP. 3.A.A.A.16: clica com o botão esquerdo do dispositivo apontador

    Method 3.B: Fazer login pelo GOV.BR
    (SEL. RULE: usuário tem preferencia por usar esse login e/ou já possui conta )
      Method 3.B.A: Realizar login
      (SEL. RULE: usuário já possui conta )
       Method 3.A.B.A: Fazer login em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.B.A.1: desloca o cursor até o botão "Entrar com GOV.BR"
          OP. 3.A.B.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.B.A.4: desloca o cursor até o botão "Entrar como {NOME DO USUÁRIO}"
          OP. 3.A.B.A.5: clica com o botão esquerdo do dispositivo apontador
         
        Method 3.A.A.B: Fazer login em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: desce a página até a aba de login
          OP. 3.A.B.A.2: clica no botão "Entrar com GOV.BR"
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.A.B.4: desce a página até a aba de login
          OP. 3.A.B.A.5: clica no botão "Entrar como {NOME DO USÁRIO}"
         
      Method 3.B.B: Cadastrar e realizar login
      (SEL. RULE: usuário não possui conta )
       Method 3.A.B.A: Fazer cadastro em computadores (PCs e Notebooks)
        (SEL. RULE: usuário está usando aparelhos que possuem dispositivo apontador  e teclado ( mecânico ou virtual))
          OP. 3.A.B.A.1: desloca o cursor até o botão "Entrar com GOV.BR"
          OP. 3.A.B.A.2: clica com o botão esquerdo do dispositivo apontador
          OP. 3.A.B.A.3: realiza cadastro no site do GOV.BR
          OP. 3.A.B.A.4: realiza login no site do GOV.BR
          OP. 3.A.B.A.5: desloca o cursor até o botão "Entrar como {NOME DO USUÁRIO}"
          OP. 3.A.B.A.6: clica com o botão esquerdo do dispositivo apontador
         
        Method 3.A.A.B: Fazer cadastro em telas touchscreen
        (SEL. RULE: usuário está usando dispositivos com tela touchscreen (ex: Smartphones, Tablets, Notebooks) )
          OP. 3.A.A.B.1: desce a página até a aba de login
          OP. 3.A.B.A.2: clica no botão "Entrar com GOV.BR"
          OP. 3.A.B.A.3: realiza cadastro no site do GOV.BR
          OP. 3.A.B.A.3: realiza login no site do GOV.BR
          OP. 3.A.A.B.4: desce a página até a aba de login
          OP. 3.A.B.A.5: clica no botão "Entrar como {NOME DO USÁRIO}"


    Method 3.C: Solicitar anonimamente
    (SEL. RULE: usuário não quer se identificar )
    OP 3.C.1: desloca cursor até botão "Solicitar Anonimamente"
    OP 3.C.2: clica com o botão esquerdo do dispositivo apontador

  Goal 4: Enviar Solicitação de vistoria de local com água parada
    OP. 4.1: preenche o formulário nos campos solicitados
    OP. 4.2: responde o reCaptcha
    OP. 4.3: clica no botão "Enviar"

  Goal 5: Baixar os dados da solicitação
    OP. 5.1: move o cursor até o botão "Baixar dados da solicitação"
    OP. 5.2: clica com o botão esquerdo do dispositivo apontador


```
## Bibliografia
> [1] Barbosa, S. D. J.; Silva, B. S. da; Silveira, M. S.; Gasparini, I.; Darin, T.; Barbosa, G. D. J. (2021) Interação Humano-Computador e Experiência do usuário. Autopublicação.

> [2] Annett, John (2003). Hierarchical Task Analysis. In The Handbook of Task Analysis for Human-Computer Interaction, pages 67–82. Lawrence Erlbaum.

> [3] Card, Stuart K., Newell, Allen, e Moran, Thomas P. (1983). The Psychology of Human-Computer Interaction. L. Erlbaum Associates Inc., USA.


## Historico de Versões

|    Data     | Versão |                                  Descrição                                   |                   Autor(es)                   |    Data de revisão     |                                        Revisor(es)                                        |
| :---------: | :----: | :--------------------------------------------------------------------------: | :-------------------------------------------: | :--------------------: | :---------------------------------------------------------------------------------------: |
| 06/05/2024  | `1.0`  |                             Criação do documento                             | [Cainã Freitas](https://github.com/freitasc)  |       07/05/2024       |                       [Lucas Meireles](https://github.com/Katuner)                        |
| 06/05/2024  | `1.1`  |                         Adição de Análise de Tarefas                         | [Joyce Dionizio](https://github.com/joycejdm) |       07/05/2024       |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 06/05/2024  | `1.2`  |                        Adição de Análise de Tarefas 3                        | [Augusto Duarte](https://github.com/Augcamp)  |       07/05/2024       |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 06/05/2024  | `1.3`  |                        Adição de Análise de Tarefas 4                        | [Lucas Meireles](https://github.com/Katuner)  |       07/05/2024       |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 07/05/2024  | `1.4`  |                        Adição de Análise de Tarefas 5                        |  [Pedro Lucas](https://github.com/lucasdray)  |       07/05/2024       |                        [Lucas Heler](https://github.com/akaeboshi)                        |
| 07/05/2024  | `1.5`  |                      Adição de Análise de Tarefas HTA 1                      |  [Lucas Heler](https://github.com/akaeboshi)  |       07/05/2024       |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 10/05/2024  | `1.6`  |    Edição de Análise de Tarefa e correção pós entrega ponto de controle 2    | [Lucas Meireles](https://github.com/Katuner)  |       13/05/2024       |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 22/05/2024  | `1.7`  |                     Adição de Análise de Tarefas 6 e HTA                     |  [Lucas Heler](https://github.com/Akaeboshi)  |       22/05/2024       |                       [Cainã Freitas](https://github.com/freitasc)                        |
| 22/05/2024  | `1.8`  |                               Adição de tarefa                               | [Joyce Dionizio](https://github.com/joycejdm) |       22/05/2024       | [Cainã Freitas](https://github.com/freitasc), [Pedro Lucas](https://github.com/lucasdray) |
| 06/06/2024  | `2.0`  |                               Adição de HTA 6                                |  [Pedro Lucas](https://github.com/lucasdray)  |       11/06/2024       |                       [Augusto Duarte](https://github.com/Augcamp)                        |
| 07/06/2024  | `2.1`  |                              Adição CNM-GOMS 8                               |  [Pedro Lucas](https://github.com/lucasdray)  | 11/06/2024, 17/06/2024 | [Augusto Duarte](https://github.com/Augcamp), [Pedro Lucas](https://github.com/lucasdray) |
| 07/07/2024 | `3.0`  | Adição fonte GOMS e motivo de escolha, bibliografia, citações bibliograficas | [Pedro Lucas](https://github.com/lucasdray) |           07/07/2024             |              [Cainã Freitas](https://github.com/freitasc)                                                                             |
| 07/07/2024 | `3.1`  | Melhora e revisa meu HTA e Gomms, corrige uns typos no texto | [Cainã Freitas](https://github.com/freitasc) |    08/07/2024                    |  [Joyce Dionizio](https://github.com/joycejdm)                                                                                         |
| 08/07/2024 | `3.2`  | Revisao HTA e Gomms | [Joyce Dionizio](https://github.com/joycejdm) |               |                                                                                       |