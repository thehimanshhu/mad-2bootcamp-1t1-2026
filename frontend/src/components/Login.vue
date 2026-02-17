<template>
    <div class ="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <div class="card">

            <div class="card-body p-3" >
                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <button class="btn btn-primary w-100">Login</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'LoginComp',
    data() {
        return {
            formdata: {
                email: "",
                password: ""
            }
        }
    }
}
</script>