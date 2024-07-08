## Introdução

Durante a realização de uma tarefa de design, é comum que se siga diversos guias, processos e premissas para que o trabalho, além de ter um embasamento teórico amplo e robusto, possua uma certificação maior de qualidade e consiga atingir seus objetivos predeterminados. De acordo com Barbosa (2021) [1], os responsáveis pelo design seguem 3 principais conjuntos de características em IHC, sendo eles princípios (objetivos gerais e alto nível), diretrizes (regras gerais de prática) e padrões (soluções específicas). 
É importante ressaltar, porém, que a utilização e embasamento de princípios e diretrizes não substitui as demais atividades gerais previstas, isto é, para este projeto, a importância de que quesitos estabelecidos pelo processo de design de Mayhew (1999) continue sendo seguido.


## Principais princípios e diretrizes de projeto

A comunidade de pesquisadores de IHC costumam seguir determinados princípios e diretrizes para exercer sua função, itens estes que serão trabalhados a seguir em comparação com 
o site da Prefeitura Municpal de Lagoa da Prata. Há um enfoque, também, na publicação de Norman (1988) que destaca algumas das diretrizes bases que hoje são consideradas como imprescindíveis para a realização da tarefa de design, como facilitação de aprendizado e compreensão do usuário, desenvolvimento de modelos conceituais, compreensão do estado do sistema, entre outros. 

## Metodologia 
Neste artefato iremos utilizar os prinípios e diretrizes de projeto de acordo com Norman (1988)[3], Tognazzini (2014)[4], as heurísticas de Nielsen (1994)[5] e as regras de ouro de Shneiderman (Shneiderman, 1998) [6]. Será apresentado cada um dos 8 princípios, tendo uma descrição e um tópico mostrando a violação do princípio cometida pelo site com prints demonstrando a mesma.
Para avaliação de violação será utilizado o método de inspeção utilizando a avaliação heurística das princípais funcionalidades do site. 

### Correspondência com as Expectativas dos Usuários
Devemos nos certificar de que o usuário consegue determinar os relacionamentos entre: intenções e ações possíveis; entre ações e seus efeitos no sistema; entre o estado real do sistema e o que é percebido pela visão, audição ou tato; entre o estado percebido do sistema e as necessidades, intenções e expectativas do usuário. [1]


#### Violação
Na Figura 1 abaixo, é possivel visualizar a violação da Correspondência com a Expectativa do Usuário, uma vez que o usuário clica para saber a respeito do prefeito da cidade e encontra apenas a foto e seu nome que não está completo

<center>

**Figura 01** - Violação sessão prefeito

