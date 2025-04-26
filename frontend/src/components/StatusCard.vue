<template>
  <v-card
    :class="statusClass"
    variant="tonal"
    color="black"
    style="margin: 10px"
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
  if (props.content === "On-time") return "On-time";
  if (props.content === "Late") return "Late";
  return "";
});
</script>

<style scoped>
.Abnormal {
  background-color: rgba(0, 0, 0, 0.3); /* 30%透明 */
}

.On-time {
  background-color: rgba(30, 154, 108, 0.3);
}

.Late {
  background-color: rgba(223, 155, 8, 0.3);
}
</style>
