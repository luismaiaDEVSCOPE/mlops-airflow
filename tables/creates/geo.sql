/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Geografia]
           ([GeografiaSKey]
           ,[CodDistrito]
           ,[Distirito]
           ,[CodConcelho]
           ,[Concelho]
           ,[CodFreguesia]
           ,[Freguesia]
           ,[Freguesia Geo]
           ,[Concelho Geo]
           ,[Distrito Geo])
     VALUES
           (<GeografiaSKey, numeric(18,0),>
           ,<CodDistrito, decimal(2,0),>
           ,<Distirito, varchar(30),>
           ,<CodConcelho, decimal(2,0),>
           ,<Concelho, varchar(30),>
           ,<CodFreguesia, decimal(2,0),>
           ,<Freguesia, varchar(30),>
           ,<Freguesia Geo, varchar(101),>
           ,<Concelho Geo, varchar(70),>
           ,<Distrito Geo, varchar(39),>)
GO
*/

CREATE TABLE [dbo].[Geografia](
    [GeografiaSKey] numeric(18,0),
    [CodDistrito] decimal(2,0),
    [Distirito] varchar(30),
    [CodConcelho] decimal(2,0),
    [Concelho] varchar(30),
    [CodFreguesia] decimal(2,0),
    [Freguesia] varchar(30),
    [Freguesia Geo] varchar(101),
    [Concelho Geo] varchar(70),
    [Distrito Geo] varchar(39),
);
