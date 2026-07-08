<template>
  <el-container style="min-height: 100vh">
    <el-header style="background: #545c64; display: flex; align-items: center; justify-content: space-between;">
      <h2 style="color: #fff; margin: 0;">📚 自习室预约系统</h2>
      <el-menu
        :default-active="currentRoute"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        router
      >
        <el-menu-item index="/">座位总览</el-menu-item>
        <el-menu-item index="/booking">我要预约</el-menu-item>
        <el-menu-item index="/my-bookings">我的预约</el-menu-item>
        <el-menu-item index="/stats">数据统计</el-menu-item>
      </el-menu>
    </el-header>
    <el-main style="padding: 20px; background: #f5f7fa;">
      <router-view />
    </el-main>
  </el-container>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const currentRoute = computed(() => route.path)
</script>
