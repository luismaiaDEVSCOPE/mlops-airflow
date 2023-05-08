/*USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Utente]
           ([UtenteSkey]
           ,[GeografiaSKey]
           ,[Nº Sequencial]
           ,[Data Nascimento]
           ,[Idade Atual]
           ,[Nº Processo]
           ,[Nº Utente SNS]
           ,[Nome]
           ,[CodSexo]
           ,[Sexo]
           ,[Nacionalidade]
           ,[Morada]
           ,[Código Postal]
           ,[Telefone]
           ,[Telemóvel]
           ,[Email]
           ,[Código Unidade Saúde]
           ,[Unidade Saúde]
           ,[Médico Centro Saúde])
     VALUES
           (<UtenteSkey, numeric(18,0),>
           ,<GeografiaSKey, numeric(18,0),>
           ,<Nº Sequencial, decimal(8,0),>
           ,<Data Nascimento, datetime2(7),>
           ,<Idade Atual, int,>
           ,<Nº Processo, numeric(14,0),>
           ,<Nº Utente SNS, decimal(12,0),>
           ,<Nome, varchar(100),>
           ,<CodSexo, varchar(1),>
           ,<Sexo, varchar(50),>
           ,<Nacionalidade, varchar(30),>
           ,<Morada, varchar(200),>
           ,<Código Postal, varchar(13),>
           ,<Telefone, varchar(15),>
           ,<Telemóvel, varchar(15),>
           ,<Email, varchar(200),>
           ,<Código Unidade Saúde, decimal(7,0),>
           ,<Unidade Saúde, varchar(50),>
           ,<Médico Centro Saúde, varchar(25),>)
GO
*/
CREATE TABLE [dbo].[Utente] (
    [UtenteSkey] numeric(18,0),
    [GeografiaSKey] numeric(18,0),
    [Nº Sequencial] decimal(8,0),
    [Data Nascimento] datetime2(7),
    [Idade Atual] int,
    [Nº Processo] numeric(14,0),
    [Nº Utente SNS] decimal(12,0),
    [Nome] varchar(100),
    [CodSexo] varchar(1),
    [Sexo] varchar(50),
    [Nacionalidade] varchar(30),
    [Morada] varchar(200),
    [Código Postal] varchar(13),
    [Telefone] varchar(15),
    [Telemóvel] varchar(15),
    [Email] varchar(200),
    [Código Unidade Saúde] decimal(7,0),
    [Unidade Saúde] varchar(50),
    [Médico Centro Saúde] varchar(25),
);