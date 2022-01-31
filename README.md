# Python mysql-data-generator 工具使用手冊
## 啟用 MySQL
1. 在本專案的根目錄執行下方指令，即可建構一個正在運行的 MySQL Server：
    ```bash
    docker-compose up -d
    ```
2. 進入 MySQL Client 的指令，因為建立時就沒有設定 password，所以不需要打 password ：
    ```bash
    docker-compose exec db mysql -uroot
    ```
    進入 test database
    ```mysql
    mysql> use test
    ```
3. (想動基礎設定再看) 如果想設定 password：將 docker-compose.yml 的 ```MYSQL_ALLOW_EMPTY_PASSWORD``` 那行註解或刪除，並將 ```MYSQL_ROOT_PASSWORD``` 的註解取消，範例如下：
    ``` YAML
    environment: 
    #  - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    - MYSQL_DATABASE=test
    - MYSQL_ROOT_PASSWORD=root
    ```
    改動後，重新建立 docker-compose：
    ```bash
    docker-compose up -d --build
    ```

## Generator Function 使用方法

### 進入 docker-compose中 的 python 執行環境
```bash
docker-compose exec app bash
```

### 建立 (CREATE) Table
在 ```models.py``` 寫好要建立的 table，格式如註解處與 ```test``` table 可以參考，並執行建立 table 的程式：
```bash
python create_table.py
```

### 刪除 (DROP) Table
執行刪除 table 的程式：
```bash
python drop_table.py
```

### 新增 (INSERT) Table
執行新增資料的程式，可以選擇要新增多少筆資料（以1萬為單位）:
```bash
python insert_data.py
```

### 截斷 (TRUNCATE) Table
執行截斷特定 table 的程式 (可以選擇截斷對象) :
```bash
python truncate.py
```

### 新增 (ADD) Index
執行對特定 table 新增 index 的程式（可以建立包含多個 column 的 index）
```bash
python add_index.py
```

### 刪除 (DROP) Index
執行刪除特定 table 的特定 index 的程式（包含一次刪除所有 index 的選項)
```bash
python drop_index.py
``` 