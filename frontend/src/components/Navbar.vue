<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">HomeEase</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto me-5">
                    <li class="nav-item">
                        <router-link class="nav-link" :class="{ 'active' : $route.path=='/admin/dashboard'}" aria-current="page" href="#">Dashboard</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :class="{ 'active' : $route.path=='/admin/search'}" href="#">Search</router-link>
                    </li>
                    <li class="nav-item">
                       
                        <div class="dropdown">
                            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                 <i class="bi bi-person-circle fs-4 ms-2"></i>
                            </button>
                            <ul class="dropdown-menu dropdown-menu-end">
                                <li><router-link class="dropdown-item" to="/logout">Logout</router-link></li>
                               
                            </ul>
                        </div>
                    </li>


                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default ({
    name: 'UsersCard',
    data() {
        return {
            // Define any data properties if needed
        }
    },

})
</script>