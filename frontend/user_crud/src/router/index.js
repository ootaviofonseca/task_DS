import { createRouter, createWebHistory } from 'vue-router';
import UserTable from '../components/UserTable.vue';
import UserPage from '../components/UserPage.vue';

const routes = [
  { path: '/', component: UserTable },
  { path: '/user/:id',component: UserPage},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
