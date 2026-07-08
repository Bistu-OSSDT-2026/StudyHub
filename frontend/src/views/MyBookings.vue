<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span>我的预约</span>
          <el-input
            v-model="userName"
            placeholder="输入姓名查询"
            style="width: 200px"
            @change="loadBookings"
          />
        </div>
      </template>

      <el-table :data="bookings" stripe style="width: 100%">
        <el-table-column prop="room_name" label="自习室" />
        <el-table-column prop="seat_no" label="座位号" />
        <el-table-column prop="date" label="日期" />
        <el-table-column label="时间段">
          <template #default="{ row }">
            {{ row.start_time }} - {{ row.end_time }}
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态">
          <template #default="{ row }">
            <el-tag :type="row.status === 'active' ? 'success' : 'info'">
              {{ row.status === 'active' ? '有效' : '已取消' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template #default="{ row }">
            <el-button
              v-if="row.status === 'active'"
              type="danger"
              size="small"
              @click="handleCancel(row.id)"
            >
              取消预约
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-empty v-if="bookings.length === 0" description="暂无预约记录" />
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { getBookings, cancelBooking } from '../api'

const bookings = ref([])
const userName = ref('')

const loadBookings = async () => {
  if (!userName.value) {
    bookings.value = []
    return
  }
  const res = await getBookings({ user_name: userName.value })
  bookings.value = res.data
}

const handleCancel = async (id) => {
  await ElMessageBox.confirm('确定要取消这个预约吗？', '确认')
  try {
    await cancelBooking(id)
    ElMessage.success('已取消')
    await loadBookings()
  } catch {
    ElMessage.error('取消失败')
  }
}

onMounted(() => {})
</script>
