<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <h3>【TEST】APIサーバーのルートから受け取ったメッセージ: {{ apiMessage }}</h3>

  <button v-on:click="postTestModel">Create TestModel</button>

  <p v-if="createTestModelId !== ''">id: {{ createTestModelId }} を作成しました</p>


  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<script>
  export default {
    data() {
        return {
            apiMessage: '',
            createTestModelId: '',
        };
    },
    methods: {
      // APIサーバーのルートからのメッセージを受け取る
      getRootMessage() {
        this.axios.get("/").then((response) => {
          console.log(response.data);
          this.apiMessage = response.data["Message"];
        });
      },
      postTestModel() {
        this.axios.post("/api/test", {
          title: 'vite post',
          description: 'create test document from vite'
        })
        .then((response) => {
          console.log(response.data);
          this.createTestModelId = response.data["id"]
        })
      }
    },
    mounted() {
      this.getRootMessage();
    }
  }

</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
