import { createRouter, createWebHistory } from 'vue-router';
import MainView from '../components/MainView.vue'
import EditPollView from '../components/EditPollView.vue'
import PollView from '../components/PollView.vue'
import EditPollCompleteView from '../components/EditPollComplete.vue'

// routerのインスタンスを作成してパスを設定
const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', name: "root", component: MainView },
      { path: '/editPoll', name: "editPoll", component: EditPollView },
      // { path: '/Poll', name: "Poll", component: PollView }, //TODO パスはオリジナルURLとする 一旦適当に作成
      { path: "/Poll/:random_token", name: "vote", component: PollView },
      { path: '/editPollComplete', name: "editPollComplete", component: EditPollCompleteView },
    ],
});

export default router;
