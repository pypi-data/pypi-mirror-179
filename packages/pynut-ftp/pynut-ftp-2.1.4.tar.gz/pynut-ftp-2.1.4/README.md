# pynut - Laurent Tupin

It provides various functions to simplify the users life. 


## Installation

You can install the package from [PyPI](https://pypi.org/project/pynut-ftp/):

    python -m pip install pynut-ftp

The package is supported on Python 3.7 and above.



## How to use


You can call a function as this example:

    $ ----------------------------------------------------
    >>> from pyNutTools import nutDate
    >>> nutDate.today()



This is the libraries I am using with the package

    $ ----------------------------------------------------
    >>> paramiko==2.11.0
    


## Documentation


Temporary documentation for nutFtp :

    Class c_FTP and c_SFTP allow you to Download / Upload on a server
    Decorated to be a singleton as to keep the same instance / connection
    FTP uses the ftplib library, SFTP paramiko
    
    from pyNutFtp import nutFtp as ftp
    
    1.1. Download FTP
    
    ftp.fBl_ftpDownFileBinary(host, uid, pwd, ['FTP Folder'], fileName, folderToSave, bl_ssl = False)
        OR
    _ftp = ftp.ftp_prep(host, uid, pwd, ['FTP Folder'], bl_ssl = False)
    _ftp.ftp_DownloadFile(fileName, folderToSave)
    
    1.2. Download SFTP
    
    ftp.ssh_downFile(host, uid, pwd, ['FTP Folder'], fileName, folderToSave, int_port = 10022)
        OR
    _sftp = sftp_prep(host, uid, pwd, ['FTP Folder'], int_timeout = -1, int_port = 10022)
    _sftp.sftp_DownloadFile(fileName, folderToSave)
    
    2.1 Upload FTP
    
    ftp.fBl_ftpUpFile_Bi(host, uid, pwd, ['FTP Folder'], fileName, folderToSave,  bl_ssl = False)
        OR
    _ftp = ftp_prep(host, uid, pwd, ['FTP Folder'], bl_ssl = False)
    _ftp.ftp_UploadFile(fileName, folderToSave)
    
    2.2 Upload SFTP
    
    bl_success = ftp.ssh_upFile(host, uid, pwd, ['FTP Folder'], fileName, folderToSave, int_port = 10022)
        OR
    _sftp = sftp_prep(host, uid, pwd, ['FTP Folder'], int_port = 10022)
    _sftp.sftp_UploadFile(fileName, folderToSave)
    
    



***END***