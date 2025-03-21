import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index.js'

import 'primeicons/primeicons.css';
import PrimeVue from 'primevue/config'
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import Aura from '@primeuix/themes/aura'
import ToastService from 'primevue/toastservice';

import axios from 'axios'

const app = createApp(App)
app.use(PrimeVue, { theme: {
    preset : Aura
}});
app.use(ToastService);
app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Dialog', Dialog);
app.component('InputText', InputText);
app.component('Checkbox', Checkbox);

app.config.globalProperties.$axios = axios;

app.use(router)

app.mount('#app');
