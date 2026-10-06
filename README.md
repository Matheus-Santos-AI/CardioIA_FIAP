# ❤️ CardioIA

> Projeto acadêmico do curso de IA — FIAP
> Metodologia PBL (Project Based Learning)

## 📋 Sobre o Projeto

O **CardioIA** é uma plataforma digital inteligente que simula o ecossistema de uma cardiologia moderna, integrando dados clínicos, Machine Learning, Visão Computacional, IoT e agentes inteligentes para triagem, diagnóstico, monitoramento, assistência remota e previsões médicas.

Esta é a **Fase 1** do projeto, na qual assumimos o papel de cientistas de dados hospitalares, responsáveis por levantar, organizar e documentar três tipos fundamentais de dados que servirão de base para as fases seguintes do projeto:

1. **Dados Numéricos** (IoT) — variáveis clínicas de pacientes cardíacos;
2. **Dados Textuais** (NLP) — textos médicos/literários sobre saúde cardiovascular;
3. **Dados Visuais** (Visão Computacional) — imagens de exames cardiológicos. https://drive.google.com/drive/folders/1cJQ_F9KFJgSQsAAJuBPls_IACj-dZPbi?usp=sharing

---

## 👥 Integrantes do Grupo

| Nome | RM |
|------|----|
| Matheus Santos | 566901 | 
| Ricardo José Amorin | 567312 |
| Victor Oliveira Fedeli Tate | 566823 |
| Paulo Roberto Silva Amaral Ribeiro Junior | 568413 |
| Klaus Lohany Barbosa de Oliveira | 566994 |

