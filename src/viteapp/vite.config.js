import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0', // ここにホスト名を指定
    // ホットリロード監視
    watch: {
      include: [path.resolve(__dirname, 'src/**/*')],
      exclude: ['node_modules']
    }
  },
  plugins: [vue()],

  css: {
    // 開発モードでソースマップを生成する
    devSourcemap: true,
    // 本番ビルド時にCSSを最適化
    // minify: true,
  }
})


