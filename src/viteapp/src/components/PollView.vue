<script setup>
import { ref, inject, onMounted, computed } from 'vue';
const axios = inject('axios')
import { useRoute } from 'vue-router';
import { decryptSafeEncryptedText, copyToClipboard } from '../utils/function'

// Vue Routerのルート情報を取得
const route = useRoute();
const router = inject('router')

// const randomToken = route.params.random_token
const randomToken = route.params.random_token;
const currentUrl = 'http://' + window.location.hostname + ':' + window.location.port + route.fullPath

const PollChoice = ref([])

function getPollChoiceOne() {
    console.log(randomToken)
    const pollid = decryptSafeEncryptedText(randomToken)
    axios.get(`/api/v1/poll/${pollid}`).then((response) => {
    console.log(response.data.title);
    PollChoice.value = response.data;
    });
}

function updateChoiceCount(choice_id) {
    axios.put(`/api/v1/choices/${choice_id}/increase`).then((response) => {
    console.log(response.data);
    });

    router.go(route.path)
}

onMounted(() => { getPollChoiceOne()
    console.log(PollChoice)

});

</script>

<template>
    <h2>投票作成が完了しました画面</h2>
    <div class="card-poll-view">
        <h2>{{ PollChoice.title }}</h2>
        <h3>{{ PollChoice.description }}</h3>
        <div class="choices-container">
            <div class="one-choice-container" v-for="(choice, index) in PollChoice.choices" :key="choice.id" :class="{ 'first-choice-block': index === 0, 'second-choice-block': index === 1 }">
                <h4>{{ choice.name }}</h4>
                <p>{{ choice.description }}</p>
                <p>{{ choice.count }}</p>
                <button v-on:click="updateChoiceCount(choice.id)">投票する</button>
            </div>
        </div>
        <div class="copy-url-block">
            <p>URLを共有する</p>
            <input v-on:click="copyToClipboard(currentUrl)" :value="currentUrl" readonly />
            <button v-on:click="copyToClipboard(currentUrl)">コピー</button>
        </div>
    </div>
</template>