---
# 🎬 Vídeos de cada fase:
- Fase 2 -Diagnostico Automatizado ( https://youtu.be/igTSt70JQWE )

---


## 🗂️ Estrutura do Repositório

```
CardioAI_FIAP/
│
├── README.md                  
├── docs/                      
│   ├── Frases_Sintomas_Faceis.txt
│   ├── frase_risco.csv
│   ├── resultado_dignostico.csv
│   ├── sintomas.csv
│   ├── texto1.txt
│   └── texto2.txt
├── src/
│   ├── DADOS_CARDIO_AI.ipynb
│   └── text_transform.ipynb
├── assets/                    
│    
└── dataset/                   
    └── dataset_dados.csv
```

---

## ❤️ Fase 1: Batimentos de Dados

## 📊 Parte 1 — Dados Numéricos (IoT)

### Origem dos dados
Para a base de dados foi utilizada uma base de dados real , obtida através do site (https://www.kaggle.com/datasets/m0hamedyousry/ptb-xl-a-large-publicly-available-ecg-dataset), que possui 21,837 dados clínicos para estudo de doenças cardíacas.
A principio foi feito o estudo do dataset, seu tratamento de dados nulos e filtragem ,foi considerado 50 amostras de cada diagnostico para que o treinamento seja feito de forma mais rápido e com menos custo de computacional.
Alguns dados foram gerados sinteticamente de forma querente ao diagnostico e adicionado ao dataset original , para criar um modelo de dados mais completo e com parâmetros de triagem.
O script que fez o tratamento do dataframe e a geração de imagens esta em anexo no repositório.


### Link para o dataset
🔗 **Dataset completo:** [dataset/dataset_dados.csv](dataset/dataset_dados.csv)

> O dataset contém 250 linhas e 17 colunas com variáveis clínicas de pacientes cardíacos.

### Variáveis presentes

| Variável | Coluna no CSV | Tipo | Descrição |
|----------|---------------|------|-----------|
| ID do Paciente | `patient_id` | Numérica (identificador) | Identificador único do paciente |
| Idade | `age` | Numérica | Idade do paciente em anos |
| Sexo | `sex` | Categórica/Binária | 0 = Feminino / 1 = Masculino |
| IMC | `IMC` | Numérica | Índice de Massa Corporal (kg/m²) |
| Pressão Arterial | `pressao` | Numérica | Pressão arterial (mmHg) |
| Colesterol Total | `colesterol_total` | Numérica | Nível de colesterol total (mg/dL) |
| Diabetes | `diabetes` | Categórica/Binária | 0 = Não / 1 = Sim |
| Doença Cardíaca | `doenca_cardiaca` | Categórica/Binária | 0 = Não / 1 = Sim |
| Estágio do Infarto | `infarction_stadium1` | Categórica (ordinal) | Estágio do infarto identificado (0 a 4) |
| Classificação Diagnóstica | `diagnostic_superclass` | Categórica | Classe diagnóstica do exame (ex: NORM, MI, STTC, HYP, CD) |
| Relatório | `report` | Numérica/Categórica | Código de referência do laudo/relatório clínico |
| Dor no Peito | `dor_peito` | Categórica/Binária | 0 = Não / 1 = Sim |
| Dor Irradiada | `dor_irradiada` | Categórica/Binária | 0 = Não / 1 = Sim |
| Náusea | `nausea` | Categórica/Binária | 0 = Não / 1 = Sim |
| Falta de Ar | `falta_de_ar` | Categórica/Binária | 0 = Não / 1 = Sim |
| Arquivo ECG (baixa resolução) | `filename_lr` | Texto (caminho de arquivo) | Referência ao arquivo de sinal de ECG em baixa resolução |
| Arquivo ECG (alta resolução) | `filename_hr` | Texto (caminho de arquivo) | Referência ao arquivo de sinal de ECG em alta resolução |

### Variáveis mais relevantes clinicamente
Foram utilizados dados considerados relevantes para o modelo tanto de números quanto de sintomas ou doenças pré-existentes.  

### Considerações sobre Governança de Dados e Viés
O tratamento dos dados foi feito de forma imparcial e randômica , foi utilizado um dataset publico sem nenhum tipo de menção aos pacientes , assim preservando seu anonimato e os seus direitos a privacidade de dados.
As amostras de cada diagnostico foram escolhidas randomicamente através de um código python em que não se considera nenhum tipo de filtro que possa ser discriminatório ou causar algum tipo de viés.
Os dados são de origem alemã e tem seu tempo de coleta entre os anos de 1989 e 1994.

---

## 📝 Parte 2 — Dados Textuais (NLP)

### Textos selecionados

| Arquivo | Título | Fonte |
|---------|--------|-------|
| `docs/texto_1.txt` | The Project Gutenberg eBook of An anatomical disquisition on the motion of the heart & blood in animals | William Harvey | (original e traduzido)
| `docs/texto_2.txt` | Tempo de chegada do paciente com infarto agudo do miocárdio em unidade de emergência | Alessandra Soler Bastos1/ Lúcia Marinilza Beccaria / Ligia Márcia Contrin / Cláudia Bernardi Cesarino |

### Aplicações de NLP

Os dois textos selecionados têm naturezas distintas — um é um relato histórico-biográfico, o outro é um artigo científico com dados clínicos — o que permite explorar diferentes técnicas de Processamento de Linguagem Natural:

**1. Extração de sintomas e entidades clínicas (NER — Named Entity Recognition)**
O `texto_2.txt` descreve explicitamente os sintomas apresentados por pacientes com infarto agudo do miocárdio (dor no tórax, dor irradiada, dispneia, sudorese súbita, náusea). Um algoritmo de NER pode ser treinado ou ajustado para identificar automaticamente menções a sintomas, fatores de risco (hipertensão, diabetes, dislipidemia, sedentarismo) e termos clínicos (delta T, cateterismo, angioplastia) em textos livres de prontuários, permitindo estruturar dados que hoje existem apenas em texto corrido.

**2. Classificação de tópicos**
Combinando os dois textos, é possível treinar um classificador para distinguir entre diferentes tipos de conteúdo em saúde — por exemplo, texto científico/estatístico (`texto_2`) vs. texto histórico/narrativo (`texto_1`), ou, dentro de um corpus maior, separar artigos por tema (diagnóstico, tratamento, prevenção, epidemiologia). Essa classificação é útil para organizar automaticamente grandes volumes de literatura médica.

**3. Extração de informação estruturada a partir de texto não estruturado**
O `texto_2.txt` contém dados quantitativos embutidos em texto (ex: "idade média de 62,35 ± 14,66 anos", "delta T de 9h54min ± 18h9min"). Técnicas de extração de informação (regras, expressões regulares combinadas com NLP, ou modelos de extração de relações) podem converter essas menções textuais em variáveis estruturadas, aproximando esse texto do dataset numérico da Parte 1 do projeto.

**4. Análise de sentimentos e percepção do paciente**
Embora o `texto_2.txt` seja predominantemente técnico, ele relata comportamentos e percepções de pacientes diante dos sintomas (negação de que a dor fosse cardíaca, automedicação, demora em buscar ajuda). Um modelo de análise de sentimentos ou de intenção poderia ser aplicado a relatos de pacientes (como os que aparecem em prontuários ou entrevistas) para identificar sinais de negação, ansiedade ou desconhecimento — fatores que, segundo o próprio artigo, influenciam diretamente o tempo de chegada à emergência (delta T) e, portanto, o prognóstico.

**5. Sumarização automática**
O `texto_1.txt`, mais longo e narrativo, é um bom candidato para testar algoritmos de sumarização extrativa ou abstrativa, gerando resumos curtos de textos históricos ou de revisões de literatura — útil para profissionais de saúde que precisam consultar rapidamente grandes volumes de material.

**6. Análise terminológica e evolução da linguagem médica**
Como os dois textos pertencem a períodos e registros muito diferentes (um tratado científico de 1628/1906 vs. um artigo clínico de 2012), o corpus permite comparar a terminologia médica ao longo do tempo — por exemplo, como termos relacionados ao coração e à circulação evoluíram de descrições anatômicas gerais para nomenclatura clínica padronizada (IAM, delta T, cateterismo).

### Relevância para o projeto de IA em saúde

Essas análises são especialmente relevantes para o CardioIA porque boa parte do conhecimento clínico relevante — sintomas relatados, fatores de risco, comportamento do paciente diante da emergência — não está disponível em formato tabular, mas sim em texto livre (prontuários, laudos, artigos, relatos). Algoritmos de NLP permitem transformar esse conhecimento não estruturado em informação utilizável por modelos preditivos, complementando os dados numéricos  e as imagens , e aproximando o sistema de um cenário real de triagem e apoio à decisão clínica, em que o profissional de saúde frequentemente descreve o caso do paciente em linguagem natural


## 🩻 Parte 3 — Dados Visuais (Visão Computacional)


### Link para as imagens
🔗 **Banco de imagens:** (https://drive.google.com/drive/folders/1cJQ_F9KFJgSQsAAJuBPls_IACj-dZPbi?usp=sharing)

> O conjunto contém 250 imagens (.png).

### Origem das imagens
As imagens são referentes a Ecocardiogramas (ECG) geradas com os dados do dataset utilizado anteriormente (PTB-XL), e indexados aos respectivos pacientes.  

### Aplicações de Visão Computacional

- **Detecção de padrões:** identificar formatos característicos de ondas em ECGs (ex: arritmias);
- **Reconhecimento de anomalias:** apoiar a detecção precoce de cardiomegalia, obstruções em angiogramas ou irregularidades no ritmo cardíaco;
- **Segmentação de imagens:** criar um alerta para possíveis casos de infarto por redes neurais convolucionais (CNNs).

## Relevância 
A criação de um modelo computacional através de NLP , IOT, visão computacional e Redes Neurais, impacta diretamente na agilidade de pronto atendimento de pessoas com risco cardíaco, possibilitando a redução do tempo de atendimento que por muitos pode salvar vidas.  

## ❤️ Fase 2: Diagnostico Automatizado

### 📊 Parte 1 - Frases de Sintomas + Extração de Informações
- Foi criado um arquivo 'Frases_Sintomas_Faceis.txt' onde possui 20 frases simulando relatos de pacientes com um ou mais tipos de sintomas que podem ou não estar relacionados com problemas cardiacos.
- Em um arquivo CSV nomeado de 'sintomas.csv' foi criada uma estrutura de associações entre sintomas e doenças diagnosticadas, onde contem 26 linhas distribuídas em 5 tipo de classes sendo uma classe sintomas normais não relacionados a problemas cardíacos (normal) e outros 4 diagnósticos de doenças cardíacas (infarto, isquemia, distúrbio de condução e  hipertrofia).
- Através do código 'text_transform.ipynb' feito em python cruzamos os dois arquivos criados para conseguir identificar diagnósticos nas frases do arquivo 'Frases_Sintomas_Faceis.txt' utilizando a rotulagem do arquivo 'sintomas.csv', em seguida criando um arquivo chamado 'resultado_diagnosticos.csv' onde contem a frase , os sintomas identificados , a quantidade de sintomas  e o diagnostico sugerido.
- Tudo isso utilizando de métodos de analise de texto da ontologia para identificar palavras.     

### 📊 Parte 2 - Classificador Básico de texto
- Foi elaborado um arquivo CSV chamado 'frases_risco.csv' com 20 linhas onde foram rotuladas frases de sintomas com um nível de risco a saúde estimado.
- Elaboramos um código python incluido no arquivo 'text_transform.ipynb' que através a aplicação do metodo TF-IDF vetorizamos as palavras do arquivo 'frases_risco.csv' e em seguida treinamos 3 modelos diferentes de classificação da biblioteca Scikit-Learn (SVC , KNN, RandomForestClassifier) testando suas respectivas acuracias , recall e f1-score.

| Modelo | Acuracia |
|------|------|
| RandomForestClassifier | 0.5 |  
| SVC | 1.0 |
| KNN | 1.0 |

- Em seguida foi feita uma simulação com os 3 modelos utilizando a mesma frase , onde os todos deram um bom resultado.
- OBS: O modelo utilizando RandomForestClassifier teve um desempenho ruim para classificar sintomas de baixo risco.  



## 🚀 Próximos Passos (Fases Futuras)

Os dados levantados nesta fase servirão de base para as próximas etapas do projeto CardioIA, incluindo o desenvolvimento de modelos de Machine Learning, sistemas de Visão Computacional, integração com IoT e agentes inteligentes para diagnóstico e monitoramento.

---

## 🛠️ Tecnologias Utilizadas

pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
wfdb>=4.1.0
kagglehub>=0.2.0


---


## 📚 Referências

https://www.kaggle.com/datasets/m0hamedyousry/ptb-xl-a-large-publicly-available-ecg-dataset
