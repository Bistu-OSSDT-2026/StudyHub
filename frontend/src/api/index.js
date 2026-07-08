import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 5000,
})

// 自习室接口
export const getRooms = () => api.get('/rooms')
export const getRoom = (id) => api.get(`/rooms/${id}`)

// 座位接口
export const getSeatsByRoom = (roomId, date) =>
  api.get(`/seats/room/${roomId}`, { params: { date } })

// 预约接口
export const getBookings = (params) => api.get('/bookings', { params })
export const createBooking = (data) => api.post('/bookings', data)
export const cancelBooking = (id) => api.put(`/bookings/${id}/cancel`)

// 统计接口
export const getOverview = () => api.get('/stats/overview')
export const getBookingsByRoom = () => api.get('/stats/by-room')
export const getDailyTrend = (days) => api.get('/stats/daily-trend', { params: { days } })

export default api
