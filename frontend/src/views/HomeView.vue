<template>
  <ToolBar />
  <HelloWorld />
</template>

<script>
import { defineComponent } from "vue";
import ToolBar from "../components/ToolBar.vue";

import HelloWorld from "../components/HelloWorld.vue";

export default defineComponent({
  name: "HomeView",

  components: {
    HelloWorld,
    ToolBar,
  },
});
</script>
