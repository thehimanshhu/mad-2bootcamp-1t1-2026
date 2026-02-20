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
                        <button v-if="user['Status'] === 'Pending'" class="btn btn-success btn-sm me-2"
                            @click="approveUser(user['prof_id'])">Approve</button>

                        <button v-if="user['Status'] === 'Pending'" class="btn btn-danger btn-sm"
                            @click="flagUser(user['prof_id'])">Flag</button>
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
                        <button v-if="user['Status'] === 'Pending'" class="btn btn-success btn-sm me-2"
                            @click="approveUser(user['customer_id'])">Approve</button>

                        <button v-if="user['Status'] === 'Pending'" class="btn btn-danger btn-sm"
                            @click="flagUser(user['customer_id'])">Flag</button>
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

})
</script>