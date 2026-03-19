import os
from supabase import create_client, Client

url = "https://fburyyzzewkdqxutuayl.supabase.co"
key = "sb_publishable_rRavetQ4CoLx_I29JkWOsQ_SvgyuP2u"
supabase = create_client(url, key)


response = (
    supabase.table("quotes")
    .select("text")
    .execute()
)

text_list = []
for row in response.data:
    text_list.append(row['text'])

print(text_list)