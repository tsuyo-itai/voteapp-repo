import axios from 'axios';

// axiosのインスタンスを作成してbaseURLを設定
const axiosInstance = axios.create({
    baseURL: 'http://' + window.location.hostname + ':8000', // APIサーバーの設定 (TODO:本番環境では環境変数から読み込むように)
});

export default axiosInstance;