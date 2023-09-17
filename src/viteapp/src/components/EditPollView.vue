<!-- ここらへん https://reffect.co.jp/vue/vue-js-input-v-model/-->
<script setup>
import { ref } from 'vue';

const pollTitle = ref('');
const pollDescription = ref('');

const choiceNameA = ref('');
const choiceNameB = ref('');

</script>
<template>
  <h1>投票作成</h1>

    <div class="card-poll-edit">
        <h2>要素</h2>
        <div class="card-poll-inputblock">
            <h3>投票タイトル</h3>
            <input class="poll-input" v-model="pollTitle" />
        </div>
        <div class="card-poll-inputblock">
            <h3>投票内容詳細</h3>
            <input class="poll-input" v-model="pollDescription" />
        </div>
        <div class="card-poll-inputblock">
            <h3>A (名前)</h3>
            <input class="poll-input" v-model="choiceNameA" />
        </div>
        <div class="card-poll-inputblock">
            <h3>B (名前)</h3>
            <input class="poll-input" v-model="choiceNameB" />
        </div>
    </div>


</template>

