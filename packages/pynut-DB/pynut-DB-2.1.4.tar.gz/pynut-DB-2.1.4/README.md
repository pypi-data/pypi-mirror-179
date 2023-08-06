# pynut - Laurent Tupin

It provides various functions to simplify the users life. 


## Installation

You can install the package from [PyPI](https://pypi.org/project/pynut-DB/):

    python -m pip install pynut-DB

The package is supported on Python 3.7 and above.



## How to use


You can call a function as this example:

    $ ----------------------------------------------------
    >>> from pyNutTools import nutDate
    >>> nutDate.today()



This is the libraries I am using with the package

    $ ----------------------------------------------------
    >>> pyodbc==4.0.32


## Documentation


Temporary documentation for nutDb :
    
    from pyNutDB import nutDb as db
    
    1. Lite Db
    
    db_lite = db.c_db_lite(r'\db_param.db')
    db_lite.connect()
    df_UID = db_lite.getDataframe("SELECT * FROM tbl_Table")
    db_lite.closeConnection()
    """ This class allows you to manage simple lite database"""
    
    2. SQL Server (pyodbc)
    
    dbServer =  db.c_db_withLog()
    # df_UID will be a dataframe of connexion: Server, Database, UID, Password
    dbServer.dataframeCredentials(df_UID)
    
    # Request with a dataframe as a return
    db.db_SelectReq("SELECT top 10 * FROM tbl_Table")
    print(dbServer.df_result)
    
    # OR EXEC a stored procedure    
    db.db_EXEC('EXEC Stored_Procedure')
    
  
    
    
***END***