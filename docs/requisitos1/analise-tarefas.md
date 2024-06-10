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


### Análise da Tarefa HTA 1: Informar luminária queimada no Município

| Objetivos / Operações                                | Relações      | Problemas / Recomendações                                                                                                      |
|------------------------------------------------------|---------------|----------------------------------------------------------|
| 0: Informar luminária queimada no Município | 1>2 | Input: Acesso a página de iluminação, preenchimento do formulário com as informações pedidas e passar pelo reCaptcha e o preenchimento do protocolo para acompanhar solicitação <br> Plano: Acessar página de iluminação pública, depois preencher o formulário de troca de lâmpadas, em seguida ver o protocolo de solicitação e por último acompanhar a solicitação <br> Feedback: Tela de acompanhamento de solicitação de iluminação pública   |
|   1: Acessar a página sobre iluminação pública  | 1>2 | Plano: Selecionar uma das opções de acesso à pagina pelo MENU "hamburguer, aba de pesquisa ou acesso rápido <br> Feedback: Tela iluminação pública |
|     1.1: Encontrar pelo MENU "hamburguer"  | 1/2 | Plano: Selecionar o MENU "hamburguer" por meio de uma das opções, clicando ou não |
|     1.1.1: Encontrar pelo MENU "hamburguer" sem necessidade de clicar | |           |
|     1.1.2: Encontrar pelo MENU "hamburguer" com necessidade de clicar | |           |
|     1.2: Encontrar pela aba de pesquisa    | 1/2| Input: Preencher aba de pesquisa, realizar a pesquisa e filtrar resultados para "serviços" <br> Plano: Realizar a pesquisa por meio de uma das opções, clicando ou não no botão de pesquisa  |
|     1.2.1: Realizar a pesquisa clicando sem clicar no botão de pesquisa   | |  |
|     1.2.2: Realizar a pesquisa clicando no botão de pesquisa   | |  |
|     1.3: Encontrar pelo acesso rápido disponível na página inicial | | Plano: Localizar na página inicial o botão |
|   2: Preencher formulário "Iluminação Pública - Troca de Lâmpadas"  | 1>2 | Plano: Preencher dados, em seguida responder o reCaptcha e finalmente clicar no botão enviar <br> Feedback: Tela de protocolo de solicitação|
|     2.1: Preencher informações requeridas |  |     |
|     2.2: Responder o reCaptcha |  |     |
|     2.3: Clicar no botão Enviar |  |     |
|   3: Ver protocolo de solicitação  | | |
|   4: Acompanhar protocolo de solicitação em "Acompanhe sua solicitação"  | 1>2 | Plano: Preencher número de protocolo e em seguida clicar em consultar <br> Feedback: Tela de acompanhamento de solicitação de iluminação pública  |
|     4.1: Colocar protocolo no campo requerido | |    |
|     4.2: Clicar em consultar | |      
|     4.3: Visualizar a situação e atualizações do protocolo | |       

