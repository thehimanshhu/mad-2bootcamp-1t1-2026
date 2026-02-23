<template>
    <router-link to="/customer/dashboard"  class="btn btn-outline-primary  mt-5 ms-5">Go Back</router-link>
    <div  class="card ms-auto me-auto " style="max-width: 500px;">
        <div v-if="pack.title" class="card-body">
            Package Title: {{ pack.title }} <br>
            Package Description: {{ pack.description }} <br>
            Package Price: {{ pack.price }} <br>
            Professional Name: {{ pack.professional_name }} <br>
            Professional Email: {{ pack.professional_email }} <br>
            Professional Mobile: {{ pack.professional_mobile }} <br>
            Start Date: {{ pack.start_date }} <br>
            End Date: {{ pack.end_date }} <br>
        </div>
        <div v-else-if="message" class="card-body">
            <div class="alert alert-danger">{{ message }}</div>

        </div>
        <div v-else class="card-body">
            <p class="card-text">Loading package details...</p>
        </div>
    </div>

    <div class="d-flex justify-content-center mt-5">
        
        <div class="card">
            <div class="card-body">
                                
                    <div class="form-floating mb-3">
                        <input type="date" class="form-control" v-model="formdata.start_date" required id="floatingStartDate" :min="pack.start_date " :max="pack.end_date" placeholder="Start Date">
                        <label for="floatingStartDate">Start Date</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="time" class="form-control" v-model="formdata.start_time" required id="floatingStartTime" placeholder="Start Time">
                        <label for="floatingStartTime">Start Time</label>
                    </div>
                    
                    <button class="btn btn-primary w-100 " @click="Bookpackage">Book</button>
            </div>
        </div>
    </div>

</template>
<script>
export default({
    name: "BookPackage",
    data(){
        return {
            formdata: {
                start_date: "",
                start_time: ""
            },
            pack :{
                id: null,
                title: "",
                description: "",
                price: null,
                professional_name: "",
                professional_email: "",
                professional_mobile: "",
                start_date: "",
                end_date: "",
                status: ""
            } , 
            message: ""
        }
    },
    methods:{
        async getpackage(){
            console.log("Fetching package details...");
            const pack_id = this.$route.params.id
            
            try {
                const response = await fetch(`http://localhost:5000/api/getpackage/${pack_id}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json' , 
                        "Authentication-Token": localStorage.getItem("token")
                    }
                });
                if (response.ok) {
                    const data = await response.json();
                    this.pack = data;
                    console.log(this.pack);
                }else if (response.status === 404){
                    this.message = "Package not found"
                    setTimeout(() => {
                        this.$router.push("/customer/dashboard")
                    }, 3000);
                }
                else {
                    console.error('Failed to fetch package');
                    this.$router.push("/login")
                }
                
            } catch (error) {
                console.error('Error:', error);
            }
            
        },
        async Bookpackage(){
            const pack_id = this.$route.params.id
            try {
                const response = await fetch(`http://localhost:5000/api/book-package/${pack_id}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json' , 
                        "Authentication-Token": localStorage.getItem("token")
                    },
                    body: JSON.stringify(this.formdata)
                });
                const data = await response.json();
                if (response.status === 201){
                    this.$router.push("/customer/dashboard")
                }
                else if (response.status === 400){
                    this.message = data.error || "An error occurred while booking the package.";
                }
                else if (response.status === 401){
                    this.$router.push("/login")
                }
                else if (response.status === 403){
                    this.$router.push("/login")
                }
                else{
                    this.message = data.error || "An error occurred while booking the package.";
                }
            } catch (error) {
                this.message = "An error occurred while booking the package.";
            }
        }
    } ,
    mounted(){
        this.getpackage();
    }
})
</script>