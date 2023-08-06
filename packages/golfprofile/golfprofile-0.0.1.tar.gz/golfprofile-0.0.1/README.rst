(Golf Profile) เป็นตัวอย่างการอัพโหลด package ไปยัง pypi.org
============================================================

PyPi: https://pypi.org/project/golfprofile/

สวัสดีจ้า package นี้อธิบายโปรไฟล์ของนาย golf
และสามารถนำไปใช้กับผู้อื่นได้

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install golfprofile

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

.. code:: python

       my = Profile('loong')
       my.company = 'uncle-engineer'
       my.hobby = ['youtuber','sleeping']
       print(my.name)
       my.show_email()
       my.show_myart()
       my.show_hobby()

พัฒนาโดย: RashawatCoding
