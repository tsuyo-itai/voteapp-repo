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
import axiosInstance from "./axios/index"
import router from "./router/index"

const app = createApp(App);

console.log(app.config.globalProperties)
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
// 外部から触れるように
app.provide('axios', app.config.globalProperties.axios)
app.provide('router', app.config.globalProperties.$router)
app.mount('#app')
