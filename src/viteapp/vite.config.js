import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0', // ここにホスト名を指定
  },
  plugins: [vue()],

  css: {
    // 開発モードでソースマップを生成する
    devSourcemap: true,
    // 本番ビルド時にCSSを最適化
    // minify: true,
  }
})


