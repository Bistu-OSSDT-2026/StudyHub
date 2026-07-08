<template>
  <div>
    <el-row :gutter="20" style="margin-bottom: 20px;">
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="自习室总数" :value="overview.total_rooms" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="座位总数" :value="overview.total_seats" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="今日预约数" :value="overview.today_bookings" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="累计预约数" :value="overview.total_bookings" />
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20">
      <el-col :span="12">
        <el-card>
          <template #header>各自习室预约量</template>
          <StatsChart :option="roomChartOption" height="300px" />
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card>
          <template #header>近7天预约趋势</template>
          <StatsChart :option="trendChartOption" height="300px" />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getOverview, getBookingsByRoom, getDailyTrend } from '../api'
import StatsChart from '../components/StatsChart.vue'

const overview = ref({ total_rooms: 0, total_seats: 0, today_bookings: 0, total_bookings: 0 })
const roomChartOption = ref({})
const trendChartOption = ref({})

const loadOverview = async () => {
  const res = await getOverview()
  overview.value = res.data
}

const loadRoomStats = async () => {
  const res = await getBookingsByRoom()
  const data = res.data
  roomChartOption.value = {
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: data.map(d => d.room_name) },
    yAxis: { type: 'value', name: '预约数' },
    series: [{
      type: 'bar',
      data: data.map(d => d.booking_count),
      itemStyle: { color: '#409EFF' }
    }]
  }
}

const loadTrend = async () => {
  const res = await getDailyTrend(7)
  const data = res.data
  trendChartOption.value = {
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: data.map(d => d.date) },
    yAxis: { type: 'value', name: '预约数' },
    series: [{
      type: 'line',
      data: data.map(d => d.count),
      smooth: true,
      itemStyle: { color: '#67C23A' }
    }]
  }
}

onMounted(async () => {
  await Promise.all([loadOverview(), loadRoomStats(), loadTrend()])
})
</script>
