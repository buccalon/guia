-----------------

### Nível de Descrição (`DescriptionLevel`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`created`     | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`id`          | **PK**, Sequential | id único do nível de descrição | 001
`title`       | CharField(128), Null, Blank | título do nível de descrição    | 0. Controle Inicial
`description` | CharField(512),Null, Blank, | descrição do campo | Conferência, identificação e localização da aquisição para estabelecimento de controle patrimonial.


Exemplos de instâncias que vão constar neste modelo:

ID    | Name                    | Description     |
------|-------------------------|--------------|
0     | Controle inicial        | Conferência, identificação e localização da aquisição para estabelecimento de controle patrimonial. |
1     | Descrição Básica        | Registro de informações de procedência, proveniência e contextualização. |
2     | Descrição Intermediária | Identificação de informações para produção do arranjo, a partir da função primária e tipologia documental. Registro de informações de série, autoria, data de produção e caracterização formal. |
3     | Descrição Avançada      | Descrição individual dos documentos. Registro de informações primárias ou atribuídas, em cruzamento com fontes externas. Documentação retrospectiva, reconstituição de usos e referências ao documento em seu contexto de produção, apresentação e circulação. Conjuntos de documentos podem ser descritos em lote. |
4     | Pesquisa especializada  | Elaboração de argumento interpretativo e construção de conhecimento novo a partir da seleção e co-relação de documentos. Apresentação, mediação e interpretação para fins de difusão de conhecimento. Redação de legendas expandidas e textos de inéditos. |

-----------------

### Tipo de Agregação (`AggregationType`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | **PK**, Sequential | id único do nível de descrição | 001
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`      | CharField(128), NotNull, Blank, | Tipo de Agregação | Coleção
`description`   | CharField(512)     | descrição do campo | Conjuntos de __documentos reunidos intencionalmente__ por uma pessoa ou instituição |

Exemplos de instâncias que vão constar neste modelo:

ID  | Title        | Description     |
----|--------------|--------------|
1   | Coleção      | Conjuntos de __documentos reunidos intencionalmente__ por uma pessoa ou instituição |
2   | Arquivo      | Conjuntos de __documentos produzidos e acumulados__ por uma pessoa ou instituição __no desempenho de suas atividades__ |
3   | Biblioteca   | Conjuntos de __livros e publicações reunidos__ por uma pessoa ou instituição |
4   | Conjunto     | Agrupamento documentos |

-----------------

### Gênero Documental (`GenreTags`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | **PK**, Sequential | id único do nível de descrição | 001
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`      | CharField(128), NotNull, Blank, | Tipo de Agregação | Audiovisual
`description`   | CharField(512)     | descrição do campo| Filmes cinematográficos, fitas magnéticas, vídeo digital e demais suportes audiovisuais.|

Exemplos de instâncias que vão constar neste modelo:

ID  | Title          | Descriptio             |
----|----------------|----------------------|
1   | Audiovisual    | Filmes cinematográficos, fitas magnéticas, vídeo digital e demais suportes audiovisuais. |
2   | Bibliográfico  | Livros, jornais, revistas, catálogos e brochuras. |
3   | Cartográfico   | Mapas e plantas arquitetônicas. |
4   | Fotográfico    | Fotografias em papel, slides, negativos, cromos e demais suportes fotográficos. |
5   | Iconográfico   | Desenhos, gravuras, caricaturas, charges, cartazes e peças gráficas. |
6   | Nato-digital   | Documentos originalmente gerados em computadores. |
7   | Sonoro         | Discos, fitas, cds e álbums. |
8   | Textual        | Cadernos, manuscritos, impressos e folheteria. |
9   | Tridimensional | Objetos tridimensionais. |

-----------------

### Condições de Acesso (`AccessCondition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`id`          | **PK**, Unique, Sequential  | Identificador de cada registro |
`title_short` | CharField(64), Unique, Null, Blank | Identificador textual único da condição de acesso |  Livre
`title_long`  | CharField(128), Null, Blank | Título longo da condição de acesso |  Acesso pleno
`description`| TextField, Null, Blank | Descrição completa da condição de acesso | Todos os documentos originais ou seus representantes digitais estão disponíveis para consulta.

Exemplos de instâncias que vão constar neste modelo:

ID      | Access    | title            | description         |
--------|-----------|------------------|---------------------|
0       | Livre     | Acesso pleno     | Todos os documentos originais ou seus representantes digitais estão disponíveis para consulta.
1       | Parcial   | Em processamento | Existem documentos em processamento técnico (inventário, identificação, ordenação, higienização, acondicionamento, digitalização ou restauro) ou em uso (empréstimo para exposições ou em consulta por outros pesquisadores).
2       | Parcial   | Estado de conservação | Existem documentos cujo estado de conservação coloca em risco a estabilidade ou a própria existência dos mesmos.
3       | Restrito  | Direito autoral  | Existem restrições ao acesso aos documentos por questões de direito autoral. O pesquisador pode solicitar acesso mediante autorização expressa do titular, herdeiro ou detentor dos referidos direitos.
4       | Restrito  | Contratual       | Existem restrições ao acesso aos documentos por questões contratuais definidas por cláusulas especificadas no processo de aquisição.
5       | Restrito  | Segurança institucional | Existem restrições ao acesso aos documentos por questões de risco à seguraça operacional. Aplica-se exclusivamente a documentos do arquivo institucional.
6       | Restrito  | Informação privada | Existem restrições ao acesso aos documentos por questões de privacidade envolvendo informações de cunho extritamente privado de terceiros.
