<template>
    <v-card
      class="square-card"
      elevation="3"
    >
      <v-card-title>Your color of today</v-card-title>
      <v-card-subtitle>{{ formattedDate }}</v-card-subtitle>
      
      <v-card-text>
        <div class="circle" :style="{ backgroundColor: color }"></div>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    name: "ColorCircle",
    props: {
      date: String, // 接收從父層傳來的日期
    },
    computed: {
    formattedDate() {
        // 如果有傳入 date，就用它；否則預設為今天
        return this.date || new Date().toISOString().slice(0, 10);
    },
    },
    data() {
      return {
        color: "#f39c12",
      };
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
  }
  </style>
  