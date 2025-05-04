<template>
  <div id="calendar"></div>
</template>

<script>
import { onMounted } from "vue";
import { Calendar } from "vanilla-calendar-pro";

// 你可以選擇性的引入不同的樣式
import "vanilla-calendar-pro/styles/index.css";
// import 'vanilla-calendar-pro/styles/layout.css'
// import 'vanilla-calendar-pro/styles/themes/light.css'
// import 'vanilla-calendar-pro/styles/themes/dark.css'

export default {
  name: "CalenderView",
  setup() {
    onMounted(() => {
      const calendar = new Calendar("#calendar", {
        settings: {
          lang: "en",
          selection: {
            day: "single",
          },
        },
      });
      calendar.init();
    });
  },
};
</script>

<style scoped>
/* 可加上自訂樣式微調 */
</style>
