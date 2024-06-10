## Introdução
Este documento tem como objetivo definir as metas de usabilidade para o projeto presente que realizará uma avaliação do site da Prefeitura de Lagoa da Prata, estabelecendo quais fatores de qualidade devem ser priorizados no projeto, bem como a forma com a qual a avaliação ocorrerá durante o processo de design. 
A equipe irá se basear nas metas de usabilidade definidas por Nielsen (1999) para realizar as devidas verificações e consequentemente a avaliação como um todo para o site,
visando como objetivo primário a melhor intuição e tranquilidade do usuário durante sua navegação pelo site.


## Definição das Metas de Usabilidade

Através da análise de Barbosa (2021) sobre o trabalho de Nielsen (1999), é possível identificar 6 metas de usabilidade principais, sendo elas tratadas a seguir:

- Eficácia: Refere-se à qualidade do produto de cumprir com aquilo que foi planejado para fazer, ou seja, se ele é capaz de cumprir suas funcionalidades da forma que foram planejadas para serem realizadas.

- Eficiência: Refere-se à forma e facilidade com a qual os usuários são capazes de realizar suas tarefas no site, preferencialmente no menor número possível de passos.

- Segurança: Refere-se à proteção do usuário contra situações indesejadas, como a perda de dados, a realização de ações inadvertidas e em como o sistema é capaz de fornecer um ponto de retorno ao usuário para se recuperar de eventuais falhas.

- Utilidade: Refere-se à relevância das informações e funcionalidades disponibilizadas no site para os usuários, isto é, se o usuário conseguirá encontrar uma função que solucione sua necessidade ao utilizar o sistema.

- Aprendizagem: Refere-se à facilidade com que os usuários conseguem aprender a utilizar o site e se tornar competentes na realização das tarefas.

- Memorização: Fortemente associado à aprendizagem, refere-se à facilidade com que os usuários conseguem lembrar como utilizar o site após terem tido alguma experiência no sistema.

## Metas a serem conquistadas pelo nosso projeto
Para definir as metas que desejamos alcançar foram levantadas as seguintes questões sobre cada meta:

- Eficácia: O sistema atende às funções à qual foi projetado?
    - O site fornece diversas formas de informações públicas, como lista de espera de creches, lista de espera para o SUS, consulta de editais, itens relacionados à prestação de serviços, itens relacionados à transparência de gastos, entre outros. Há porém de se analisar as diversas partes do sistema, que se apresenta para diversas funcionalidades à diferentes áreas, como cidadão, empresa, funcionários, etc. O site avaliado apresenta algumas páginas e funcionalidades que estão incompletas ou não aparentam ter sido implementadas até então, como é o caso de uma listagem de prefeitos, de informações do prefeito atual, de eventos atuais, entre outros. Sendo demonstrado na Figura 1 a seguir:
<div style="text-align:center;">
  <p>Figura 1 - Login em Guia Externa <br>
  <img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/sitePrefeitura/eficacia.png" alt="Tecnologias Wappalyzer"> <br>
  Disponível em https://www.lagoadaprata.mg.gov.br/portal/. Acesso em 03/06/2024
  </p>
</div>
- Eficiência: Quanto tempo leva para realizar uma tarefa específica?
    - A maioria das atividades no site é realizada em poucas interações, como consultas de editais e acesso à listas de espera, mas algumas atividades levam a links externos que exigem login ou preenchimento de formulários, comumente visto em áreas para empresas ou verificações de impostos pelo cidadão. Sendo demonstrado na Figura 2 a seguir:

<div style="text-align:center;">
  <p>Figura 2 - Login em Guia Externa <br>
  <img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/sitePrefeitura/eficiencia.png" alt="Tecnologias Wappalyzer"> <br>
  Disponível em https://www.lagoadaprata.mg.gov.br/portal/. Acesso em 03/06/2024
  </p>
</div>

- Segurança: O sistema evita erros ou ações indesejáveis? Ele permite recuperar ações anteriores?
    - O site não oferece alternativas de segurança para evitar erros, especialmente para atividades que levam a guias externas. Como mostra a Figura 3 a seguir:

<div style="text-align:center;">
  <p>Figura 3 - Guia Externa sem retorno <br>
  <img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/sitePrefeitura/seguranca.png" alt="Tecnologias Wappalyzer"> <br>
  Disponível em https://www.lagoadaprata.mg.gov.br/portal/. Acesso em 03/06/2024
  </p>
</div>

- Utilidade: O sistema oferece a funcionalidade certa no contexto certo?
    - O site possui seções de acesso rápido para atividades específicas, porém também há ocorrências em que os usuários precisam navegar por locais gerais, como "Serviços de Cidadão", para encontrar atividades específicas ou ainda pelo ícone de menu geral e que poderiam estar disponibilizadas na página principal de uma forma direta como "Inscrições Habita Lagoa" ou "Solicitar ITBI On-line". Como mostra na figura 4 a seguir:

