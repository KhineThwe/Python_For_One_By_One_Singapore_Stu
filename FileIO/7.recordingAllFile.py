"""
onlinedb = {0:{"email":"khine@gmail.com","u_name":"khine","password":"upass","phone":"09792372847","age":100},
           1:{"email":"zar@gmail.com","u_name":"zar","password":"upass","phone":"09792372848","age":100},
           2:{"email":"thwe@gmail.com","u_name":"thwe","password":"upass","phone":"09792372845","age":100},
           3:{"email":"online@gmail.com","u_name":"online","password":"upass","phone":"09792372846","age":100}}
"""

onlinedb = {0:{"email":"khine@gmail.com","u_name":"khine","password":"upass","phone":"09792372847","age":100},
           1:{"email":"zar@gmail.com","u_name":"zar","password":"upass","phone":"09792372848","age":100},
           2:{"email":"thwe@gmail.com","u_name":"thwe","password":"upass","phone":"09792372845","age":100},
           3:{"email":"online@gmail.com","u_name":"online","password":"upass","phone":"09792372846","age":100}}
def recording_all_data():
    with open("onlinedb.txt","w") as dbfile:
       for i in range(len(onlinedb)):
           email = onlinedb[i]["email"]
           user_name = onlinedb[i]["u_name"]
           password = onlinedb[i]["password"]
           phone = onlinedb[i]["phone"]
           age = onlinedb[i]["age"]
           total_user_data = str(i) + ' ' + email + ' '+user_name + ' '+password+' '+str(phone)+' '+str(age)+'\n'

           dbfile.write(total_user_data)
           print("data: ",email,user_name,password,phone,age)
           print("Recorded")

readdb = {}
def loading_data_from_file():

    with open("onlinedb.txt","r") as dbfile:
        datas = dbfile.readlines()
        for one in datas:
            oneData = one.split(" ")

            if len(oneData) >= 6:
                id = oneData[0]
                data_form = {
                    id: {"email": oneData[1], "u_name": oneData[2], "password": oneData[3],
                         "phone": oneData[4], "age": oneData[5].rstrip("\n")  # Remove the newline character
                         }
                }
                readdb.update(data_form)
    return readdb

if __name__ == '__main__':
    # recording_all_data()
    readdb = loading_data_from_file()
    print(readdb)

