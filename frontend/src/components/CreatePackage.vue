<template>

    <router-link to="/professional/dashboard"  class="btn btn-outline-primary  mt-5 ms-5">Go Back</router-link>
    <div class="d-flex justify-content-center mt-5">
        
        <div class="card">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger">{{ message }}</div>

                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="formdata.title" id="floatingTitle" required placeholder="name@example.com">
                        <label for="floatingTitle">Package Title</label>
                    </div>
                    <div class="form-floating mb-3 ">
                        <input type="text" class="form-control" v-model="formdata.description" required id="floatingDescription" placeholder="Package Description">
                        <label for="floatingDescription">Package Description</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="formdata.price" required id="floatingPrice" placeholder="Package Price">
                        <label for="floatingPrice">Package Price</label>
                    
                    </div>
                    <div class="form-floating mb-3">
                        <input type="date" class="form-control" v-model="formdata.start_date" required id="floatingStartDate" :min="todaysdate()" placeholder="Start Date">
                        <label for="floatingStartDate">Start Date</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="date" class="form-control" v-model="formdata.end_date" required id="floatingEndDate" placeholder="End Date">
                        <label for="floatingEndDate">End Date</label>
                    </div>
                    <button class="btn btn-primary w-100 " @click="createPackage">Create Package</button>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: 'CreatePackage',
    data() {
        return {
            formdata: {
                title: "",
                description: "",
                price: null , 
                start_date: "",
                end_date: ""
            } , 
            message: null
        }
    },
    methods:{
        todaysdate(){
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const day = String(today.getDate()).padStart(2, '0');
            return `${year}-${month}-${day}`;
        },
        async createPackage(){
            try {
                const response = await fetch("http://localhost:5000/api/create-package", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                    body: JSON.stringify(this.formdata)
                });
                const data = await response.json();
                console.log(response.status)
                console.log(data)
                if (response.status === 201){
                    this.$router.push("/professional/dashboard")
                }
                else if (response.status === 401){
                    this.$router.push("/login")
                }
                else if (response.status === 403){
                    this.$router.push("/login")
                }
                else{
                    this.message = data.error || "An error occurred while creating the package.";
                }
            } catch (error) {
                this.message = "An error occurred while creating the package.";
            }
        }
    }

}
</script>