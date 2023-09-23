import { createApp } from 'vue'
import './style.css'
import './scss/style.scss'
import App from './App.vue'
import VueAxios from 'vue-axios';
import axiosInstance from "./axios/index"
import router from "./router/index"

const app = createApp(App);

console.log(app.config.globalProperties)

app.use(router);
app.use(VueAxios, axiosInstance);
// 外部から触れるように
app.provide('axios', app.config.globalProperties.axios)
app.provide('router', app.config.globalProperties.$router)
app.mount('#app')