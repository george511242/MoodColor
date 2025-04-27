<template>
  <v-card
    :class="statusClass"
    flat
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
import { computed, defineProps } from "vue";

const props = defineProps({
  content: {
    type: String,
    required: true,
  },
});

// 直接 computed 判斷 content，完全不用 watch
const statusClass = computed(() => {
  switch (props.content) {
    case "On Time":
      return "on-time";
    case "Late":
      return "late";
    case "Leave Early":
      return "leave-early";
    case "Absent":
      return "absent";
    case "Abnormal":
      return "abnormal";
    case "Day Off":
      return "day-off";
    default:
      return "";
  }
});
</script>

<style scoped>
.on-time {
  background-color: rgba(30, 154, 108, 0.3); /* 綠色 */
}

.late {
  background-color: rgba(223, 155, 8, 0.3); /* 橘黃色 */
}

.leave-early {
  background-color: rgba(255, 165, 0, 0.3); /* 淺橘色 */
}

.absent {
  background-color: rgba(255, 0, 0, 0.3); /* 紅色 */
}

.abnormal {
  background-color: rgba(96, 96, 96, 0.3); /* 灰色 */
}

.day-off {
  background-color: transparent; 
  color: #666666; 
}
</style>
