<template>
    <Navbar :usertype="customer" />
    <router-view></router-view>
</template>

<script>

import Navbar from './Navbar.vue'
export default {
  name: 'CustomerDashboard',
  data() {
    return {
      msg: "Welcome Himanshu!"
    }
  },
  components: {
    Navbar
  }
}
</script>
