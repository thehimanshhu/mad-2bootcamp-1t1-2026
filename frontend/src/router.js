import { createRouter, createWebHistory } from 'vue-router'

import HomeComp from './components/Home.vue'
import LoginComp from './components/Login.vue'
import CustomerRegisterComp from './components/CustomerRegister.vue'
import ProfessionalRegisterComp from './components/ProfessionalRegister.vue'

import AdminComp from './components/AdminComp.vue'
import AdminDashboard from './components/AdminDashboard.vue'
import AdminSearch from './components/AdminSearch.vue'
import ProfessionalComp from './components/ProfessionalComp.vue'
import ProfessionalDashboard from './components/ProfessionalDashboard.vue'
import CreatePackage from './components/CreatePackage.vue'
import CustomerComp from './components/CustomerComp.vue'
import CustomerDashboard from './components/CustomerDashboard.vue'
import BoookPackge from './components/BookPackge.vue'
const routes = [
    {
        "path": "/",
        "component": HomeComp
    },
    {
        "path": "/login",
        "component": LoginComp
    },
    {
        "path": "/customer/register",
        "component": CustomerRegisterComp
    },
    {
        "path": "/professional/register",
        "component": ProfessionalRegisterComp
    },
    {
        "path": "/admin",
        "component": AdminComp,
        children: [
            {
                path: "dashboard",
                component: AdminDashboard
            },
            {
                path: "Search",
                component: AdminSearch
            }

        ]
    },
    {
        path: "/professional",
        component: ProfessionalComp,
        children: [
            {
                path: "dashboard",
                component: ProfessionalDashboard
            },
            {
                path: "create-package",
                component: CreatePackage
            }
        ]
    },
    {
        path: "/customer",
        component: CustomerComp,
        children: [
            {
                path: "dashboard",
                component: CustomerDashboard
            },
            {
                path: "book-package/:id",
                component: BoookPackge
            }
        ]
    },

]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router