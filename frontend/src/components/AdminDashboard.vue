<template>
  <div v-if="professionals" class="ms-5 me-5 mt-3">
    <UsersCard :users="professionals" usertype="professional" />
  </div>
  <div v-if="customers" class="ms-5 me-5 mt-3">
    <UsersCard :users="customers" usertype="customer" />
  </div>
</template>

<script>

import UsersCard from './UsersCard.vue'
export default {
  name: 'AdminDashboard',
  data() {
    return {
      professionals: null,
      customers: null
    }
  },
  components: {
    UsersCard
  },
  methods: {
    async fetchProfessionals() {
      try {
        const response = await fetch('http://localhost:5000/api/professionals' ,
          {
            "method": "GET",
            "headers" : {
              "Authentication-Token" : localStorage.getItem("token")
            }
          }
        );
        const data = await response.json();
        if (response.ok) {

          this.professionals = data;
          console.log(this.professionals);
        } else if (response.status === 401) {
          this.$router.push('/login');
        } else if (response.status === 403) {
          this.$router.push('/admin/dashboard');
        } else {
          this.$router.go(0)
        }


      }
      catch (err) {
        console.log(err);
      }
    },
    async fetchCustomers() {
      try {
        const response = await fetch('http://localhost:5000/api/customers' ,
          {
            "method": "GET",
            "headers" : {
              "Authentication-Token" : localStorage.getItem("token")
            }
          }
        );
        const data = await response.json();
        
        if (response.ok) {

          this.customers = data;
        } else if (response.status === 401) {
          this.$router.push('/login');
        } else if (response.status === 403) {
          this.$router.push('/admin/dashboard');
        } else {
          this.$router.go(0)
        }


      }
      catch (err) {
        console.log(err);
      }
    }
  },
  mounted() {
    this.fetchProfessionals();
    
    this.fetchCustomers();
  }

}
</script>
