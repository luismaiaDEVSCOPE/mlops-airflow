/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Unidade Saúde Destino]
           ([Código Unidade Destino]
           ,[Unidade Destino]
           ,[Tipo Unidade Destino])
     VALUES
           (<Código Unidade Destino, decimal(7,0),>
           ,<Unidade Destino, varchar(50),>
           ,<Tipo Unidade Destino, varchar(1),>)
GO
*/

CREATE TABLE [dbo].[Unidade Saúde Destino](
    [Código Unidade Destino] decimal(7,0),
    [Unidade Destino] varchar(50),
    [Tipo Unidade Destino] varchar(1),
);