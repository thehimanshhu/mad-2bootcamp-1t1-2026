<template>
    <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="card">

            <div class="card-body p-3">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="floatingInput" placeholder="Himanshu">
                    <label for="floatingInput">Name</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="floatingInput" placeholder="123 Main St">
                    <label for="floatingInput">Address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="floatingInput" placeholder="123-456-7890">
                    <label for="floatingInput">Phone Number</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="floatingInput" placeholder="123-456-7890">
                    <label for="floatingInput">Resume</label>
                </div>

                <button class="btn btn-primary w-100">Register</button>
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
                resume: ""
            }
        }
    }
}
</script>