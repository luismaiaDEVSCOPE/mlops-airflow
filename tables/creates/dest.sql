/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Destino]
           ([CodDestino]
           ,[Destino])
     VALUES
           (<CodDestino, decimal(2,0),>
           ,<Destino, varchar(30),>)
GO

*/

CREATE TABLE [dbo].[Destino](
    [CodDestino] decimal(2,0),
    [Destino] varchar(30),
);