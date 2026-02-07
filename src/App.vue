<script setup lang="ts">
import CircuitBackground from './components/ui/CircuitBackground.vue';
import NavBar from './components/NavBar.vue';
import HeroSection from './components/HeroSection.vue';
import ServicesSection from './components/ServicesSection.vue';
import ContactForm from './components/ContactForm.vue';
import TechComponents from './components/TechComponents.vue';

const scrollTo = (id: string) => {
   const el = document.querySelector(id);
   if (el) el.scrollIntoView({ behavior: 'smooth' });
};
</script>

<template>
   <main class="antialiased overflow-x-hidden">
      <CircuitBackground />
      <NavBar />

      <HeroSection @scroll-to="scrollTo" />
      <ServicesSection />

      <!-- You can break TechStack and Stats into their own files similarly -->
      <TechComponents />
      <ContactForm />

      <footer class="py-8 border-t border-white/10 bg-brand-dark relative z-10">
         <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-600 text-xs font-mono">© {{ new Date().getFullYear() }} Fullstack Master. All Systems
               Operational.</p>
         </div>
      </footer>
   </main>
</template>