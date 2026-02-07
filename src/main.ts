import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// Import Phosphor Icons CSS
import "@phosphor-icons/web/regular"; // Loads regular weight
import "@phosphor-icons/web/fill";    // Loads fill weight// Optional: if you use filled icons

createApp(App).mount('#app')