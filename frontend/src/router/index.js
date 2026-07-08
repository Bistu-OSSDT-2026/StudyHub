import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BookingView from '../views/BookingView.vue'
import MyBookings from '../views/MyBookings.vue'
import StatsView from '../views/StatsView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/booking', name: 'booking', component: BookingView },
  { path: '/my-bookings', name: 'my-bookings', component: MyBookings },
  { path: '/stats', name: 'stats', component: StatsView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
