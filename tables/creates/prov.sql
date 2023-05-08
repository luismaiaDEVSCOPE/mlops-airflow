/*

USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Proveniência]
           ([CodProveniencia]
           ,[Proveniência])
     VALUES
           (<CodProveniencia, decimal(2,0),>
           ,<Proveniência, varchar(30),>)
GO

*/

CREATE TABLE [dbo].[Proveniência] (
    [CodProveniencia] decimal(2,0),
    [Proveniência] varchar(30),
);