<div style="text-align:center;">
  <p>Figura 4 - Atividades Específicas de Díficil localização <br>
  <img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/sitePrefeitura/utilidade.png" alt="Tecnologias Wappalyzer"> <br>
  Disponível em https://www.lagoadaprata.mg.gov.br/portal/. Acesso em 03/06/2024
  </p>
</div>

- Aprendizagem:  É fácil aprender a usar o sistema?
    - O site oferece uma experiência de aprendizado intuitiva e os dados estão organizados de forma que facilitem a utilização de determinadas funções, porém existem funções e informações que estão "escondidas" pelo site e exigem mais atenção à detalhes e movimentação do usuário por outras páginas para encontrá-las.

- Memorização: Que suporte é oferecido para auxiliar o usuário a realizar tarefas, especialmente as não recorrentes?
    -  Não é oferecido nenhum guia ou suporte ao usuário, logo o usuário depende inicialmente de que nenhuma mudança seja feita na página inicial do sistema levando a uma memorização das funcionalidades requiridas e também corre o risco de perder um acesso rápido à alguma funcionalidade caso o site remova do destaque aquilo que o usuário estava buscando, como é o caso de notícias mostrado na Figura 5 abaixo.

<div style="text-align:center;">
  <p>Figura 5 - Funcionalidade de díficil localização <br>
  <img src="https://raw.githubusercontent.com/Interacao-Humano-Computador/2024.1-Prefeitura-Lagoa-da-Prata/main/docs/assets/images/sitePrefeitura/memorizacao.png" alt="Tecnologias Wappalyzer"> <br>
  Disponível em https://www.lagoadaprata.mg.gov.br/portal/. Acesso em 03/06/2024
  </p>
</div>



## Conclusão
Com base na análise, foi estabelicido as metas que devem ser focadas para melhorar a usabilidade do site da Prefeitura Municipal de Lagoa da Prata, sem que haja um grande retrabalho em suas funcionalidades e aparência. 
Também adotaremos a metodologia de avaliação heurística criando 2 perfis de usuário: 
 - Usuário com pouca ou nenhuma familiaridade com computadores e tecnólogias e que possui dificuldades para acessar.
 - Usuário comum que possui um conhecimento médio de acesso e familiaridades com acessos a sites e computadores.

 Com isso foi feita a seguinte tabela com resultados:

| Meta de usabilidade | Como será feito a avaliação                                                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eficiência          | Garantir que as atividades possam ser realizadas em no máximo 2 cliques e que estejam descritas de forma não ambígua, evitando ao máximo o uso de links externos                                      |
| Segurança           | Garantir medidas que permite ao usuário reverter ações indesejadas facilmente, tendo opções de confirmação a fim de evitar que o usuário faça alguma ação ou interação que não estava planejado fazer |
| Utilidade           | O usuário deve receber feedback visual do que está acontecendo em tempo real para confirmar suas ações e que seja de facil localização                                                                |
| Aprendizagem        | Garantir que a aprendizagem da utilização do site seja intuitiva e facil assim como um guia rapido de como utilizar para que usuários com pouca ou nenhuma experiência não sejam prejudicados |


## Referências Bibliográficas

> [1] Barbosa, S. D. J.; Silva, B. S. da; Silveira, M. S.; Gasparini, I.; Darin, T.; Barbosa, G. D. J. (2021) Interação Humano-Computador e Experiência do usuário. Autopublicação.

> [2] NIELSEN, Jacob. Designing Web Usability: The Practice of Simplicity Peachpit Press, la edição 1999


## Historico de Versões

|    Data    | Versão |             Descrição              |                   Autor(es)                   | Data de revisão |                  Revisor(es)                  |
| :--------: | :----: | :--------------------------------: | :-------------------------------------------: | :-------------: | :-------------------------------------------: |
| 11/05/2024 | `1.0`  |        Criação do documento        | [Joyce Dionizio](https://github.com/joycejdm) |   11/05/2024    | [Lucas Meireles](https://github.com/Katuner)  |
| 11/05/2024 | `1.1`  |  Adição da estrutura do documento  | [Joyce Dionizio](https://github.com/joycejdm) |   11/05/2024    | [Lucas Meireles](https://github.com/Katuner)  |
| 11/05/2024 | `1.2`  | Definição das Metas de Usabilidade | [Joyce Dionizio](https://github.com/joycejdm) |   11/05/2024    | [Lucas Meireles](https://github.com/Katuner)  |
| 11/05/2024 | `1.3`  |   Ajuste de referencial e nomes    | [Lucas Meireles](https://github.com/Katuner)  |   13/05/2024    | [Augusto Duarte ](https://github.com/Augcamp) |
| 11/05/2024 | `1.4`  |    Ajuste de escrita e de metas    | [Lucas Meireles](https://github.com/Katuner)  |   13/05/2024    | [Augusto Duarte ](https://github.com/Augcamp) |
| 03/06/2024 | `2.0`  |  Correção pós entrega artefato 3   | [Pedro Lucas](https://github.com/lucasdray) |                 |                                               |
