<p align="center">
  <img src="/.img/Screenshot_1.png" alt="image" width="640" height="360" />
</p>

# 🧩 Ключ під килимком (Key Under the Doormat)
## **Категорія:** Cryptography  
## **Складність:** Easy

---

### **Опис завдання:**  
Під час внутрішнього аудиту було виявлено підозрілу активність на комп’ютері одного з викладачів.  
З’ясувалося, що на його пристрої діяв зловмисний процес, який перехопив файл sslkeys.log. Саме під час цієї атаки був зафіксований фрагмент трафіку між викладачем і одним із серверів університету.  
Подейкують, що у перехопленній комунікації приховано дещо важливе.

---
### **Файли**
```net_dump.pcapng```
```sslkeys.log```

### **Розв'язання:**
1. Після завантаження відкриваємо дамп трафіку та бачимо, що маємо зашифровані потоки.  
  <p align="center">
    <img width="1915" height="1092" alt="Picture1" src=".img/Screenshot_1.png" />
  </p>  
  
2. Оберемо пункт **Edit → Preferences → Protocols → TLS** та в полі **(PRE)-Master-Secret log filename** вкажемо наш `sslkeys.log`.
  <p align="center">
    <img width="528" height="394" alt="image" src=".img/Screenshot_2.png" />
  </p>

3. Натиснемо **OK** - отримаємо розшифрований трафік
   <p align="center">
     <img width="1606" height="827" alt="image" src=".img/Screenshot_3.png" />
  </p>

4. Оберемо **GET-запит до index.html** та натиснемо **Follow HTTP stream**.
  <p align="center">
    <img width="473" height="362" alt="image" src=".img/Screenshot_4.png" />
  </p>

---
#### **Flag:** ```actf{cryptography_flag}```  
