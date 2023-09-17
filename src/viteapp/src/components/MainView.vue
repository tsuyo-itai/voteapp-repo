
<template>
  <h1>今話題の投票</h1>

  <div class="card-poll-list" v-for="poll in debugPollList" :key="poll.id">
    <div class="card-content-poll-list">
      <h2>{{ poll.title }}</h2>
      <!-- TODO 選択肢が複数ある場合の対応 (現状は2つまでの仕様にする) -->
      <div class="card-content-wrapper-poll-list">
        <p class="bold">{{ poll.choices[0].name }}</p>
        <p>{{ poll.choices[0].count }}</p>
        <!-- 投票率バー -->
        <div class="pollbar-container">
          <div class="pollbar-segment-1" :style="{ width: computedWidth(poll.choices[0].count, poll.choices[1].count) + '%' }"></div>
          <div class="pollbar-segment-2" :style="{ width: computedWidth(poll.choices[1].count, poll.choices[0].count) + '%' }"></div>
        </div>
        <p>{{ poll.choices[1].count }}</p>
        <p class="bold">{{ poll.choices[1].name }}</p>
      </div>
    </div>
  </div>

</template>


<script>
  export default {
    data() {
        return {
            apiPollChoiceList:[],
            debugPollList: [
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
        };
    },
    computed: {
      computedWidth() {
        return (value1, value2) => {
          const total = value1 + value2;
          if (total === 0) {
            return 0; // 投票がない場合は0%
          }
          const percentage = (value1 / total) * 100; // value1の割合を計算
          return percentage; // パーセンテージ
        };
      },
    },
    methods: {
      // 投票一覧を取得する
      getPollChoiceList() {
        this.axios.get("/api/v1/pollchoices").then((response) => {
          console.log(response.data);
          this.apiPollChoiceList = response.data;
        });
      },
      // ２つの値から割合を算出
      calcPercent(value, total){
        return (value / total) * 100;
      }
    },
    mounted() {
      this.getPollChoiceList();
    }
  }

</script>
