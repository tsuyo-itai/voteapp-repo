<!-- ここらへん https://reffect.co.jp/vue/vue-js-input-v-model/-->
<!-- TODO 作成時にAPIを3回発行するのは思想としていかがなものか.. -->
<script setup>
import { ref, inject } from 'vue';
import CryptoJS from 'crypto-js';
const axios = inject('axios')
const router = inject('router')

const pollTitle = ref('');
const pollDescription = ref('');

const choiceNameA = ref('');
const choiceDescriptionA = ref('');
const choiceNameB = ref('');
const choiceDescriptionB = ref('');

// TODO: 環境変数へ
// 暗号化キー（16バイト、32バイト、または64バイト）
const secretKey = 'mysecretkey';

// 暗号化文字列の作成
function createSafeEncryptedText(text) {
    // 1. 文字列を暗号化
    const cipherText = CryptoJS.AES.encrypt(text, secretKey).toString();
    // 2. 暗号文をBase64エンコード
    const base64CipherText = btoa(cipherText);
    // 3. '/' を取り除く
    const safeEncryptedText = base64CipherText.replace(/\//g, '_'); // 例: '/' を '_' に置き換える

    return safeEncryptedText;
}

// 投票タイトル・詳細をpostする
async function sendPollContents(choiceId1, choiceId2) {
    try {
        const response = await axios.post("/api/v1/polls", {
            title: pollTitle.value,
            description: pollDescription.value,
            choice_ids: [choiceId1, choiceId2],
        })
        console.log(response.data);
        return response.data.id
    } catch (error){
        // TODO: エラーハンドリングをしっかりしよう
        console.error(error);
        return null; // エラーハンドリング
    }
}

// 選択肢をpostする
async function sendChoiceContents(name, description) {
    try {
        const response = await axios.post("/api/v1/choices", {
            name: name.value,
            description: description.value,
            image_file: "",
            count: 0
        });
        return response.data.id;
    } catch (error) {
        // TODO: エラーハンドリングをしっかりしよう
        console.error(error);
        return null; // エラーハンドリング
    }
}

// 投票作成処理一括を処理
async function createPoll() {
    const choiceId1 = await sendChoiceContents(choiceNameA, choiceDescriptionA)
    const choiceId2 = await sendChoiceContents(choiceNameB, choiceDescriptionB)

    const pollId = await sendPollContents(choiceId1, choiceId2)

    // 投票idを暗号化した文字列をURLに使用
    const url_suffix = createSafeEncryptedText(pollId)

    // window.location.replace(`/Poll/${url_suffix}`);
    router.push(`/Poll/${url_suffix}`)

}

</script>

<template>
  <h1>投票作成</h1>

    <div class="card-poll-edit">
        <div class="card-poll-inputblock">
            <h3>投票タイトル</h3>
            <input class="poll-content-input" v-model="pollTitle" />
        </div>
        <div class="card-poll-inputblock">
            <h3>投票内容詳細</h3>
            <input class="poll-content-input" v-model="pollDescription" />
        </div>
        <div class="card-poll-inputblock">
            <h3>A (名前)</h3>
            <input class="poll-content-input" v-model="choiceNameA" />
        </div>
        <div class="card-poll-inputblock">
            <h3>A (詳細)</h3>
            <input class="poll-content-input" v-model="choiceDescriptionA" />
        </div>
        <div class="card-poll-inputblock">
            <h3>B (名前)</h3>
            <input class="poll-content-input" v-model="choiceNameB" />
        </div>
        <div class="card-poll-inputblock">
            <h3>B (詳細)</h3>
            <input class="poll-content-input" v-model="choiceDescriptionB" />
        </div>

        <button v-on:click="createPoll()">作成</button>
    </div>

</template>

