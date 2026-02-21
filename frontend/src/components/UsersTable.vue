<template>
    <div v-if="perticular_users && perticular_users.users && perticular_users.users.length > 0">

        <table v-if="usertype === 'professional'" class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Address</th>
                    <th scope="col">Status</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(user, index) in perticular_users.users" :key="index">
                    <td>{{ user['Professional Name'] }}</td>
                    <td>{{ user['Professional Email'] }}</td>
                    <td>{{ user['Mobile'] }}</td>
                    <td>{{ user['Address'] }}</td>
                    <td>{{ user['Status'] }}</td>
                    <td>
                        
                        <!-- Button trigger modal -->
                        <button type="button" class="btn btn-secondary btn-sm me-2" data-bs-toggle="modal"
                            :data-bs-target="'#viewresume' + user['prof_id']">
                            View Resume
                        </button>

                        <!-- Modal -->
                        <div class="modal fade" :id="'viewresume' + user['prof_id']" tabindex="-1" aria-labelledby="viewresumeLabel"
                            aria-hidden="true">
                            <div class="modal-dialog modal-lg">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="viewresumeLabel">View Resume</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal"
                                            aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <embed :src="'http://localhost:5000/' + user['Professional Resume URL']" type="application/pdf" width="100%" height="600px" />
                                    </div>
                                   
                                </div>
                            </div>
                        </div>
                        <button v-if="user['Status'] === 'Registered'" class="btn btn-success btn-sm me-2"
                            @click="approveprof(user['prof_id'])">Accept</button>
                        <button v-if="user['Status'] === 'Registered'" class="btn btn-danger btn-sm me-2"
                            @click="rejectprof(user['prof_id'])">Reject</button>
                        <button v-if="user['Status'] === 'Flagged'" class="btn btn-warning btn-sm me-2"
                            @click="unflagprof(user['prof_id'])">Unflag</button>
                        <button v-if="user['Status'] === 'Active'" class="btn btn-warning btn-sm me-2"
                            @click="flagprof(user['prof_id'])">Flag</button>


                    </td>
                </tr>
            </tbody>
        </table>
        <table v-if="usertype === 'customer'" class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Address</th>
                    <th scope="col">Status</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(user, index) in perticular_users.users" :key="index">
                    <td>{{ user['Customer Name'] }}</td>
                    <td>{{ user['Customer Email'] }}</td>
                    <td>{{ user['Mobile'] }}</td>
                    <td>{{ user['Address'] }}</td>
                    <td>{{ user['Status'] }}</td>
                    <td>
                        
                        <button v-if="user['Status'] === 'Active'" class="btn btn-warning btn-sm"
                            @click="flagCust(user['customer_id'])">Flag</button>
                        <button v-if="user['Status'] === 'Flagged'" class="btn btn-warning btn-sm"
                            @click="unflagCust(user['customer_id'])">Unflag</button>

                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div v-else>
        <p>No users found for status: {{ perticular_users.status }}</p>
    </div>
</template>

<script>
export default ({
    name: 'UsersTable',
    props: {
        perticular_users: {
            type: Object,
            required: true
        },
        usertype: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            // Define any data properties if needed
        }
    },
    methods: {
        async approveprof(prof_id) {
            const response = await fetch(`http://localhost:5000/api/approve-professional/${prof_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while approving the professional.");
            }
        },
        async rejectprof(prof_id) {
            const response = await fetch(`http://localhost:5000/api/reject-professional/${prof_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while rejecting the professional.");
            }
        },

        async flagprof(prof_id) {

            const response = await fetch(`http://localhost:5000/api/flag-professional/${prof_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while flagging the professional.");
            }
        },
        async unflagprof(prof_id) {

            const response = await fetch(`http://localhost:5000/api/unflag-professional/${prof_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while unflagging the professional.");
            }
        },
        async flagCust(customer_id) {
            const response = await fetch(`http://localhost:5000/api/flag-customer/${customer_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while flagging the customer.");
            }
        },
        async unflagCust(customer_id) {
            const response = await fetch(`http://localhost:5000/api/unflag-customer/${customer_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    "Authentication-Token": localStorage.getItem('token')
                }
            });
            const data = await response.json();
            if (response.ok) {
                this.$router.go(0); // Refresh the page
            } else if (response.status === 401) {
                alert("Session expired. Please log in again.");
                this.$router.push('/login');
            } else if (response.status === 403) {
                this.$router.push('/login');
            } else {
                alert(data.error || "An error occurred while unflagging the customer.");
            }
        }
    }

})
</script>