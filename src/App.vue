<script setup lang="ts">
import { onMounted, onUnmounted, ref, nextTick } from 'vue';
import Lenis from '@studio-freight/lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

import Preloader from './components/Preloader.vue';
import CustomCursor from './components/CustomCursor.vue';
import CircuitBackground from './components/ui/CircuitBackground.vue';
import NavBar from './components/NavBar.vue';
import HeroSection from './components/HeroSection.vue';
import AboutSection from './components/AboutSection.vue';
import ServicesSection from './components/ServicesSection.vue';
import WhyChooseUs from './components/WhyChooseUs.vue';
import PortfolioComponent from './components/PortfolioComponent.vue';
import TechComponents from './components/TechComponents.vue';
import TestimonialsSection from './components/TestimonialsSection.vue';
import StatsSection from './components/StatsSection.vue';
import FAQSection from './components/FAQSection.vue';
import ContactForm from './components/ContactForm.vue';

gsap.registerPlugin(ScrollTrigger);

let lenis: Lenis;

onMounted(() => {
    document.body.style.overflow = 'hidden';
});

const initLenis = () => {
   lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true,
      wheelMultiplier: 1,
      smoothTouch: false,
      touchMultiplier: 2,
      infinite: false,
   });

   lenis.on('scroll', ScrollTrigger.update);

   gsap.ticker.add((time) => {
      lenis.raf(time * 1000);
   });


};

const handleLoaded = () => {
    document.body.style.overflow = '';
    nextTick(() => {
        initLenis();
        ScrollTrigger.refresh();
    });
};

onUnmounted(() => {
   if (lenis) lenis.destroy();
   gsap.ticker.remove((time) => {
      if (lenis) lenis.raf(time * 1000);
   });
});

const scrollTo = (id: string) => {
   if (lenis) lenis.scrollTo(id, { offset: -50, duration: 1.5 });
};
</script>

<template>
   <Preloader @loaded="handleLoaded" />
   <CustomCursor />
   
   <main class="antialiased overflow-x-hidden">
      <CircuitBackground />
      <NavBar @scroll-to="scrollTo" />

      <HeroSection @scroll-to="scrollTo" />
      <AboutSection />
      <ServicesSection />
      <WhyChooseUs />
      <PortfolioComponent />
      <TechComponents />
      <TestimonialsSection />
      <StatsSection />
      <FAQSection />
      <ContactForm />

      <footer class="py-12 border-t border-white/5 bg-brand-dark relative z-10">
         <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <img src="/logo.svg" alt="Logo" class="w-6 h-6 object-contain" />
                <span class="text-white font-bold tracking-tight">Fullstack<span class="text-brand-cyan">Master</span></span>
            </div>
            <p class="text-gray-500 text-sm font-mono tracking-wide">
               © {{ new Date().getFullYear() }} Fullstack Master. All Systems Operational.
            </p>
         </div>
      </footer>
   </main>
</template>