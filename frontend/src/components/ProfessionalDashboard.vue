<template>
    <div class="alert alert-info mt-3 mb-3" role="alert" v-if="message">
        
        <div>
            {{ message }}
        </div>
        <button type="button" class="btn-close" @click="clearMessage"></button>
    </div>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            <div class="d-flex">
                <h3>Packages</h3>
                <router-link to="/professional/create-package" class="btn btn-primary btn-sm ms-auto">Create Package</router-link>
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
                            <p class="card-text">Start Date: {{ pack.start_date }}</p>
                            <p class="card-text">End Date: {{ pack.end_date }}</p>
                            <p class="card-text">Status: {{ pack.status }}</p>
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
                   <table v-if="bookings && bookings.Accepted && bookings.Accepted.length > 0" class="table">
                        <thead>
                            <tr>
                                <th scope="col">Package Name</th>
                                <th scope="col">Customer Name</th>
                                <th scope="col">Customer Email</th>
                                <th scope="col">Date</th>
                                <th scope="col">Time</th>
                                <th scope="col">Status</th>
                                
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="booking in bookings.Accepted" :key="booking.booking_id">
                                <th scope="row">{{ booking.package_title }}</th>
                                <td>{{ booking.customer_name }}</td>
                                <td>{{ booking.customer_email }}</td>
                                <td>{{ booking.date }}</td>
                                <td>{{ booking.start_time }}</td>
                                <td>{{ booking.status }}</td>
                               
                            </tr>

                        </tbody>
                    </table> 

                </div>
                <div class="tab-pane fade" id="pills-requested" role="tabpanel" aria-labelledby="pills-requested-tab"
                    tabindex="0">
                    <table v-if="bookings && bookings.Requested && bookings.Requested.length > 0" class="table">
                        <thead>
                            <tr>
                                <th scope="col">Package Name</th>
                                <th scope="col">Customer Name</th>
                                <th scope="col">Customer Email</th>
                                <th scope="col">Date</th>
                                <th scope="col">Time</th>
                                <th scope="col">Status</th>
                                <th scope="col">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="booking in bookings.Requested" :key="booking.booking_id">
                                <th scope="row">{{ booking.package_title }}</th>
                                <td>{{ booking.customer_name }}</td>
                                <td>{{ booking.customer_email }}</td>
                                <td>{{ booking.date }}</td>
                                <td>{{ booking.start_time }}</td>
                                <td>{{ booking.status }}</td>
                                <td>
                                    <button 
                                        class="btn btn-success btn-sm" @click="acceptbooking(booking.booking_id)">Accept</button>
                                    <button 
                                        class="btn btn-danger btn-sm" @click="rejectbooking(booking.booking_id)">Reject</button>
                                </td>
                            </tr>

                        </tbody>
                    </table>


                </div>
                <div class="tab-pane fade" id="pills-rejected" role="tabpanel" aria-labelledby="pills-rejected-tab"
                    tabindex="0">
                    <table v-if="bookings && bookings.rejected && bookings.rejected.length > 0" class="table">
                        <thead>
                            <tr>
                                <th scope="col">Package Name</th>
                                <th scope="col">Customer Name</th>
                                <th scope="col">Customer Email</th>
                                <th scope="col">Date</th>
                                <th scope="col">Time</th>
                                <th scope="col">Status</th>
                                
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="booking in bookings.rejected" :key="booking.booking_id">
                                <th scope="row">{{ booking.package_title }}</th>
                                <td>{{ booking.customer_name }}</td>
                                <td>{{ booking.customer_email }}</td>
                                <td>{{ booking.date }}</td>
                                <td>{{ booking.start_time }}</td>
                                <td>{{ booking.status }}</td>
                               
                            </tr>

                        </tbody>
                    </table> 

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
            packages : null , 
            bookings: null , 
            message : null
        }
    },
    methods: {
        
        async getpackages(){
            try {
                const response = await fetch('http://localhost:5000/api/get-packages', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json' , 
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
        } , 
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
                    console.log(this.bookings)
                }

            }
            catch (e) {
                this.$router.push("/login")
            }
        },
        async acceptbooking(booking_id){
            try {
                const response = await fetch(`http://localhost:5000/api/accept-booking/${booking_id}`, {
                    method: "GET",
                    headers: {
                        "Authentication-Token": localStorage.getItem("token"),
                        'Content-Type': 'application/json',
                    }
                });
                const data = await response.json();
                if (response.ok) {
                    this.message = data.message
                    this.fetchbooking();
                } else {
                    console.error('Failed to accept booking:', data);
                }
            } catch (error) {
                console.error('Error accepting booking:', error);
            }
        },
        async rejectbooking(booking_id){
            try {
                const response = await fetch(`http://localhost:5000/api/reject-booking/${booking_id}`, {
                    method: "GET",
                    headers: {
                        "Authentication-Token": localStorage.getItem("token"),
                        'Content-Type': 'application/json',
                    }
                });
                const data = await response.json();
                if (response.ok) {
                    this.message = data.message
                    this.fetchbooking();
                } else {
                    console.error('Failed to reject booking:', data);
                }
            } catch (error) {
                console.error('Error rejecting booking:', error);
            }
        },
        clearMessage() {
            this.message = null;
        }
    },
    mounted() {
      this.getpackages(); 
      this.fetchbooking();
    }

}
</script>
