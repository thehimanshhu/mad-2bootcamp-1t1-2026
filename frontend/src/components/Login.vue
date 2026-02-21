<template>
    <div class ="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="card">

            <div class="card-body p-3" >
                <div class="alert alert-danger" v-if="message">{{   message }}</div>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="formdata.email">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="formdata.password">
                    <label for="floatingPassword">Password</label>
                </div>
                <button class="btn btn-primary w-100" @click="login">Login</button>
            </div>
        </div>

    </div>
</template>

<script>
export default{
    name :"LoginComp",
    data(){
        return {
            formdata:{
                email:"",
                password:""
            },
            message:""      
        }
    },
    methods:{
        async login(){
            try {
                const response = await fetch("http://localhost:5000/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.formdata)
                });
                const data = await response.json();
                if (response.ok){
                    const token = data.token
                    localStorage.setItem("token", token)
                    localStorage.setItem("email" , this.formdata.email)
                    localStorage.setItem("role" , data.role)
                    if (data.role === "admin"){
                        this.$router.push("/admin/dashboard")
                    }
                    else if (data.role === "professional"){
                        this.$router.push("/professional/dashboard")
                    }   
                    else if (data.role === "customer"){
                        this.$router.push("/customer/dashboard")
                    }   
                    
                }
                else {
                    this.message = data.message
                }
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>