<template>
  <v-card class="square-card" elevation="3">
    <v-card-title>Your color of today</v-card-title>
    <v-card-subtitle>{{ formattedDate }}</v-card-subtitle>

    <v-card-text>
      <div class="circle" :style="{ backgroundColor: computedColor }"></div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "ColorCircle",
  props: {
    date: String, // 傳進來的日期
    color: String, // 新增：傳進來的顏色
  },
  computed: {
    formattedDate() {
      return this.date || new Date().toISOString().slice(0, 10);
    },
    computedColor() {
      // 如果父層有傳顏色，優先使用；否則預設顏色
      return this.color && this.color.trim() !== "" ? this.color : "#f39c12";
    },
  },
};
</script>

<style scoped>
.square-card {
  width: 250px;
  height: 250px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.circle {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  margin-top: 8px;
  margin-left: auto;
  margin-right: auto;
  transition: background-color 0.3s;
  border: 1px solid black;
}
</style>