<div align="center">
<p> <b>Tabela 2</b>: HTA da Tarefa: Informar luminária queimada no Município (Fonte: Heler, Lucas. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA Poste.png" width="100%">
<div align="center">
<p> <b>Figura 2</b>: Diagrama HTA da Tarefa: Informar luminária queimada no Município </p>
</div>

### Análise da Tarefa HTA 2: Cadastrar e acompanhar uma reclamação na ouvidoria

| Objetivos / Operações                                | Relações      | Problemas / Recomendações                                                                                                      |
|------------------------------------------------------|---------------|----------------------------------------------------------|
| 0. Cadastrar e consultar uma reclamação cadastrada |1 > 2|       Input: Acesso ao site de Lagoa da Prata, Credenciais de login (usuário e senha). <br> Plano: Realizar login no site, Navegar até a Ouvidoria, Cadastrar reclamação desejada, Acessar a reclamação na lista, Acompanhar status. <br> Feedback: Status da reclamação cadastrada emitido.|
|   1. Realizar login no site   | 1 > 2|    Plano: informar o cpf e depois a senha do gov.br. <br> Feedback: tela menu de Serviços Registrato. |
|       1.1 Informar CPF | |           |
|       1.2 Informar senha do gov.br   | |  |
|   2. Navegar para a ouvidoria | 1 / 2 |   Plano: selecionar uma das opções, entre ir até pagina da ouvidoria através do menu hamburguer e ir até a pagina da ouvidoria através da aba de pesquisa <br>Feedback: Tela da ouvidoria que mostra opção de cadastrar reclamação  |
|   2.1 Ir através do menu hamburguer |  |     |
|   2.2 Ir através da aba de pesquisa |  |     |
|   3. Cadastrar Reclamação | 1 > 2 | Plano: Cadastrar uma reclamação através do formulário  <br>Feedback: Caixa de aviso avisando que a reclamação foi cadastrada |
|     3.1. Selecionar tipo, secretaria e assunto | |  |
|     3.2. Preencher texto de reclamação | |  |
|     3.3. Preencher campos opcionais | 1 / 2 | Plano: Cadastrar (ou não) campos adicionais do formulário  <br>Feedback: Campo adicional presente na pagina de acompanhamento |
|       3.3.1 Preencher endereço |  |  |
|       3.3.2 Solicitar Sigilo |  |  |
|     3.4. Resolver Captcha                    | |  |
|   4. Consultar status da reclamação | 1 > 2 | Plano: Acompanhar status da reclamação recem registrada  <br>Feedback: Campo de status presente na pagina de acompanhamento   |
|       4.1. Selecionar "meus protocolos" | |   |
|       4.2. Selecionar reclamação cadastrada | |    |
|       4.3. Conferir status | |    |

<div align="center">
<p> <b>Tabela 3</b>: HTA da Tarefa: Cadastrar e uma reclamação na ouvidoria (Fonte: Freitas, Cainã. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA Poste.png" width="100%">
<div align="center">
<p> <b>Figura 2</b>: Diagrama HTA da Tarefa: Informar luminária queimada no Município </p>
</div>

### Análise da Tarefa HTA 3: Cadastro Antecipado de Aluno

| Objetivos / Operações                                | Relações      | Problemas / Recomendações                                                                                                      |
|------------------------------------------------------|---------------|----------------------------------------------------------|
| 0. Realizar cadastro antecipado de aluno para matrícula escolar |1 > 2 > 3 > 4 > 5 > 6 > 7 > 8|      Input: Acesso ao site da Prefeitura de Goiânia, Dados do candidato, Dados do responsável, Dados sócio-econômicos. <br> Plano: Navegar até a seção de serviços, selecionar "Matrículas Web", acessar "Cadastro Antecipado", preencher dados, gravar dados, confirmar gravação. <br> Feedback: Confirmação de cadastro bem-sucedido.|
|   1. Encontrar a seção de serviços   | 1.1 > 1.2 > 1.3 > 1.4|    Plano: Abrir o navegador, acessar o site da prefeitura, navegar até o menu "SERVIÇOS", selecionar "MATRÍCULAS WEB". <br> Feedback: Acesso à página de matrículas web. |
|     1.1 Abrir o navegador | | Recomenda-se usar um navegador compatível com o site.         |
|     1.2 Acessar o site da Prefeitura de Goiânia   | | Pode ser necessário garantir uma conexão estável com a internet. |
|   1.3 Navegar até o menu "SERVIÇOS" ||   A identificação do menu "SERVIÇOS" deve ser clara.  |
|     1.4 Navegar até a opção "MATRÍCULAS WEB" |  |A opção "MATRÍCULAS WEB" deve estar visível e acessível no menu.     |
|   2. Navegar para a página de matrícula web   |2.1 > 2.2 | Plano: Visualizar a opção "Acessar Serviço", clicar para acessar. <br> Feedback: Página de cadastro antecipado aberta.|
|   2.1 Visualizar a opção "Acessar Serviço"   | | A opção deve ser funcional e responsiva.|
|   2.2 Clicar na opção "Acessar Serviço" | |   	A opção deve ser funcional e responsiva. |
|     3. Selecionar "Cadastro Antecipado" | 3.1 > 3.2| Plano: Visualizar e selecionar "Cadastro Antecipado". <br> Feedback: Página de inserção de dados aberta.   |
|     3.1 Visualizar a opção "Cadastro Antecipado"                       | | A opção deve ser destacada e facilmente localizável. |
|   3.2 Clicar na opção "Cadastro Antecipado"                   | |       A opção deve redirecionar corretamente.  |
|     4. Inserir dados do candidato | 4.1| Plano: Preencher campos obrigatórios em "Dados do Candidato". <br> Feedback: Campos preenchidos corretamente. |
|   4.1 Preencher os campos obrigatórios em "Dados do Candidato" | |    Plano: Navegar até a seção de movimentação, fazer download da movimentação|
|     5. Inserir dados do responsável | 5.1| Plano: Preencher campos obrigatórios em "Dados do Responsável". <br> Feedback: Campos preenchidos corretamente.                        |
|     5.1 Preencher os campos obrigatórios em "Dados do Responsável" | |Campos devem ser claros e permitir a inserção de informações sem erros.      
|     6. Inserir dados sócio-econômicos | 6.1| Plano: Preencher campos obrigatórios em "Dados Sócio-Econômicos". <br> Feedback: Campos preenchidos corretamente.    
|     6.1 Preencher os campos obrigatórios em "Dados Sócio-Econômicos" | | Campos devem ser claros e permitir a inserção de informações sem erros. 
|     7. Gravar os dados do candidato |7.1 > 7.2 | Plano: Verificar todas as informações e clicar em "Gravar Candidato". <br> Feedback: Dados salvos no sistema.    
|     7.1 Verificar todas as informações inseridas | |  Revisão de dados para evitar erros.   
|     7.2 Clicar no botão "Gravar Candidato" | | Botão deve ser claramente identificável e funcional.    
|    8. Confirmar gravação dos dados | 8.1 > 8.2|  Plano: Verificar balão de confirmação e clicar em "OK". <br> Feedback: Confirmação de dados gravados.   
|     8.1 Verificar o balão de confirmação de dados | |Mensagem de confirmação deve ser clara e compreensível.     
|     8.2 Clicar em "OK" no balão de confirmação de dados | | Botão "OK" deve ser funcional.      

<div align="center">
<p> <b>Tabela 4</b>: HTA da Tarefa: Cadastro Antecipado de Aluno (Fonte: Heler, Lucas. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/hta_matricula.jpg" width="100%">
<div align="center">
<p> <b>Figura 4</b>: Diagrama HTA da Tarefa: Cadastro Antecipado de Aluno </p>
</div>

### Análise da Tarefa HTA 4: Acessar o módulo de Contra Cheque e consultar processos do servidor 

|    Objetivos/Operações    |    Relações    |    Problemas e recomendações    |
| :-----------------------: | ------------------------------- | ------------------------------- | 
| 0. Acessar o módulo de Contra Cheque e consultar processos do servidor  |  | **input:** Localização e acesso ao modulo. | 
| 1. Selecionar a opção "Contra Cheque" | 1>2 | **input:** Escolha da opção para iniciar o processo de consulta. |
| 2. Preencher os campos requeridos de login | 2>3 |  **input:** Inserção de dados pessoais. |
| 3. Selecionar a opção "Processo Digital" |3>4 |  **input:** Escolha da opção para iniciar o acompanhamento dos processos. |
| 4. Escolher o processo  |4>5 |  **input:** Seleção do processo desejado. |
| 5. Acompanhar o status do processo | | **feedback:** Informação sobre o processo e resultados. |
 

<div align="center">
<p> <b>Tabela 5</b>: HTA da Tarefa: Acessar o módulo de Contra Cheque e consultar processos do servidor  (Fonte: Duarte, Augusto. 2024). </p>
</div>

<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA2.png" width="100%">
<div align="center">
<p> <b>Figura 5</b>: Diagrama HTA da Tarefa: Acessar o módulo de Contra Cheque e consultar processos do servidor </p>
</div>


### Análise da Tarefa HTA 5: Registrar e verificar o panorama de saúde da cidade


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

<div align="center">
<p> <b>Tabela 6</b>: HTA da Tarefa: Registrar e verificar o panorama de saúde da cidade (Fonte: MEIRELES, Lucas. 2024). </p>
</div>

<div>
<img title="a title" alt="Elementos HTA" src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA_Saude.png" width="100%">
<p> <b>Figura 6</b>: Diagrama HTA da Tarefa: Registrar e verificar o panorama de saúde da cidade (Fonte: Freitas, Cainã. 2024).</p>
</div>


### Análise da Tarefa HTA 6: Solicitar vistoria de local com água parada
Abaixo se encontra tanto a tabela e diagrama HTA relacionado a Solicitar vistoria de local com água parada, ambos foram elaborados levando em consideração a [persona Maria Arlete](/requisitos1/personas/#maria-arlete) e o [cenario C03](/requisitos1/cenarios/#c03-solicitar-vistoria-de-local-com-agua-parada).

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

<div align="center">
<p> <b>Tabela 7</b>: HTA da Tarefa: Solicitar vistoria de local com água parada (Fonte: DOURADO, Pedro Lucas. 2024). </p>
</div>

<div>
<img   src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/analiseTarefas/HTA_solicitacao.png" >
<p> <b>Figura 7</b>: Diagrama HTA da Tarefa: Solicitar vistoria de local com água parada (Fonte: DOURADO, Pedro Lucas. 2024).</p>
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

### Análise da Tarefa CNM-GOMS 2: Cadastro Antecipado de Aluno
```

Goal 0: Realizar cadastro antecipado de aluno para matrícula escolar
  Goal 1: Encontrar a seção de serviços
    METHOD 1.A: Encontrar através do menu "Serviços"
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até menu "SERVIÇOS"
        OP: Levar cursor até opção "MATRÍCULAS WEB"
        OP: Clicar com o botão esquerdo do mouse
    METHOD 1.B: Encontrar através da aba de pesquisa
    (SEL.RULE: preferência do usuário)
        OP: Levar cursor até barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "matrículas web"
        OP: Levar cursor até botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até opção "MATRÍCULAS WEB"
  Goal 2: Navegar para a página de matrícula web
    OP: Na nova página, visualizar e clicar na opção "Acessar Serviço"
  Goal 3: Selecionar "Cadastro Antecipado"
    OP: Selecionar a opção "Cadastro Antecipado"
  Goal 4: Inserir dados do candidato
    OP: Preencher os campos obrigatórios em "Dados do Candidato"
  Goal 5: Inserir dados do responsável
    OP: Preencher os campos obrigatórios em "Dados do Responsável"
  Goal 6: Inserir dados sócio-econômicos
    OP: Preencher os campos obrigatórios em "Dados Sócio-Econômicos"
  Goal 7: Gravar os dados do candidato
    OP: Clicar no botão "Gravar Candidato"
  Goal 8: Confirmar gravação dos dados
    OP: Clicar em "OK" no balão de confirmação de dados


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
### Análise da Tarefa CNM-GOMS 4: Registrar e verificar o panorama de saúde da cidade
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

### Análise da Tarefa CNM-GOMS 6: Cadastrar e acompanhar status de uma reclamação no conselho municipal de educação sobre uma escola do municipio da lagoa da prata
```
Goal 0: Cadastrar e acompanhar status de uma reclamação
  Goal 1: Encontrar Ouvidoria
    METHOD 1.A: Encontrar através do menu "hamburguer"
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até menu "hamburguer"
        OP: Levar cursor até botão "Ouvidoria"
        OP: Clicar com o botão esquerdo do mouse

    METHOD 1.B: Encontrar através da aba de pesquisa
    (SEL.RULE: peferência do usuário)
        OP: Levar cursor até barra de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Digitar "Ouvidoria"
        OP: Levar cursor até botão de pesquisa
        OP: Clicar com o botão esquerdo do mouse
        OP: Levar cursor até "Ouvidoria"
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

  Goal 3: Acompanhar status de reclamação cadastrada
    OP: Levar cursor até botão "Meus Protocolos
    OP: Levar cursor até protocolo cadastrado anteriormente
    OP: Clicar com o botão esquerdo do mouse
    OP: Navegar até status da reclamação
    OP: Acompanhar status
```
 


### Análise da Tarefa CNM-GOMS 6: Acessar o modulo de contra cheque e consultar processos do servidor
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

### Análise da Tarefa CNM-GOMS 7: Informar luminária queimada no Município
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

### Análise da Tarefa CNM-GOMS 8: Solicitar vistoria de água parada (Fonte: DOURADO, Pedro Lucas. 2024).
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
    OP. 4.3: rlica no botão "Enviar"

  Goal 5: Baixar os dados da solicitação
    OP. 5.1: move o cursor até o botão "Baixar dados da solicitação"
    OP. 5.2: clica com o botão esquerdo do dispositivo apontador


```


## Historico de Versões

|    Data    | Versão |                               Descrição                                |                   Autor(es)                   | Data de revisão |                                        Revisor(es)                                        |
| :--------: | :----: | :--------------------------------------------------------------------: | :-------------------------------------------: | :-------------: | :---------------------------------------------------------------------------------------: |
| 06/05/2024 | `1.0`  |                          Criação do documento                          | [Cainã Freitas](https://github.com/freitasc)  |   07/05/2024    |                       [Lucas Meireles](https://github.com/Katuner)                        |
| 06/05/2024 | `1.1`  |                      Adição de Análise de Tarefas                      | [Joyce Dionizio](https://github.com/joycejdm) |   07/05/2024    |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 06/05/2024 | `1.2`  |                     Adição de Análise de Tarefas 3                     | [Augusto Duarte](https://github.com/Augcamp)  |   07/05/2024    |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 06/05/2024 | `1.3`  |                     Adição de Análise de Tarefas 4                     | [Lucas Meireles](https://github.com/Katuner)  |   07/05/2024    |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 07/05/2024 | `1.4`  |                     Adição de Análise de Tarefas 5                     |  [Pedro Lucas](https://github.com/lucasdray)  |   07/05/2024    |                        [Lucas Heler](https://github.com/akaeboshi)                        |
| 07/05/2024 | `1.5`  |                   Adição de Análise de Tarefas HTA 1                   |  [Lucas Heler](https://github.com/akaeboshi)  |   07/05/2024    |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 10/05/2024 | `1.6`  | Edição de Análise de Tarefa e correção pós entrega ponto de controle 2 | [Lucas Meireles](https://github.com/Katuner)  |   13/05/2024    |                        [Pedro Lucas](https://github.com/lucasdray)                        |
| 22/05/2024 | `1.7`  |                  Adição de Análise de Tarefas 6 e HTA                  |  [Lucas Heler](https://github.com/Akaeboshi)  |   22/05/2024    |                       [Cainã Freitas](https://github.com/freitasc)                        |
| 22/05/2024 | `1.8`  |                            Adição de tarefa                            | [Joyce Dionizio](https://github.com/joycejdm) |   22/05/2024    | [Cainã Freitas](https://github.com/freitasc), [Pedro Lucas](https://github.com/lucasdray) |
| 06/06/2024 | `2.0`  |                            Adição de HTA 6                             |  [Pedro Lucas](https://github.com/lucasdray)  |                 |                                                                                           |
| 07/06/2024 | `2.1`  |                           Adição CNM-GOMS 8                            |  [Pedro Lucas](https://github.com/lucasdray)  |                 |                                                                                           |
