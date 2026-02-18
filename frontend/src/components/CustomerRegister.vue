<template>
    <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="card">

            <div class="card-body p-3">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.name" id="floatingInput"
                        placeholder="Himanshu">
                    <label for="floatingInput">Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" v-model="formdata.email" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" v-model="formdata.password" id="floatingPassword"
                        placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.address" id="floatingInput"
                        placeholder="123 Main St">
                    <label for="floatingInput">Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.mobile" id="floatingInput"
                        placeholder="123-456-7890">
                    <label for="floatingInput">Phone Number</label>
                </div>

                <button class="btn btn-primary w-100" @click="register">Register</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'CustomerRegisterComp',
    data() {
        return {
            formdata: {
                name: "",
                email: "",
                password: "",
                address: "",
                mobile: ""
            }
        }
    },
    methods: {
        async register() {
            try {
                const response = await fetch("http://localhost:5000/register?role=customer",
                                            {
                                                method : "POST" ,
                                                body :  JSON.stringify(this.formdata), 
                                                headers : {
                                                    "Content-Type" : "application/json"
                                                }
                                            }

                                        )
                console.log("hello")
                const data = await response.json() 
                console.log(data)
                this.$router.push("/login")
            }
            catch(e){
                console.log("m not able to connect")
                console.log(e)
            }
            
            
        }
    }
}
</script>