<script setup>
import { ref, inject, onMounted, computed } from 'vue';
import CryptoJS from 'crypto-js';
const axios = inject('axios')
import { useRoute } from 'vue-router';

// Vue Routerのルート情報を取得
const route = useRoute();

// TODO: 環境変数へ
const secretKey = 'mysecretkey';


// const randomToken = route.params.random_token
const randomToken = route.params.random_token;
const currentUrl = 'http://' + window.location.hostname + ':' + window.location.port + route.fullPath

const PollChoice = ref([])

// 暗号化文字列の復号化
function decryptSafeEncryptedText(safeEncryptedText) {
    console.log(safeEncryptedText)
    // 1. '_' を '/' に戻す
    const base64CipherText = safeEncryptedText.replace(/_/g, '/'); // 例: '_' を '/' に戻す
    // 2. Base64デコード
    const cipherText = atob(base64CipherText);
    // 3. 暗号文を復号化
    const bytes = CryptoJS.AES.decrypt(cipherText, secretKey);
    const originalText = bytes.toString(CryptoJS.enc.Utf8);

    return originalText;
}

function getPollChoiceOne() {
    console.log(randomToken)
    const pollid = decryptSafeEncryptedText(randomToken)
    axios.get(`/api/v1/poll/${pollid}`).then((response) => {
    console.log(response.data.title);
    PollChoice.value = response.data;
    });
}

// URLをクリップボードにコピーする
function copyToClipboard() {
    // クリップボードAPIを使用してテキストをクリップボードにコピー
    navigator.clipboard.writeText(currentUrl)
    .then(() => {
        alert("URLがクリップボードにコピーされました。");
    })
    .catch(err => {
        console.error("クリップボードへのコピーに失敗しました:", err);
        alert("URLのコピーに失敗しました。");
    });
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
                <button>投票する</button>
            </div>
        </div>
        <div class="copy-url-block">
            <p>URLを共有する</p>
            <input v-on:click="copyToClipboard" :value="currentUrl" readonly />
            <button v-on:click="copyToClipboard">コピー</button>
        </div>
    </div>
</template>
