<template>
  <v-app>
    <SideBar>
      <v-container>
        <v-card title="Today Record" flat>
          <v-table>
            <thead>
              <tr>
                <th
                  v-for="header in headers"
                  :key="header.value"
                  class="text-center"
                  style="background-color: #f5f5f5"
                >
                  {{ header.text }}
                </th>
              </tr>

              <tr></tr>
            </thead>

            <tbody>
              <tr v-for="item in records" :key="item.name" class="text-center">
                <td>{{ item.date }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.ClockInTime }}</td>
                <td>{{ item.ClockOutTime }}</td>
                <td>{{ item.ClockInGate }}</td>
                <td>{{ item.ClockOutGate }}</td>
                <td>
                  <StatusCard :content="item.status" />
                </td>
              </tr>
            </tbody>
          </v-table>
        </v-card>
        <v-spacer></v-spacer>
        <v-card title="History Records" flat>
          <template v-slot:text>
            <v-text-field
              v-model="search"
              label="Search"
              prepend-inner-icon="mdi-magnify"
              variant="outlined"
              hide-details
              single-line
            ></v-text-field>
          </template>

          <!-- 使用 DataTable 組件，並傳遞資料 -->
          <DataTable
            :show-headers="headers.text"
            :items="historyRecords"
            :search="search"
          />
        </v-card>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import { ref } from "vue";
import DataTable from "../components/DataTable.vue";
import SideBar from "../components/SideBar.vue";
import StatusCard from "../components/StatusCard.vue";

export default {
  name: "TodayAttendance",
  components: { SideBar, DataTable, StatusCard },
  setup() {
    const search = ref("");
    const headers = [
      { text: "Date", value: "date" },
      { text: "Name", value: "name" },
      { text: "ClockInTime", value: "ClockInTime" },
      { text: "ClockOutTime", value: "ClockOutTime" },
      { text: "ClockInGate", value: "ClockInGate" },
      { text: "ClockOutGate", value: "ClockOutGate" },
      { text: "Status", value: "status" },
    ];

    const records = [
      {
        date: "2025-04-25",
        name: "John Doe",
        ClockInTime: "09:00",
        ClockOutTime: "17:00",
        ClockInGate: "Gate A",
        ClockOutGate: "Gate B",
        status: "Late",
      },
    ];

    const historyRecords = [
      {
        date: "2025-04-25",
        name: "John Doe",
        ClockInTime: "09:00",
        ClockOutTime: "17:00",
        ClockInGate: "Gate A",
        ClockOutGate: "Gate B",
        status: "Late",
      },
      {
        date: "2025-04-25",
        name: "John Doe",

        checkInTime: "08:45",
        checkOutTime: "17:05",
        checkInGate: "Gate B",
        checkOutGate: "Gate C",
        status: "On Time",
      },
      {
        date: "2025-04-25",
        name: "John Doe",
        ClockInTime: "09:20",
        ClockOutTime: "16:55",
        ClockInGate: "Gate A",
        ClockOutGate: "Gate A",
        status: "Late",
      },
      {
        date: "2025-04-25",
        name: "John Doe",
        checkInTime: "08:30",
        checkOutTime: "17:15",
        checkInGate: "Gate C",
        checkOutGate: "Gate B",
        status: "On Time",
      },
      {
        date: "2025-04-25",
        name: "John Doe",
        ClockInTime: "09:10",
        ClockOutTime: "16:40",
        ClockInGate: "Gate B",
        ClockOutGate: "Gate C",
        status: "Abnormal",
      },
    ];

    return {
      search,
      headers,
      records,
      StatusCard,
      historyRecords,
    };
  },
};
</script>

<style scoped>
text {
  color: black;
}
h2 {
  margin: 10px auto;
  font-size: 30px;
}

.login-page {
  display: flex;
  flex-direction: column;
  align-items: center; /* 這樣內容（input, button）就會置中 */
  margin-top: 0px;
}
.centered-input {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
}
</style>
