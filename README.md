# 投票アプリ (サービス名は未定)

## Docker環境構築手順

`docker-compose.yml`と同階層で実行する

### ビルド

```bash
docker-compose build

# キャシュを使用せずビルド (本番前環境作成時など)
docker-compose build --no-cache
```

### 起動

```bash
docker-compose up

# バックグラウンド起動
docker-compose up -d
```

[http://localhost:8000/](http://localhost:8000/)で環境へアクセス可能

#### vite環境を立ち上げる場合

事前にローカルの環境で`npm install`を行っておくか以下のコマンドでdocker環境内に`npm install`を反映させておく

```bash
docker-compose exec frontend npm install
```

viteの起動

```bash
docker-compose exec frontend npm run dev
```

[http://localhost:5173/](http://localhost:5173/)でvite環境へアクセス可能


### コンテナ環境へのログイン

コンテナ環境内に入る必要があれば

```bash
# python(fastapi)環境
docker-compose exec webapi /bin/bash

# vue(vite)環境
docker-compose exec frontend /bin/bash

```
