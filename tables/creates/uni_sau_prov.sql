/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Unidade Saúde Proveniência]
           ([Código Unidade Proveniência]
           ,[Unidade Proveniência]
           ,[Tipo Unidade Proveniência])
     VALUES
           (<Código Unidade Proveniência, decimal(7,0),>
           ,<Unidade Proveniência, varchar(50),>
           ,<Tipo Unidade Proveniência, varchar(1),>)
GO

*/

CREATE TABLE [dbo].[Unidade Saúde Proveniência](
    [Código Unidade Proveniência] decimal(7,0),
    [Unidade Proveniência] varchar(50),
    [Tipo Unidade Proveniência] varchar(1),
);