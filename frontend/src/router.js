import { createRouter, createWebHistory } from 'vue-router'

import HomeComp from './components/Home.vue'
import LoginComp from './components/Login.vue'
import CustomerRegisterComp from './components/CustomerRegister.vue'
import ProfessionalRegisterComp from './components/ProfessionalRegister.vue'

import AdminComp from './components/AdminComp.vue'
import AdminDashboard from './components/AdminDashboard.vue'
import AdminSearch from './components/AdminSearch.vue'


const routes = [
    {
        "path" : "/" , 
        "component" : HomeComp
    },
    {
        "path" : "/login" , 
        "component" : LoginComp
    },
    {
        "path" : "/customer/register" , 
        "component" : CustomerRegisterComp
    },
    {
        "path" : "/professional/register" , 
        "component" : ProfessionalRegisterComp
    } ,
    {
        "path": "/admin",
        "component"   : AdminComp,
        children : [
            {
                path : "dashboard",
                component : AdminDashboard
            },
            {
                path : "Search",
                component : AdminSearch
            }

        ]
    }
]


const router = createRouter({
    history : createWebHistory() , 
    routes
})

export default router