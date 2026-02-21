<template>
    <Navbar :usertype="professional" />
    <router-view></router-view>
</template>

<script>

import Navbar from './Navbar.vue'
export default {
  name: 'ProfessionalComp',
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
