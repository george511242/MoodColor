<!-- src/components/DataTable.vue -->
<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :search="search"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
export default {
  name: "DataTable",
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    search: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
:deep(.v-data-table__th) {
  background-color: #f5f5f5 !important; /* 設置為灰色 */
}
</style>
