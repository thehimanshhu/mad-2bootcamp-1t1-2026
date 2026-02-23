<template>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h3>Packages</h3>
                <router-link to="/professional/create-package" class="btn btn-primary btn-sm ms-auto">Create Package</router-link>
            </div>
        </div>
        <div class="card-body">
            <div class="row ">
                <div v-for="pack in packages" :key="pack.id" class="col-3">
                    <div class="card ">

                        <div class="card-body">
                            <h5 class="card-title">Title: {{ pack.title }}</h5>
                            <p class="card-text">{{ pack.description }}</p>
                            <p class="card-text">Price: {{ pack.price }}</p>
                            <p class="card-text">Start Date: {{ pack.start_date }}</p>
                            <p class="card-text">End Date: {{ pack.end_date }}</p>
                            <p class="card-text">Status: {{ pack.status }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'ProfessionalDashboard',
    data() {
        return {
            packages : null
        }
    },
    methods: {
        
        async getpackages(){
            try {
                const response = await fetch('http://localhost:5000/api/get-packages', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json' , 
                        "Authentication-Token": localStorage.getItem("token")
                    }
                });
                if (response.ok) {
                    const data = await response.json();
                    this.packages = data;
                    console.log(this.packages);
                } else {
                    console.error('Failed to fetch packages');
                    this.$router.push("/login")
                }
            } catch (error) {
                console.error('Error:', error);
            }
        }
    },
    mounted() {
      this.getpackages(); 
    }

}
</script>
