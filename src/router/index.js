import { createRouter, createWebHistory } from 'vue-router'
import BillList from '../components/Bills/BillList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'order',
    //   component: MyOrderVue
    // },
    {
      path: '/Bill',
      name: 'Bill',
      component: BillList
    }
  ]
})

export default router
