# Preprocessing Brainstorming #

**2_cl_dataset.ipynb** files (classificacao_1st depends on) :
- /code/data/absenteeism/segmentacao/consulta_train.parquet
- /code/data/absenteeism/segmentacao/consultamarcacao_train.parquet
- /code/data/absenteeism/Especialidade.txt -- **sql statement**
- /code/data/absenteeism/unisau.txt -- **sql statement**
- /code/data/absenteeism/segmentacao/modelacao_1/modelacao_1_train_utente_basic.parquet

**2_modelacao_1.ipynb** files (**modelacao_1_train_utente_basic.parquet** depends on) :
- /code/data/absenteeism/segmentacao/consulta_train.parquet
- /code/data/absenteeism/segmentacao/consultamarcacao_train.parquet
- /code/data/absenteeism/Utentes.txt -- **sql statement**
- /code/data/absenteeism/geografia_coord.parquet
- /code/data/absenteeism/Especialidade.txt -- **sql statement**
- /code/data/absenteeism/unisau.txt -- **sql statement**
- /code/data/absenteeism/unisaudestino.txt -- **sql statement**
- /code/data/absenteeism/proveniencia.txt -- **sql statement**
- /code/data/absenteeism/destinounidade.txt -- **sql statement**


**1_train_test_split.ipynb** writes :
- /code/data/absenteeism/segmentacao/consulta_train.parquet
- /code/data/absenteeism/segmentacao/consultamarcacao_train.parquet



dataset depends on modelacao_1_train_utente_basic and classificacao_1st