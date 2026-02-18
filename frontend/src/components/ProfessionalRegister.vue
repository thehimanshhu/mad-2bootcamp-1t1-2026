<template>
    <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="card">

            <div class="card-body p-3">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.name" id="floatingInput" placeholder="Himanshu" required="">
                    <label for="floatingInput">Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" v-model="formdata.email" id="floatingInput" placeholder="name@example.com" required="">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" v-model="formdata.password" id="floatingPassword" placeholder="Password" required="">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.address" id="floatingInput" placeholder="123 Main St" required="">
                    <label for="floatingInput">Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" v-model="formdata.phone" id="floatingInput" placeholder="123-456-7890" required="">
                    <label for="floatingInput">Phone Number</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="file" class="form-control" @change="uploadfile" id="floatingInput"  placeholder="123-456-7890">
                    <label for="floatingInput">Resume</label>
                </div>

                <button class="btn btn-primary w-100" @click="register"> Register</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'ProfessionalRegisterComp',
    data() {
        return {
            formdata: {
                name: "",
                email: "",
                password: "",
                address: "",
                phone: "",
                resume: null
            }
        }
    },
    methods: {
        uploadfile(e){
            this.formdata.resume = e.target.files[0]


        },
        async register() {
            try {
                const formData = new FormData()
                formData.append('name', this.formdata.name)
                formData.append('email', this.formdata.email)
                formData.append('password', this.formdata.password)
                formData.append('address', this.formdata.address)
                formData.append('mobile', this.formdata.phone)
                if (this.formdata.resume) {
                    formData.append('resume', this.formdata.resume)
                }

                console.log(this.formdata)
                const response = await fetch("http://localhost:5000/register?role=professional",
                    {
                        method: "POST",
                        body: formData
                    }
                )
                console.log("hello")
                const data = await response.json()
                console.log(data)
                this.$router.push("/login")
            }
            catch (e) {
                console.log("m not able to connect")
                console.log(e)
            }


        }
    }
}
</script>