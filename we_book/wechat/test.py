import re
import base64


str = base64.b64decode('MzQzNWVhODdlYjZkZmUxNmJjMDdhYzJiOWIzOTdlNjZmNTNlNzFiNzp7ImlkIjoxLCJ1c2VybmFtZSI6Inl6eSIsInBhc3N3b3JkIjoiMTIzIiwidHlwZSI6dHJ1ZSwiQ2xhc3MiOjExMX0=').decode("utf-8")
print(str)
str_id = re.findall(r'id":(.*?),"',str)[0]
print(str_id)