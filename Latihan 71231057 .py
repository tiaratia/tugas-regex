#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from datetime import datetime, date

teks = "Pada tanggal 1945-08-17 Indonesia merdeka.  Indonesia memiliki beberapa pahlawan nasional,  seperti Pangeran Diponegoro (TL: 1785-11-11),  Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."

tanggal_regex = r'\b(\d{4}-\d{2}-\d{2})\b'
tanggal_list = re.findall(tanggal_regex, teks)

hasil = []
for tanggal in tanggal_list:
    tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%d')
    tanggal_str = tanggal_obj.strftime('%d-%m-%Y')
    selisih_hari = (date.today() - tanggal_obj.date()).days
    hasil.append(f"{tanggal_str} 00:00:00 selisih {selisih_hari} hari")

    
for hasil_tanggal in hasil:
    print(hasil_tanggal)


# In[3]:


import re
import random
import string


teks = "Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari"


email_regex = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
email_list = re.findall(email_regex, teks)


username_list = []
for email in email_list:
    username = email.split('@')[0]
    username_list.append(username)


password_list = []
for _ in range(len(username_list)):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    password_list.append(password)

for email, username, password in zip(email_list, username_list, password_list):
    print(f"{email} username: {username}, password: {password}")


# In[ ]:




