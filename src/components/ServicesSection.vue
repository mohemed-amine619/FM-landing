<script setup lang="ts">
import { onMounted, ref } from 'vue';
import type { Service } from '../types';
import gsap from 'gsap';

const services: Service[] = [
    {
        title: 'Enterprise Web Applications & ERPs',
        desc: 'Development of custom management systems and complex business logic, designed to streamline internal operations.',
        icon: 'ph-buildings',
        tags: ['Laravel', 'Vue.js']
    },
    {
        title: 'Scalable Backend Architecture & APIs',
        desc: 'Engineering robust API designs, advanced data logic, and seamless third-party integrations to power highly scalable systems.',
        icon: 'ph-database',
        tags: ['Go', 'Laravel']
    },
    {
        title: 'Quantitative Trading Solutions',
        desc: 'Custom algorithm design, automated bot architecture, and precise execution scripts tailored for high-performance financial strategies.',
        icon: 'ph-chart-line-up',
        tags: ['Python', 'MetaTrader 5']
    },
    {
        title: 'Modern Frontend Development',
        desc: 'Creation of pixel-perfect, highly interactive, and fully responsive user interfaces focusing on exceptional user experiences.',
        icon: 'ph-desktop',
        tags: ['Vue.js', 'Tailwind CSS']
    }
];

const sectionRef = ref(null);
const headerRef = ref(null);
const cardsRef = ref<HTMLElement[]>([]);

onMounted(() => {
    // Header Blur to Sharp Reveal
    gsap.fromTo(headerRef.value, 
        { y: 50, opacity: 0, filter: 'blur(10px)' }, 
        { 
            y: 0, opacity: 1, filter: 'blur(0px)', duration: 0.5, ease: "power3.out",
            scrollTrigger: { trigger: headerRef.value, start: "top 85%" }
        }
    );

    // Cards Staggered Fade Up
    gsap.fromTo(cardsRef.value, 
        { y: 80, opacity: 0, scale: 0.95 }, 
        { 
            y: 0, opacity: 1, scale: 1, duration: 0.4, stagger: 0.055, ease: "back.out(1.2)",
            scrollTrigger: { trigger: sectionRef.value, start: "top 75%" }
        }
    );
});
</script>

<template>
    <section id="services" ref="sectionRef" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div ref="headerRef" class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight"><span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">/</span> Capabilities</h2>
                <p class="text-gray-400 font-sans text-lg font-light">End-to-end development & infrastructure</p>
            </div>

            <!-- Updated grid to 2 columns on large screens for better balance with 4 items -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">
                <div v-for="(service, index) in services" :key="index" ref="cardsRef"
                    class="glass-card p-6 rounded-xl group relative overflow-hidden h-full flex flex-col">
                    <!-- Hover Glow -->
                    <div
                        class="absolute -right-10 -top-10 w-32 h-32 bg-brand-cyan/10 rounded-full blur-[50px] group-hover:bg-brand-green/10 transition-colors duration-500">
                    </div>

                    <div
                        class="mb-6 inline-block p-3 rounded-xl bg-white/[0.03] border border-white/[0.05] text-brand-cyan group-hover:text-brand-green group-hover:bg-brand-cyan/20 group-hover:border-brand-cyan/50 group-hover:shadow-[0_0_30px_rgba(4,154,181,0.8)] transition-all duration-500 w-fit">
                        <i :class="['ph', service.icon, 'text-3xl group-hover:animate-pulse']"></i>
                    </div>

                    <h3 class="text-xl font-semibold text-white mb-3 group-hover:text-gray-200 transition-colors">{{
                        service.title }}</h3>
                    <p class="text-gray-400 text-sm leading-relaxed mb-6 font-light flex-grow">{{ service.desc }}</p>

                    <div class="flex flex-wrap gap-2 mt-auto">
                        <span v-for="tag in service.tags" :key="tag"
                            class="inline-flex items-center text-xs font-medium text-gray-400 bg-white/[0.03] border border-white/[0.05] px-2.5 py-1 rounded-full">
                            {{ tag }}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
/* Scoped styles omitted, using global glass-card */
</style>