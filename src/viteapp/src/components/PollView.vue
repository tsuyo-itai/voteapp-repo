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
console.log(randomToken)

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

onMounted(() => { getPollChoiceOne()
    console.log(PollChoice)

});

</script>

<template>
    <h2>投票作成が完了しました画面</h2>
    <h3>{{ PollChoice.title }}</h3>
    <h4>{{ PollChoice.description }}</h4>
</template>
