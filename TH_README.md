
# PyPageSummarizer
ไลบรารี Python สำหรับการสรุปเนื้อหาจากเว็บไซต์โดยใช้โมเดล Google T5 
## ฟีเจอร์
- สามารถดึงเนื้อหาหรือบทความจากเว็บไซต์
- สามารถสรุปเนื้อหาที่ถูกดึงจากเว็บไซต์


## ไลบรารีที่ใช้

 - [Requests](https://pypi.org/project/requests/)
 - [Trafilatura](https://pypi.org/project/trafilatura/)
 - [Transformers](https://pypi.org/project/transformers/)
 - [PyTorch](https://pypi.org/project/torch/)


## ใช้เวอร์ชัน Prerelease

ดาวน์โหลด main.py จาก repository นี้และติดตั้งไลบรารี Python ดังต่อไปนี้.

```bash
  pip install requests
  pip install trafilatura
  pip install transformers
  pip install torch
```
และสามารถรั

    
## ฟังค์ชั่น
1.ดึงเนื้อหาหรือบทความจากเว็บไซต์
```bash
maincontent(url)
```
URL - String.
\
\
2.สามารถสรุปเนื้อหาที่ถูกดึงจากเว็บไซต์
```bash
summarize(url,maxlength,minlength)
```
url - String.\
maxlength - Integer.\
minlength - Integer.
## ใบอนุญาต

[MIT](https://choosealicense.com/licenses/mit/)


## ผู้เขียน

- [@sorawithwetubon](https://github.com/sorawithwetubon)

