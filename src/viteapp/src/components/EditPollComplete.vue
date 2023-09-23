<template>
  <h1>投票作成完了</h1>
    <h3>投票タイトル</h3>
    <h3>投票内容詳細</h3>
    <div class="card-choice choice-first">
      <h3>A (名前)</h3>
      <h3>A (詳細)</h3>
    </div>
    <div class="card-choice choice-second">
      <h3>B (名前)</h3>
      <h3>B (詳細)</h3>
    </div>
    <!-- 追加部分: URL表示とコピー機能 -->
    <div class="copy-url-section">
      <input type="text" v-model="currentUrl" readonly>
      <button @click="copyToClipboard">URLをコピー</button>
    </div>
    <!-- 追加部分: SNSシェアリンク -->
    <div class="social-share-section">
      <a :href="twitterShareLink" target="_blank">Twitterでシェア</a>
      <a :href="facebookShareLink" target="_blank">Facebookでシェア</a>
      <a :href="lineShareLink" target="_blank">LINEでシェア</a>
    </div>
</template>

<script>
export default {
  data() {
    return {
      currentUrl: window.location.href
    }
  },
  computed: {
    twitterShareLink() {
      const text = encodeURIComponent("投票に参加してください！");  // シェア時のテキスト
      return `https://twitter.com/intent/tweet?text=${text}&url=${encodeURIComponent(this.currentUrl)}`;
    },
    facebookShareLink() {
      return `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(this.currentUrl)}`;
    },
    lineShareLink() {
      const text = encodeURIComponent("投票に参加してください！");  // シェア時のテキスト
      return `https://line.me/R/msg/text/?${text}%20${encodeURIComponent(this.currentUrl)}`;
    }
  },
  methods: {
    async copyToClipboard() {
      // ... 省略 ...
    }
  }
}
</script>

<style>
/* 必要に応じてスタイルを追加 */
.copy-url-section, .social-share-section {
  margin-bottom: 20px;
}
</style>