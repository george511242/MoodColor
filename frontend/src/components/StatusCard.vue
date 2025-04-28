<template>
  <v-card
    :class="statusClass"
    variant="tonal"
    color="black"
    style="margin: 5px 10px"
  >
    <v-card-text
      style="display: flex; align-items: center; justify-content: center"
    >
      {{ content }}
    </v-card-text>
  </v-card>
</template>

<script setup>
import { defineProps, computed } from "vue";

const props = defineProps({
  content: {
    type: String,
    required: true,
  },
});

// 直接 computed 判斷 content，完全不用 watch
const statusClass = computed(() => {
  if (props.content === "Abnormal") return "Abnormal";
  if (props.content === "On time") return "On-time";
  if (props.content === "Late") return "Late";
  if (props.content === "Warning") return "Warning";
  if (props.content === "Alert") return "Alert";
  return "";
});
</script>

<style scoped>
.v-card-text {
  padding: 0.5rem; /* 或你想要的數值 */
}
.Abnormal {
  background-color: rgba(0, 0, 0, 0.3); /* 30%透明 */
}

.On-time {
  background-color: #2c9a6c;
}

.Late {
  background-color: #fcd12a;
}
.Alert {
  background-color: #fcd12a;
}
.Warning {
  background-color: red;
}
</style>
