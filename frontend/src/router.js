import { createRouter, createWebHistory } from 'vue-router'

import HomeComp from './components/Home.vue'
import LoginComp from './components/Login.vue'
import CustomerRegisterComp from './components/CustomerRegister.vue'
import ProfessionalRegisterComp from './components/ProfessionalRegister.vue'

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
    }
]


const router = createRouter({
    history : createWebHistory() , 
    routes
})

export default router