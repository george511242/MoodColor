const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,

  // 指定輸出目錄與 public 路徑
  publicPath: '/',
  outputDir: 'dist',

  // 避免 history 模式造成的 404 問題
  devServer: {
    historyApiFallback: true,
  },

  pluginOptions: {
    vuetify: {
      // vuetify 設定可維持不變
    },
  },
});
