# atmarksol-training-python-2023
2023年度 作成課題 Python

## 環境構築手順  
```
$ docker-compose build　　
$ docker exec -it admin-mariadb bash
# mysql -u root -p < python2023.sql
password入力を求められるのでpasswordと入力してenter
# exit  
$ docker-compose up -d
```
