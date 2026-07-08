<template>
  <div>
    <h3>{{ roomName }} - 座位布局</h3>
    <div class="seat-grid">
      <div
        v-for="seat in seats"
        :key="seat.id"
        class="seat"
        :class="{
          'seat--available': !seat.is_booked && seat.status === 'available',
          'seat--booked': seat.is_booked,
          'seat--maintenance': seat.status === 'maintenance',
        }"
        :title="`${seat.seat_no} ${seat.is_booked ? '已预约' : '可用'}`"
      >
        <span class="seat-no">{{ seat.seat_no }}</span>
      </div>
    </div>
    <div class="legend">
      <span class="legend-item"><span class="dot dot--available"></span> 可用</span>
      <span class="legend-item"><span class="dot dot--booked"></span> 已预约</span>
      <span class="legend-item"><span class="dot dot--maintenance"></span> 维护中</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  seats: { type: Array, required: true },
  roomName: { type: String, default: '' },
})
</script>

<style scoped>
.seat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, 60px);
  gap: 10px;
  padding: 20px;
}
.seat {
  width: 60px;
  height: 60px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.2s;
  font-size: 12px;
}
.seat:hover { transform: scale(1.1); }
.seat--available { background: #e1f3d8; border: 2px solid #67c23a; color: #67c23a; }
.seat--booked { background: #fde2e2; border: 2px solid #f56c6c; color: #f56c6c; }
.seat--maintenance { background: #eee; border: 2px solid #999; color: #999; }
.legend { margin-top: 16px; display: flex; gap: 20px; }
.legend-item { display: flex; align-items: center; gap: 6px; font-size: 14px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot--available { background: #67c23a; }
.dot--booked { background: #f56c6c; }
.dot--maintenance { background: #999; }
</style>
