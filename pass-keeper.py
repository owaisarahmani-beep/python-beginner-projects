import json

website=input("Website: ")
username=input("Username: ")
password=input("Password: ")


password={
"website_name":website,
"username":username,
"password":password,

}
print(password)
with open("D:/python/projects/pyth.json","r") as f:
      data= json.load(f)
      data.append(password)
with open("D:/python/projects/pyth.json","w") as f:
      json.dump(data,f)
