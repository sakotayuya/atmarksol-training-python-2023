FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# Flaskアプリケーションを実行
CMD ["python3", "app.py"]