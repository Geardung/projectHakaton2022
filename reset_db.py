
from database import *

for table in [ Controllers, Roles, Groups, Users, Ver_SMS, Rukovoditeli, Codes, Prohodi,
              Cabinets, Events, Invitations, Chats, Messages, Chats_access, Goods]:
    table:Users
    try:
        
        table:Users
        table.drop_table(cascade=True)
    except: 
        print("ERROR ERROR", table)

    
for table in [Controllers, Roles, Groups, Users, Ver_SMS, Rukovoditeli, Codes, Prohodi,
              Cabinets, Events, Invitations, Chats, Messages, Chats_access, Goods]:
    table:Users
    table.create_table() 
    
