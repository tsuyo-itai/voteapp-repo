<script setup>
import { ref, inject, onMounted, computed } from 'vue';
import { createSafeEncryptedText } from '../utils/function'

const axios = inject('axios')
const router = inject('router')

const allPollChoiceList = ref([])
const debugPollList = [
            {
                "id": "6506364fc0e085863e8eeb72",
                "title": "全日本エチエチ大会",
                "description": "エロい女を決めよう",
                "choice_ids": [
                "650635eac0e085863e8eeb70",
                "65063607c0e085863e8eeb71"
                ],
                "choices": [
                {
                    "id": "650635eac0e085863e8eeb70",
                    "name": "hogeA",
                    "description": "hogehogehogehoge ok!!",
                    "image_file": "",
                    "count": 12
                },
                {
                    "id": "65063607c0e085863e8eeb71",
                    "name": "hugaB",
                    "description": "hugahugahuga ok!!",
                    "image_file": "",
                    "count": 47
                }
                ]
            },
            {
                "id": "650636d9c0e085863e8eeb72",
                "title": "大分大学ミスコン",
                "description": "あああ",
                "choice_ids": [
                "650635eac02015863e8eeb70",
                "65063607988085863e8eeb71"
                ],
                "choices": [
                {
                    "id": "650635eac02015863e8eeb70",
                    "name": "斎藤あかり",
                    "description": "hogehogehogehoge ok!!",
                    "image_file": "",
                    "count": 108
                },
                {
                    "id": "65063607988085863e8eeb71",
                    "name": "佐藤栞",
                    "description": "hugahugahuga ok!!",
                    "image_file": "",
                    "count": 120
                }
                ]
            },
            {
                "id": "6506363820e085863e8eeb72",
                "title": "でっかいメロン",
                "description": "うん",
                "choice_ids": [
                "65063102c0e085863e8eeb70",
                "65063607c03335863e8eeb71"
                ],
                "choices": [
                {
                    "id": "65063102c0e085863e8eeb70",
                    "name": "ああああ",
                    "description": "hogehogehogehoge ok!!",
                    "image_file": "",
                    "count": 3290
                },
                {
                    "id": "65063607c03335863e8eeb71",
                    "name": "すごいいね",
                    "description": "hugahugahuga ok!!",
                    "image_file": "",
                    "count": 880
                }
                ]
            }
        ]

function calcCssWidthPercent(value1, value2) {
    const total = value1 + value2;
    if (total === 0) {
        return 0; // 投票がない場合は0%
    }

    const percentage = (value1 / total) * 100; // value1の割合を計算

    return percentage; // パーセンテージ
}

// 投票一覧を取得する
function getPollChoiceList() {
    axios.get('/api/v1/pollchoices').then((response) => {
    console.log(response.data);
    allPollChoiceList.value = response.data
    });
}

// 投票ページへ遷移する
function pollPageJump(pollId) {
    // 投票idを暗号化した文字列をURLに使用
    const url_suffix = createSafeEncryptedText(pollId)
    
    router.push(`/Poll/${url_suffix}`)
}

onMounted(() => { getPollChoiceList() });

</script>

<template>
  <h1>今話題の投票</h1>

  <div v-if="allPollChoiceList.length > 0">
    <!-- 投票情報リスト -->
    <div class="card-poll-list" v-for="poll in allPollChoiceList" :key="poll.id">
      <div v-on:click="pollPageJump(poll.id)" class="card-content-poll-list">
        <h2>{{ poll.title }}</h2>
        <!-- TODO 選択肢が複数ある場合の対応 (現状は2つまでの仕様にする) -->
        <div class="card-content-wrapper-poll-list">
          <p class="bold">{{ poll.choices[0].name }}</p>
          <p>{{ poll.choices[0].count }}</p>
          <!-- 投票率バー -->
          <div class="pollbar-container">
            <div class="pollbar-segment-1" :style="{ width: calcCssWidthPercent(poll.choices[0].count, poll.choices[1].count) + '%' }"></div>
            <div class="pollbar-segment-2" :style="{ width: calcCssWidthPercent(poll.choices[1].count, poll.choices[0].count) + '%' }"></div>
          </div>
          <p>{{ poll.choices[1].count }}</p>
          <p class="bold">{{ poll.choices[1].name }}</p>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="poll-not-found">
    <h2>作成された投票がありません</h2>
  </div>

</template>