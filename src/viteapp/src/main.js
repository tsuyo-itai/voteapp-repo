import { createApp } from 'vue'
import './style.css'
import './scss/style.scss'
import App from './App.vue'
import MainView from './components/MainView.vue'
import EditPollView from './components/EditPollView.vue'
import EditPollCompleteView from './components/EditPollComplete.vue'
import PollView from './components/PollView.vue'
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import VueAxios from 'vue-axios';


const app = createApp(App);
// axiosのインスタンスを作成してbaseURLを設定
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', // APIサーバーの設定 (TODO:本番環境では環境変数から読み込むように)
});

// routerのインスタンスを作成してパスを設定
const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', name: "root", component: MainView },
      { path: '/editPoll', name: "editPoll", component: EditPollView },
      { path: '/editPollComplete', name: "editPollComplete", component: EditPollCompleteView },
      { path: '/Poll', name: "Poll", component: PollView }, //TODO パスはオリジナルURLとする 一旦適当に作成
    ],
});

app.use(router);
app.use(VueAxios, axiosInstance);
app.mount('#app')
