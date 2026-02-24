<template>
  <div class="d-flex justify-content-center mt-2">
    <div class="card  " style="width: 24rem;">

      <div class="card-body">
        <div class="d-flex">
          <div class="form-check me-2">
            <input class="form-check-input" type="radio" v-model="query_type" value="customer" name="radioDefault"
              id="radioCustomer">
            <label class="form-check-label" for="radioCustomer">
              Customer
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" v-model="query_type" value="professional" name="radioDefault"
              id="radioprofessional" >
            <label class="form-check-label" for="radioprofessional">
              Professional
            </label>
          </div>

        </div>
        <div class="form-floating mt-3">
          <input type="text" class="form-control" v-model="query" id="floatingInput" placeholder="Enter search query">
          <label for="floatingInput">Search Query</label>
        </div>
        <button class="btn btn-primary mt-3 w-100" @click="search">Search</button>

      </div>
    </div>
  </div>
  <div v-if="customers && customers.length>0"  class="card">
    <div class="card-header">
      Customer
    </div>
    <div class="card-body">
      <table  class="table">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Address</th>
            <th scope="col">Status</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cust, index) in customers" :key="index">
            <td>{{ cust["Customer Name"] }}</td>
            <td>{{ cust['Customer Email'] }}</td>
            <td>{{ cust['Mobile'] }}</td>
            <td>{{ cust['Address'] }}</td>
            <td>{{ cust['Status'] }}</td>

          </tr>
        </tbody>
      </table>

    </div>
  </div>
  <div v-if="professionals && professionals.length>0" class="card">
    <div class="card-header">
      Professional
    </div>
    <div class="card-body">
      <table  class="table">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Address</th>
            <th scope="col">Status</th>
            
          </tr>
        </thead>
        <tbody>
          <tr v-for="(prof, index) in professionals " :key="index">
                <td>{{ prof["Professional Name"] }}</td>
                <td>{{ prof['Professional Email'] }}</td>
            <td>{{ prof['Mobile'] }}</td>
            <td>{{ prof['Address'] }}</td>
            <td>{{ prof['Status'] }}</td>

          </tr>
        </tbody>
      </table>

    </div>
  </div>

</template>

<script>


export default {
  name: 'AdminSearch',
  data() {
    return {
      msg: "Welcome Himanshu!",

      query_type: "",
      query: "",
      customers: [],
      professionals: []
    }
  },
  watch: {
    query_type(n, o) {
      console.log("new : ", n)
      console.log("old :", o)
    }
  },
  methods: {
    async search() {
      const qtype = this.query_type
      const response = await fetch(`http://localhost:5000/api/admin-search?query_type=${this.query_type}&query=${this.query}` ,
        {
          method:"GET", 
          headers:{
            'Authentication-Token' : localStorage.getItem("token")
            
          }
        }
      )
      const data = await response.json()
      if (response.ok) {
        if (qtype == "customer") {
          this.customers = data

        }
        else if (qtype == "professional") {
          this.professionals = data
        }
      } else {
        console.error("Error searching: ", data)
      }
    }

  }
}
</script>
