<template>
    <Navbar />
    <router-view></router-view>
</template>

<script>

import Navbar from './Navbar.vue'
export default {
  name: 'AdminComp',
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
