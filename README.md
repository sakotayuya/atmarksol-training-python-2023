# atmarksol-training-python-2023
2023年度 作成課題 Python

## 環境構築手順  
```
$ docker-compose build
$ docker-compose up -d　　
$ docker exec -it admin-db bash
# mysql -u root -p < python2023.sql
password入力を求められるのでpasswordと入力してenter
# exit  
```

## 機能一覧
<table>
    <tr>
        <th width="500">ログイン画面</th>
        <th width="500">新規登録画面</th>
    </tr>
    <tr>
        <td align="center">
          <img width="250" alt="スクリーンショット (624)" src="https://github.com/sakotayuya/atmarksol-training-python-2023/assets/103469048/a6accc9c-24bc-478a-b215-43b2a2fdb4e7">
        </td>
        <td align="center">
          <img width="250" alt="スクリーンショット (625)" src="https://github.com/sakotayuya/atmarksol-training-python-2023/assets/103469048/f7cd69e8-c032-4d5b-bc8f-4824f9b0970d">
        </td>
    </tr>
    <tr>
        <td>
            メールアドレス、パスワードによる認証機能を実装
        </td>
        <td>
            新規ユーザ登録機能を実装（ログイン時はメニューバー付き）
        </td>
    </tr>
</table>  

<table>
    <tr>
        <th width="500">ユーザ一覧画面</th>
        <th width="500">ユーザ詳細画面</th>
    </tr>
    <tr>
        <td align="center">
            <img width="350" alt="スクリーンショット (627)" src="https://github.com/sakotayuya/atmarksol-training-python-2023/assets/103469048/c2b89f4e-404b-4f70-9d8e-a37a0b6f64a0">
        </td>
        <td align="center">
            <img width="350" alt="スクリーンショット (628)" src="https://github.com/sakotayuya/atmarksol-training-python-2023/assets/103469048/dd60b5ca-70da-422f-b9f0-312ab6898eca">
        </td>
    </tr>
    <tr>
        <td>
            登録ユーザの一覧をリスト形式で表示 
        </td>
        <td>
            ユーザの詳細を表示
        </td>
    </tr>
</table>  

<table>
    <tr>
        <th width="500">ユーザ編集画面</th>
    </tr>
    <tr>
        <td align="center">
            <img width="350" alt="スクリーンショット (629)" src="https://github.com/sakotayuya/atmarksol-training-python-2023/assets/103469048/e33191cf-2420-4664-a443-3f94e3742181">
        </td>
    </tr>
    <tr>
        <td>
            ユーザの編集機能を実装
        </td>
    </tr>
</table>
