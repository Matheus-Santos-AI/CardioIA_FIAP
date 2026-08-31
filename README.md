# ❤️ CardioIA — Fase 1: Batimentos de Dados

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

| Nome | RM | Turma |
|------|----|-------|
| Matheus Santos | _566901 | 
| _[Nome completo]_ | _[RM]_ |
| _[Nome completo]_ | _[RM]_ |

---

## 🗂️ Estrutura do Repositório

```
cardioia-fase1/
│
├── README.md                  
├── docs/                      
│   ├── texto1.txt
│   └── texto2.txt
├── assets/                    
│    
└── dataset/                   
    └── df_dados.csv
```

---

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
| `docs/texto1.txt` | _[Título do texto]_ | _[SciELO / BVS / SUS / Projeto Gutenberg / outra]_ |
| `docs/texto2.txt` | _[Título do texto]_ | _[SciELO / BVS / SUS / Projeto Gutenberg / outra]_ |

### Aplicações de NLP
_[Explique como esses textos podem ser explorados por algoritmos de Processamento de Linguagem Natural. Exemplos de análises possíveis:]_

- **Análise de sentimentos:** identificar tom emocional em relatos de pacientes ou artigos sobre a doença;
- **Extração de sintomas (NER — Named Entity Recognition):** identificar automaticamente menções a sintomas, medicamentos e condições clínicas no texto;
- **Classificação de tópicos:** categorizar textos por tema (prevenção, tratamento, diagnóstico, etc.);
- **Sumarização automática:** gerar resumos de artigos extensos para consulta rápida por profissionais de saúde.


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
