<template>
  <div class="container mt-5">

    <div class="d-flex justify-content-center">
      <div>
        <h1>{{ msg }}</h1>

      </div>

      <div>
        <router-link to="/login" class="btn btn-primary mx-2">Login</router-link>
        <router-link to="/customer/register" class="btn btn-secondary mx-2">Customer Register</router-link>
        <router-link to="/professional/register" class="btn btn-success mx-2">Professional Register</router-link>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeComp',
  data() {
    return {
      msg: "Welcome Himanshu!"
    }
  }
}
</script>
