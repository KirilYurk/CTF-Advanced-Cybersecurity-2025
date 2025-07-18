<p align="center">
  <img src="/.img/Screenshot_1.png" alt="image" width="640" height="360" />
</p>

# 🧩 Дебютний шифр (Debut Cipher)
## **Категорія:** Cryptography  
## **Складність:** Easy

---

### **Опис завдання:**  
Студент першого курсу, надихнувшись лекціями з криптографії, вирішив створити власне зашифроване повідомлення.  
У кожному, навіть найпростішому шифрі, може ховатися щось цікаве...

---
### **Файли**
```debut.txt```
### **Розв'язання:**  
```debut.txt```
```PVTWC3DGL54WQ4DBOJTW65DQPFZGG63GORRWC===```
1. Побачивши рядок, визначаємо, що його структура схожа на ```base32.```

   Виконуємо декодування (наприклад, за допомогою [CyberChef](https://gchq.github.io/CyberChef/))
<p align="center">
  <img width="896" height="205" alt="image" src=".img/Screenshot_1.png" />
</p>

2. Отриманий рядок виглядає віддзеркаленим, повернемо йому початковий вигляд.

<p align="center">
  <img width="898" height="254" alt="image" src=".img/Screenshot_2.png" />
</p>

---
#### **Flag:** ```actf{cryptography_flag}```  
