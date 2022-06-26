from random import randint
from requests import get
import database, uvicorn

from time import sleep
from fastapi import FastAPI
from threading import Thread

app = FastAPI()
    
@app.get("/api/v1/ver_phone")
async def start_verification_phone(phone):
    
    user:database.Users = database.Users.select().where((database.Users.phone == phone)).first()
    
    
    
    if ((not user) and (len(phone) == 12) and phone.startswith("+")):
        a = database.Ver_SMS.select().order_by(-database.Ver_SMS.id).first()
        
        if a: a = a.id + 1
        else: a = 1
        
        new_sms_code = database.Ver_SMS.create(id = a, code = randint(100000, 999999), for_phone=phone[1:])
        new_sms_code.save()
        
        
        return {"success": True, "code": new_sms_code.code}
    
    else:
        return {"success": False, "message": "User not registered"}
    

@app.get("/api/v1/get_info")
async def Get_User_Info():
    return {"info": "Okey"}



if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host='5.23.55.230', reload=True)