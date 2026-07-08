<template>
  <div>
    <el-card>
      <template #header><span>预约座位</span></template>

      <el-form :model="form" label-width="100px" style="max-width: 500px;">
        <el-form-item label="自习室">
          <el-select v-model="form.room_id" placeholder="选择自习室" @change="onRoomChange">
            <el-option
              v-for="room in rooms"
              :key="room.id"
              :label="room.name"
              :value="room.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="座位">
          <el-select v-model="form.seat_id" placeholder="选择座位">
            <el-option
              v-for="seat in availableSeats"
              :key="seat.id"
              :label="`${seat.seat_no} (${seat.is_booked ? '已预约' : '可用'})`"
              :value="seat.id"
              :disabled="seat.is_booked"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="预约人">
          <el-input v-model="form.user_name" placeholder="输入姓名" />
        </el-form-item>

        <el-form-item label="日期">
          <el-date-picker
            v-model="form.date"
            type="date"
            placeholder="选择日期"
            format="YYYY-MM-DD"
            value-format="YYYY-MM-DD"
          />
        </el-form-item>

        <el-form-item label="时间段">
          <el-col :span="11">
            <el-time-select
              v-model="form.start_time"
              start="08:00"
              end="22:00"
              step="00:30"
              placeholder="开始时间"
            />
          </el-col>
          <el-col :span="2" style="text-align: center;">-</el-col>
          <el-col :span="11">
            <el-time-select
              v-model="form.end_time"
              start="08:00"
              end="22:00"
              step="00:30"
              placeholder="结束时间"
            />
          </el-col>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitBooking" :loading="submitting">
            提交预约
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { getRooms, getSeatsByRoom, createBooking } from '../api'

const rooms = ref([])
const availableSeats = ref([])
const submitting = ref(false)

const form = reactive({
  room_id: null,
  seat_id: null,
  user_name: '',
  date: new Date().toISOString().split('T')[0],
  start_time: '09:00',
  end_time: '11:00',
})

const onRoomChange = async () => {
  const res = await getSeatsByRoom(form.room_id, form.date)
  availableSeats.value = res.data
}

const submitBooking = async () => {
  if (!form.user_name || !form.seat_id) {
    ElMessage.warning('请填写完整信息')
    return
  }
  submitting.value = true
  try {
    await createBooking(form)
    ElMessage.success('预约成功！')
    form.seat_id = null
  } catch (err) {
    ElMessage.error(err.response?.data?.error || '预约失败')
  } finally {
    submitting.value = false
  }
}

onMounted(async () => {
  const res = await getRooms()
  rooms.value = res.data
})
</script>
