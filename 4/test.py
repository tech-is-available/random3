import requests

api_key="pk.be7792e2a5bfb97297648d8d62ff47ac"
place=input("enter=")

url="https://us1.locationiq.com/v1/search"
params={"key":api_key,"q":place,"format":"json"}

r=requests.get(url,params=params).json()

if isinstance(r,list) and r:
    print("output")
    d=r[0]
    print("plce if=",d.get("place_id",""))
    print("lon=",d.get("lon",""))
    print("lat=",d.get("lat",""))
    print("displ=",d.get("display_name",""))
else:
    print("error=",r)
