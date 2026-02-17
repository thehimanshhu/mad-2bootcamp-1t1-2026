<template>
  <div class="container mt-5">

    <div class="d-flex justify-content-center">
        <div>
            <h1>{{ msg }}</h1>
        </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard',
  data() {
    return {
      msg: "Welcome Himanshu!"
    }
  }
}
</script>
