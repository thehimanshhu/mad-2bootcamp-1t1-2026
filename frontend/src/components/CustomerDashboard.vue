<template>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h3>Packages</h3>

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
                            <p class="card-text">Professional Name: {{ pack.professional_name }}</p>
                            <p class="card-text">Professional Email: {{ pack.professional_email }}</p>
                            <p class="card-text">Professional Mobile: {{ pack.professional_mobile }}</p>
                            <p class="card-text">Start Date: {{ pack.start_date }}</p>
                            <p class="card-text">End Date: {{ pack.end_date }}</p>
                            <p class="card-text">Status: {{ pack.status }}</p>
                            <router-link :to="`/customer/book-package/${pack.id}`" class="btn btn-primary btn-sm">Book
                                Package</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="card mt-5 ms-5 me-5 mb-4">
        <div class="card-header">
            <h3>My Bookings</h3>
        </div>
        <div class="card-body">
            <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="pills-accepted-tab" data-bs-toggle="pill"
                        data-bs-target="#pills-accepted" type="button" role="tab" aria-controls="pills-accepted"
                        aria-selected="true">Accepted</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pills-requested-tab" data-bs-toggle="pill"
                        data-bs-target="#pills-requested" type="button" role="tab" aria-controls="pills-requested"
                        aria-selected="false">Requested</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="pills-rejected-tab" data-bs-toggle="pill"
                        data-bs-target="#pills-rejected" type="button" role="tab" aria-controls="pills-rejected"
                        aria-selected="false">Rejected/Completed</button>
                </li>

            </ul>
            <div class="tab-content" id="pills-tabContent">
                <div class="tab-pane fade show active" id="pills-accepted" role="tabpanel"
                    aria-labelledby="pills-accepted-tab" tabindex="0">


                </div>
                <div class="tab-pane fade" id="pills-requested" role="tabpanel" aria-labelledby="pills-requested-tab"
                    tabindex="0">
                    <table v-if="bookings && bookings.Requested && bookings.Requested.length > 0" class="table">
                        <thead>
                            <tr>
                                <th scope="col">Package Name</th>
                                <th scope="col">Professional Name</th>
                                <th scope="col">Professional Email</th>
                                <th scope="col">Date</th>
                                <th scope="col">Time</th>
                                <th scope="col">Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="booking in bookings.Requested" :key="booking.booking_id">
                                <th scope="row">{{ booking.package_title }}</th>
                                <td>{{ booking.professional_name }}</td>
                                <td>{{ booking.professional_email }}</td>
                                <td>{{ booking.date }}</td>
                                <td>{{ booking.start_time }}</td>
                                <td>{{ booking.status }}</td>
                            </tr>

                        </tbody>
                    </table>


                </div>
                <div class="tab-pane fade" id="pills-rejected" role="tabpanel" aria-labelledby="pills-rejected-tab"
                    tabindex="0">


                </div>

            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'CustomerDashboard',
    data() {
        return {
            packages: {},
            bookings: null
        }
    },
    methods: {

        async getpackages() {
            try {
                const response = await fetch('http://localhost:5000/api/get-packages', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
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
        },
        async fetchbooking() {
            try {
                const response = await fetch("http://127.0.0.1:5000/api/getbookings",
                    {
                        method: "GET",
                        headers: {
                            "Authentication-Token": localStorage.getItem("token"),
                            'Content-Type': 'application/json',
                        }
                    }
                )
                const data = await response.json();
                if (response.ok) {
                    this.bookings = data
                }

            }
            catch (e) {
                this.$router.push("/login")
            }
        }
    },
    mounted() {
        this.getpackages();
        this.fetchbooking()
    }

}
</script>
