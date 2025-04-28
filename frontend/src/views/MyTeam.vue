<template>
  <v-app>
    <SideBar>
      <v-container>
        <!-- 下拉選單 -->
        <v-card title="Department" flat width="30%">
          <SelectBox
            v-model="selectedDepartment"
            :items="Department"
          ></SelectBox>
          <p>你選的是：{{ selectedDepartment }}</p>
        </v-card>
        <!-- 時間表 -->
        <div class="v-card-title">Date</div>
        <div class="filter">
          <v-card elevation="0" class="datepicker-container">
            <VueDatePicker
              v-model="Startdate"
              class="custom-datepicker"
              teleport="body"
              ref="startDatePicker"
              type="date"
              :enable-time-picker="false"
            />
          </v-card>
          <p>To</p>
          <v-card elevation="0" class="datepicker-container">
            <VueDatePicker
              v-model="Enddate"
              class="custom-datepicker"
              teleport="body"
              ref="endDatePicker"
              :enable-time-picker="false"
            />
          </v-card>
          <v-btn variant="tonal" color="blue"> This Month </v-btn>
          <v-btn variant="tonal" color="blue"> This Week </v-btn>
          <v-btn variant="tonal" color="black"> Analysis Chart </v-btn>
        </div>

        <!-- 放總體出勤分析表 -->
        <v-card title="OverTime Summary" flat>
          <v-table class="d-flex justify-center">
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
            </thead>
            <tbody>
              <tr v-for="item in summary" :key="item.name" class="text-center">
                <td>
                  <WorkSummaryCard
                    :totalWorkHours="item.TotalWorkHours"
                    :unit="'hr'"
                    :timeUnit="'month'"
                    :lastRecord="1968"
                  />
                </td>
                <td>
                  <WorkSummaryCard
                    :totalWorkHours="item.TotalOTHours"
                    :unit="'hr'"
                    :timeUnit="'month'"
                    :lastRecord="1968"
                  />
                </td>
                <td>
                  <WorkSummaryCard
                    :totalWorkHours="item.OTHoursPerson"
                    :unit="'hr'"
                    :timeUnit="'month'"
                    :lastRecord="12.3"
                  />
                </td>
                <td>
                  <WorkSummaryCard
                    :totalWorkHours="item.OTHeadcounts"
                    :unit="'p'"
                    :timeUnit="'month'"
                    :lastRecord="9"
                  />
                </td>
              </tr>
            </tbody>
          </v-table>
        </v-card>
        <!-- 超時工作表 -->
        <v-card title="OverTime Alert List" flat>
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
          <DataTable
            :show-headers="headers2"
            :items="testData"
            :search="search"
          />
        </v-card>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";
import SelectBox from "../components/SelectBox.vue";
import WorkSummaryCard from "../components/SummaryCard.vue";
import DataTable from "../components/DataTable.vue";
import { ref, onMounted } from "vue";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

export default {
  name: "MyTeam",
  components: { SelectBox, SideBar, WorkSummaryCard, DataTable, VueDatePicker },
  setup() {
    const selectedDepartment = ref("");
    const Startdate = ref();
    const Enddate = ref();
    const startDatePicker = ref(null);
    const endDatePicker = ref(null);

    const headers = [
      { text: "Total Work Hours", value: "TotalWorkHours" },
      { text: "Total OT Hours", value: "TotalOTHours" },
      { text: "OT Hours/ person", value: "OTHoursPerson" },
      { text: "OT-HeadCounts", value: "OTHeadcounts" },
    ];
    const headers2 = [
      { text: "Employee ID", value: "EmployeeID" },
      { text: "Name", value: "Name" },
      { text: "OT Counts", value: "OTCounts" },
      { text: "OT Hours", value: "OTHours" },
      { text: "Status", value: "status" },
    ];
    const Department = [
      "Sales",
      "Marketing",
      "Human Resources",
      "Engineering",
      "Customer Support",
      "Finance",
    ];
    const summary = [
      {
        TotalWorkHours: "5649",
        TotalOTHours: "369",
        OTHoursPerson: "12.3",
        OTHeadcounts: "7",
      },
    ];
    const testData = [
      {
        EmployeeID: "E001",
        Name: "John Doe",
        OTCounts: 5,
        OTHours: 20,
        status: "Warning",
      },
      {
        EmployeeID: "E002",
        Name: "Jane Smith",
        OTCounts: 3,
        OTHours: 15,
        status: "Warning",
      },
      {
        EmployeeID: "E003",
        Name: "Mike Johnson",
        OTCounts: 8,
        OTHours: 32,
        status: "Alert",
      },
      {
        EmployeeID: "E004",
        Name: "Sarah Lee",
        OTCounts: 2,
        OTHours: 10,
        status: "Alert",
      },
    ];

    onMounted(() => {
      // 調整 Startdate DatePicker 位置
      const startInput = startDatePicker.value.$el.querySelector(".dp__input");
      const endInput = endDatePicker.value.$el.querySelector(".dp__input");
      const menus = document.querySelectorAll(".dp__menu");

      const updatePosition = (input, menu) => {
        if (input && menu) {
          const rect = input.getBoundingClientRect();
          menu.style.left = `${rect.left}px`; // 動態設置 left 為輸入框的左邊緣
          menu.style.top = `${rect.bottom + 4}px`; // 設置為輸入框底部 + 4px
          menu.style.transform = "none"; // 移除 transform
          menu.style.width = `${rect.width}px`; // 與輸入框同寬
          menu.style.maxWidth = "200px";
        }
      };

      if (startInput && menus[0]) {
        startInput.addEventListener("click", () =>
          updatePosition(startInput, menus[0])
        );
        window.addEventListener("scroll", () =>
          updatePosition(startInput, menus[0])
        );
        window.addEventListener("resize", () =>
          updatePosition(startInput, menus[0])
        );
      }

      if (endInput && menus[1]) {
        endInput.addEventListener("click", () =>
          updatePosition(endInput, menus[1])
        );
        window.addEventListener("scroll", () =>
          updatePosition(endInput, menus[1])
        );
        window.addEventListener("resize", () =>
          updatePosition(endInput, menus[1])
        );
      }
    });

    return {
      selectedDepartment,
      Department,
      headers,
      headers2,
      summary,
      testData,
      Startdate,
      Enddate,
      startDatePicker,
      endDatePicker,
    };
  },
};
</script>

<style>
.v-table .text-center td {
  justify-content: center;
}

.filter {
  display: grid;
  grid-template-columns: auto auto auto auto auto auto;
  gap: 16px;
  align-items: end;
}

.datepicker-container {
  width: 100%;
  max-width: 200px;
  min-width: 180px;
}

.custom-datepicker .dp__input {
  width: 100%;
  box-sizing: border-box;
  height: 32px;
  font-size: 14px;
}

.custom-datepicker .dp__menu {
  min-width: unset;
}
</style>
