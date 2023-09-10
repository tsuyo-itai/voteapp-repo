import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios';


const app = createApp(App);
// axiosのインスタンスを作成してbaseURLを設定
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', // APIサーバーの設定 (TODO:本番環境では環境変数から読み込むように)
});

app.use(VueAxios, axiosInstance);
app.mount('#app')
