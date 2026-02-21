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
                <div class="col-3">
                    <div class="card ">

                        <div class="card-body">
                            <h5 class="card-title">Basic Package</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk
                                of
                                the
                                card’s content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
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
            professionals: null,
            customers: null
        }
    },
    methods: {
        async fetchProfessionals() {
            try {
                const response = await fetch('http://localhost:5000/api/professionals',
                    {
                        "method": "GET",
                        "headers": {
                            "Authentication-Token": localStorage.getItem("token")
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
                const response = await fetch('http://localhost:5000/api/customers',
                    {
                        "method": "GET",
                        "headers": {
                            "Authentication-Token": localStorage.getItem("token")
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
