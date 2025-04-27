<template>
  <v-app>
    <SideBar>
      <v-container>
        <v-row align="center" class="text-center">
          <v-col cols="auto">
            <h3 class="ma-0">Department</h3>
          </v-col>
          <!-- Department 下拉選單 -->
          <v-col cols="12" sm="4">
            <v-select
              v-model="selectedDepartment"
              :items="departments"
              item-title="text"
              item-value="value"
              label="Department"
              placeholder="Choose Your Team"
              dense
              outlined
              @update:modelValue="updateData"
            ></v-select>
          </v-col>
        </v-row>
        <v-row align="center" class="text-center">
          <v-col cols="auto">
            <h3 class="ma-0">Date</h3>
          </v-col>
          <!-- 日期選擇 -->
          <v-col cols="12" sm="4">
            <v-text-field
              v-model="selectedDate"
              label="Select Start Date"
              type="date"
              @update:modelValue="updateData"
            />
          </v-col>
        </v-row>
        <!-- 出勤表格 -->
        <StatusTable :headers="headers" :items="items" />
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import StatusTable from "@/components/StatusTable.vue";
import { addDays, format } from "date-fns";
import { onMounted, ref } from "vue";
import SideBar from "../components/SideBar.vue";

export default {
  name: "AttendenceLog", 
  components: { SideBar, StatusTable },
  setup() {
    const headers = ref([
      { text: "Employee ID", value: "employeeId" },
      { text: "Name", value: "name" },
    ]);

    const departments = [
      { text: "All", value: "" },
      { text: "HR", value: "HR" },
      { text: "Engineering", value: "Engineering" },
      { text: "Sales", value: "Sales" },
      { text: "Marketing", value: "Marketing" },
    ];
    const selectedDepartment = ref(""); 

    const items = ref([]); // 出勤資料，之後補資料用

    const selectedDate = ref(""); // 使用者選的起始日期

    const statusOptions = [
      "On Time",
      "Late",
      "Leave Early",
      "Absent",
      "Abnormal",
      "Day Off",
    ];

    const employeeList = [
      { employeeId: "B11705043", name: "Sophie Ku", department: "HR" },
      { employeeId: "B11705044", name: "Lilian Liu", department: "HR" },
      { employeeId: "B11705045", name: "Jerry Wu", department: "Engineering" },
      { employeeId: "B11705046", name: "Hugo Wang", department: "Engineering" },
      { employeeId: "B11705047", name: "Alice Chen", department: "Sales" },
      { employeeId: "B11705048", name: "Kevin Lin", department: "Sales" },
      { employeeId: "B11705049", name: "Emma Wong", department: "Marketing" },
      { employeeId: "B11705050", name: "Michael Lee", department: "Marketing" },
      { employeeId: "B11705051", name: "Nancy Huang", department: "Marketing" },
    ];

    function randomStatus() {
      const index = Math.floor(Math.random() * statusOptions.length);
      return statusOptions[index];
    }

    function generateHeaders(baseDate) {
      headers.value = [
        { text: "Employee ID", value: "employeeId" },
        { text: "Name", value: "name" },
      ];

      // ⚡ 從 baseDate 開始，往後加 7 天
      for (let i = 0; i < 7; i++) {
        const date = addDays(baseDate, i);
        const formattedText = format(date, "MM/dd (EEE)"); // 顯示用
        const dateKey = format(date, "MM/dd"); // 資料用

        headers.value.push({
          text: formattedText,
          value: dateKey, // key 用 MM/dd，對應到 item 的資料欄位
        });
      }
    }

    function generateItems(baseDate) {
      console.log('現在選擇的部門是:', selectedDepartment.value);
      let filteredEmployees = employeeList;
      if (selectedDepartment.value) {
        filteredEmployees = employeeList.filter(
          (employee) => employee.department === selectedDepartment.value
        );
      }
      items.value = filteredEmployees.map((employee) => {
        const record = {
          employeeId: employee.employeeId,
          name: employee.name,
        };
        for (let i = 0; i < 7; i++) {
          const date = addDays(baseDate, i);
          const dateKey = format(date, "MM/dd");

          record[dateKey] = randomStatus();
        }
        return record;
      });
    }

    function updateData() {
      if (!selectedDate.value) return;
      const baseDate = new Date(selectedDate.value);
      generateHeaders(baseDate);
      generateItems(baseDate);
    }

    onMounted(() => {
      const today = new Date();
      selectedDate.value = format(today, "yyyy-MM-dd");
      selectedDepartment.value = "";
      generateHeaders(today);
      generateItems(today);
    });

    return {
      headers,
      items,
      selectedDate,
      selectedDepartment,
      departments,
      updateData,
    };
  },
};
</script>