![Violação Prefeito](../assets/images/principios_gerais/prefeito.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

### Simplicidade nas Estruturas das Tarefas
Para uma simplificação nas estruturas das tarefas deve-se reduzir a quantidade de planejamento e resolução [3], e para isso os designers podem seguir as 4 abordagens tecnológicas a seguir:
- manter a tarefa inalterada, mas oferecer diferentes formas de suporte para que os usuários possam aprender e executar a tarefa
- utilizar a tecnologia para tornar visível o que seria invisível, aprimorando o feedback e a capacidade do usuário de manter o controle da tarefa
- automatizar a tarefa, ou parte dela, mantendo-a inalterada
- alterar a natureza da tarefa

#### Violação
Na figura 2 abaixo, é possível visualizar uma violação da Simplicidade nas Estruturas das Tarefas em que o serviço de ouvidoria não é encontrado de nenhuma forma dentro do site da prefeitura e caso o usuário queria acessar o serviço teria que fazer uma busca usando um buscado externo como o Google para encontrar, como mostra a figura 3.

<center>

**Figura 02** - Busca ouvidoria 

![Busca ouvidoria ](../assets/images/principios_gerais/busca_ouvidoria.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

<center>

**Figura 03** - Busca ouvidoria externa

![Busca ouvidoria externa](../assets/images/principios_gerais/ouvidoria_buscagoogle.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

Abaixo temos a figura 4 que mostra que o serviço existe dentro da página mas não existem formas dentro do site para acessá-la

<center>

**Figura 04** - Ouvidoria

![Ouvidoria](../assets/images/principios_gerais/ouvidoria.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

### Equilíbrio entre Controle e Liberdade do Usuário

De acordo com Tognazzini (2014), o computador, a interface e o ambiente de trabalho “pertencem” ao usuário. Isto é dizer que o usuário deve ter o maior controle e decisões de como alcançar seu objetivo sem se sentir "forçado" a uma sequência de ações fixa ou não possuir poder de decisão sobre as ações que está realizando. Isso implica que muitas vezes é vantajoso que o usuário seja capaz de realizar uma mesma tarefa de modos diferentes, ou até cancelar uma ação sem que o sistema o impeça ou penalize-o por isso. 

#### Violação
Na figura 05, podemos visualizar uma violação contra a liberdade do usuário, embora o site permita que ele visualize todos os tipos de registros encontrados, não é permitido para o usuário visualizar todos os registros de uma vez tendo que filtrar um por um e não podendo selecionar todos de uma vez

<center>

**Figura 05** - Busca falta de liberdade

![Busca](../assets/images/principios_gerais/busca.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

### Consistência e Padronização

Para facilitar o aprendizado e uso de um sistema, recomenda-se assegurar a consistência da interface com o modelo conceitual embutido no sistema[3], sendo a mais importante consistência a de expectativas dos usuários e quando essa correspondência não for possível é preciso padronizar [3][4].

#### Violação
Mesmo que o site em sua maior parte siga uma certa consistência e padronização, ele peca em alguns aspectos como mostrado na figura 5 abaixo em que nota-se uma violação da consistência e padronização uma vez que o menu hambúrguer está totalmente inconsistente e despadronizado.

<center>

**Figura 06** - Menu Hambúrguer

![Menu Hamburguer](../assets/images/principios_gerais/menu_hamburguer.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>


### Promovendo a Eficiência do Usuário
A eficiência do usuário vem sempre em primeiro lugar, e não a do computador. [4] O usuário deve ser mantido ocupado, logo , processamentos demorados não devem prender a interação, mas sim permitir que os usuários continuem seu trabalho com outras partes do sistema, suprimindo a ociosidade e economizando tempo e esforço do usuário.

#### Violação
Há algumas funcionalidades no site em que redireciona o usuário para outros links sem uma alternativa de retorno para a página em que o usuário estava anteriormente notando-se uma violação em promover a eficiência do usuário que terá que usar o botão do navegador ou acessar novamente a página do site da Prefeitura, como mostra a figura 07 a seguir que ao clicar em transparência no menu suspenso é redirecionado para um link externo sem opção de volta mostrado na figura 08.

<center>

**Figura 07** - Menu Suspenso

![Menu Suspenso](../assets/images/principios_gerais/menu%20suspenso.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

<center>

**Figura 08** - Página de Transparência

![Transparência](../assets/images/principios_gerais/transparencia.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://transparencia.betha.cloud/#/5jrYiAhzcWF174nC3B1Hkw==>. Acesso em 07/07/2024*

</center>



### Antecipação
Deve ser fornecido todas as informações e ferramentas necessárias ao usuário para cada passo realizado, fazendo com que não seja necessário o usuário buscar ou coletar informações.

#### Violação
Mesmo já estando cadastrado e logado no site da Prefeitura, ao tentar realizar a solicitação de troca de lâmpadas, o site requer que o usuário preenche dados que poderiam ter sido puxados do perfil, como nome do requerente, email, telefone para contato; como mostrado na figura 09 abaixo.

<center>

**Figura 09** - Página de solicitação de troca de lâmpadas

![Transparência](../assets/images/principios_gerais/troca_de_lampada.png)

*Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 07/07/2024*

</center>

### Visibilidade e Reconhecimento
Antes de executar uma ação, o usuário deve ter uma visão prévia das diferentes maneiras de realizá-la e das instruções para sua execução. Além disso, a interface deve fornecer informações lógicas e acessíveis ao usuário no momento necessário.[3]

TERMINAR



### Conteúdo Relevante e Expressão Adequada - REVISAR

Reeves e Nass (1996) estabelecem que uma interação bem polida seguem 4 máximas: qualidade (não apresentar informações que não se sabe se são reais), quantidade (não exibir mais informações que o necessário para o objetivo), relação (os itens devem estar relacionados de forma clara e não confusa) e modo (evitar ambiguidades). Isto também quer dizer que o sistema deve ser reconhecível aos usuários e que eles não estarão confusos quanto às informações que devem preencher na página. 
É possível notar, porém, conforme apresentado na figura 7 que segue este texto, há locais no site avaliado que não respeitam essas máximas e podem com certa facilidade desmotivar o usuário a completar seu objetivo. No caso apresentado, o usuário está na página primária para visualização geral dos eventos que irão ocorrer no município, e, apesar de possuir um breve texto introdutório como "agenda", ele não é explicado sobre o calendário ao lado e nem as informações disponíveis ao posicionar o mouse sobre uma data específica, assim como as informações apresentadas quando feita, não são devidamente expostas ou claras (período dos eventos).

<center>
<img src="https://github.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/blob/main/docs/assets/images/sitePrefeitura/menu_eventos.png?raw=true">
Figura 7 - Área de eventos registrados. Fonte: Prefeitura Municipal de Lagoa da Prata. 2024. Disponível em <https://www.lagoadaprata.mg.gov.br/portal/>. Acesso em 11/05/2024
</center>


### Projeto para Erros - REVISAR

Por fim, tratamos também de projeções para um erro, isto é, levar em consideração que, de alguma forma, um erro poderá acontecer e como é possível evitar esse erro ou ainda evitar que seja uma falha que possa levar a uma consequência severa ao usuário. Em um exemplo, isso significa salvar informações de um formulário em caso de uma mudança indesejada de página, em caso de perda de conexão, ou ainda evitar que um clique errado do usuário, como é possível ocorrer no site da Prefeitura aqui trabalhado, resulte na perda de quaisquer informações e/ou pesquisas já realizadas na página.


## Referenciais Bibliográficos

> [1] Barbosa, S. D. J.; Silva, B. S. da; Silveira, M. S.; Gasparini, I.; Darin, T.; Barbosa, G. D. J. (2021) Interação Humano-Computador e Experiência do usuário. Autopublicação.

> [2] Mayhew, Deborah J. (1999). The Usability Engineering Lifecycle: A Practitioner’s Handbook for User Interface Design. Morgan Kaufmann, 1st edition edition.

> [3] Norman, Don (1988). The Psychology Of Everyday Things. Basic Books, New York, illustrated edition edition.

> [4] Tognazzini, Bruce (2014). First Principles of Interaction Design (Revised & Expanded).

> [5] Reeves, Byron e Nass, Clifford (1996). The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places. Cambridge University Press/CSLI, Stanford, Calif, new edition edition.

> [6] Shneiderman, Ben (1998). Designing the User Interface: Strategies for Effective Human Computer Interaction. Addison-Wesley

## Historico de Versões

|    Data    | Versão |                         Descrição                         |                                     Autor(es) | Data de revisão |                 Revisor(es)                  |
| :--------: | :----: | :-------------------------------------------------------: | --------------------------------------------: | :-------------: | :------------------------------------------: |
| 11/05/2024 | `1.0`  |                   Criação do documento                    | [Joyce Dionizio](https://github.com/joycejdm) |   13/05/2024    | [Augusto Duarte](https://github.com/Augcamp) |
| 11/05/2024 | `1.1`  |                  Elaboração do documento                  |  [Lucas Meireles](https://github.com/Katuner) |   13/05/2024    | [Augusto Duarte](https://github.com/Augcamp) |
| 07/07/2024 | `2.0`  | Reestruturação completa do documento, TUDO foi refatorado |   [Pedro Lucas](https://github.com/lucasdray) | 07/07/2024 | [Pedro Lucas](https://github.com/lucasdray)  |