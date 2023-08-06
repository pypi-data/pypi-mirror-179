# pynut - Laurent Tupin

It provides various functions to simplify the users life. 


## Installation

You can install the package from [PyPI](https://pypi.org/project/pynut-Email/):

    python -m pip install pynut-Email

The package is supported on Python 3.7 and above.



## How to use


You can call a function as this example:

    $ ----------------------------------------------------
    >>> from pyNutTools import nutDate
    >>> nutDate.today()



This is the libraries I am using with the package

    $ ----------------------------------------------------
    >>> exchangelib==4.7.2
    


## Documentation


Temporary documentation for nutEmail :

    DESIGN PATTERN: BUILDER for OUTLOOK / EXCHANGELIB
    Allow you to manage all relating to Emails with few lines of code
    
    from pyNut import nutEmail as email
    
    1. Send an email with OUTLOOK
    
    o_builder_emailSend =   email.c_Outlook_send(**dic_param)
    o_otlk_Director =       email.c_otlk_Director(o_builder_emailSend)
    o_otlk_Director.SendMail()
    bl_success = o_otlk_Director._builder.bl_success
        OR
    bl_success = email.fBl_SendMail_desPatt(**dic_param)
    
    WHERE 
    
    dic_param = dict(bl_draft = True, l_pathAttach=['path1_fileToEnclose'], str_message = 'Hello',
                     str_from='', str_to='', str_cc='', str_bcc='',str_subject='Subject')    
    
    2. Download files from Received Email on Outlook
    
    o_builder_emailDwld =   email.c_Outlook_dwld(**dic_param)
    inst_Director =    email.c_otlk_Director(o_builder_emailDwld)
    inst_Director.Download_fMail()
    
    WHERE 
    
    dic_param = dict(str_outAcctName = 'laurent@gmail.com', str_inbox = 'Inbox', l_folders = [],
                     str_subject = 'Sujet', str_to = '', str_cc = '', str_folder = 'PathForSaveFile',
                     str_File_startW = 'file_', str_File_endW = '_01.csv')
    
    3. Download files from Received Email with Excahngelib (not on Outlook)
    
    o_builder_emailDwld = 	email.c_Webmail_dwld(**dic_param)
    inst_Director =  	    email.c_otlk_Director(o_builder_emailDwld)
    inst_Director.Download_fMail()
    
    WHERE 
    
    dic_param = dict(str_outAcctName = 'laurent@gmail.com', str_pwd = '*****', str_inbox = 'Inbox', l_folders = [],
                     str_subject = 'Sujet', str_to = '', str_cc = '', str_folder = 'PathForSaveFile',
                     str_File_startW = 'file_', str_File_endW = '_01.csv')
    

***END***