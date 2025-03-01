# SchoolFood

### 1. Создайте файл `.env`
### 2. Вставьте свой Telegram API токен в `.env`
```bash
TOKEN="YOUR_TOKEN"
```

### 3. Загрузите все библиотеки с помощью:
```bash
pip install -r requirements.txt
```

### 4. Создайте необходимые базы данных
#### 4.1 Перейдите в `backend`
```bash
cd backend
```
#### 4.2 Создайте папку `database`
```bash
mkdir database
```
#### 4.3 Запустите файл `create_db.py`

##### Для Windows
```bash
python create_dp.py
```

##### Для Linux & MacOS
```bash
python3 create_dp.py
```