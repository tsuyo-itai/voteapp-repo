<!-- ここらへん https://reffect.co.jp/vue/vue-js-input-v-model/-->
<!-- TODO 作成時にAPIを3回発行するのは思想としていかがなものか.. -->
<script setup>
import axios from 'axios';
import { ref } from 'vue';

const pollTitle = ref('');
const pollDescription = ref('');

const choiceNameA = ref('');
const choiceDescriptionA = ref('');
const choiceNameB = ref('');
const choiceDescriptionB = ref('');

// MainView.jsで定義したものとは別物
// TODO: 後々他のVueファイルもCompositionAPIの形式で書き直す
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', // APIサーバーの設定 (TODO:本番環境では環境変数から読み込むように)
});

// 投票タイトル・詳細をpostする
async function sendPollContents(choiceId1, choiceId2) {
    try {
        const response = await axiosInstance.post("/api/v1/polls", {
            title: pollTitle.value,
            description: pollDescription.value,
            choice_ids: [choiceId1, choiceId2],
        })
        console.log(response.data);
    } catch (error){
        // TODO: エラーハンドリングをしっかりしよう
        console.error(error);
    }
}

// 選択肢をpostする
async function sendChoiceContents(name, description) {
    try {
        const response = await axiosInstance.post("/api/v1/choices", {
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

    sendPollContents(choiceId1, choiceId2)

    window.location.replace('/Poll');
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

