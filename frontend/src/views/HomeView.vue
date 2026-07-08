<template>
  <div>
    <el-card>
      <template #header>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span>自习室座位总览</span>
          <el-date-picker
            v-model="selectedDate"
            type="date"
            placeholder="选择日期"
            format="YYYY-MM-DD"
            value-format="YYYY-MM-DD"
            style="width: 160px"
            @change="loadSeats"
          />
        </div>
      </template>

      <el-tabs v-model="activeRoom" @tab-change="loadSeats">
        <el-tab-pane
          v-for="room in rooms"
          :key="room.id"
          :label="room.name"
          :name="String(room.id)"
        />
      </el-tabs>

      <SeatMap v-if="seats.length > 0" :seats="seats" :room-name="currentRoomName" />
      <el-empty v-else description="该自习室暂无座位" />
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { getRooms, getSeatsByRoom } from '../api'
import SeatMap from '../components/SeatMap.vue'

const rooms = ref([])
const seats = ref([])
const activeRoom = ref('')
const selectedDate = ref(new Date().toISOString().split('T')[0])

const currentRoomName = computed(() => {
  const room = rooms.value.find(r => String(r.id) === activeRoom.value)
  return room ? room.name : ''
})

const loadRooms = async () => {
  const res = await getRooms()
  rooms.value = res.data
  if (rooms.value.length > 0 && !activeRoom.value) {
    activeRoom.value = String(rooms.value[0].id)
  }
}

const loadSeats = async () => {
  if (!activeRoom.value) return
  const res = await getSeatsByRoom(activeRoom.value, selectedDate.value)
  seats.value = res.data
}

onMounted(async () => {
  await loadRooms()
  await loadSeats()
})
</script>
