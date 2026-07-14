<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

interface Project {
    title: string;
    category: string;
    image: string;
    description: string;
    tech: string[];
    link: string;
}

const projects: Project[] = [
    {
        title: 'Neon FinTech Dashboard',
        category: 'FinTech / SaaS',
        image: 'https://placehold.co/600x400/0b1221/06b6d4?text=FinTech+Dashboard', // Replace with real screenshots
        description: 'Real-time crypto trading platform processing high-frequency data via WebSockets. Features dark mode UI and sub-second latency.',
        tech: ['Laravel', 'Vue.js', 'Reverb', 'Tailwind'],
        link: 'https://vue-dash-fm.vercel.app/'
    },
    {
        title: 'CyberCommerce Core',
        category: 'E-Commerce',
        image: 'https://placehold.co/600x400/0b1221/4ade80?text=E-Commerce+Platform',
        description: 'Headless e-commerce architecture handling 50k+ daily transactions. Integrated with Stripe Connect and custom inventory AI.',
        tech: ['Nuxt.js', 'Laravel API', 'Redis', 'AWS'],
        link: '#'
    },
    {
        title: 'AutoPilot CRM',
        category: 'Automation Tool',
        image: 'https://placehold.co/600x400/0b1221/a855f7?text=CRM+Automation',
        description: 'Custom CRM with automated email sequences and lead scoring. Built to replace expensive enterprise software for a mid-sized agency.',
        tech: ['Python', 'Django', 'React', 'PostgreSQL'],
        link: '#'
    }
];

const sectionRef = ref(null);
const headerRef = ref(null);
const projectsRef = ref<HTMLElement[]>([]);

onMounted(() => {
    // Header Reveal
    gsap.fromTo(headerRef.value, 
        { x: -50, opacity: 0 }, 
        { 
            x: 0, opacity: 1, duration: 0.8, ease: "power3.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 80%" }
        }
    );

    // Projects Staggered Reveal
    gsap.fromTo(projectsRef.value, 
        { y: 100, opacity: 0 }, 
        { 
            y: 0, opacity: 1, duration: 1.0, stagger: 0.15, ease: "power4.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 70%" }
        }
    );
});
</script>

<template>
    <section id="portfolio" ref="sectionRef" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

            <!-- Header -->
            <div ref="headerRef" class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
                <div>
                    <h2 class="text-4xl md:text-5xl font-bold text-white mb-2 tracking-tight">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">/</span> Selected Work
                    </h2>
                    <p class="text-slate-400 font-sans font-light text-lg mt-2">Case studies from enterprise deployments</p>
                </div>
            </div>

            <!-- Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="(project, index) in projects" :key="index" ref="projectsRef"
                    class="group relative rounded-xl overflow-hidden glass-card h-full flex flex-col">

                    <!-- Image Area with Overlay -->
                    <div class="relative h-52 overflow-hidden">
                        <!-- Color overlay that fades on hover -->
                        <div
                            class="absolute inset-0 bg-brand-dark/40 group-hover:bg-transparent transition-all duration-700 z-10">
                        </div>
                        <!-- Image zoom effect -->
                        <img :src="project.image" :alt="project.title"
                            class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">

                        <!-- Category Tag -->
                        <div
                            class="absolute top-4 left-4 z-20 px-3 py-1 bg-black/60 backdrop-blur-xl border border-white/10 rounded-full text-xs font-medium text-white shadow-lg">
                            {{ project.category }}
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="p-6 flex flex-col flex-grow">
                        <div class="flex justify-between items-start mb-4">
                            <h3 class="text-xl font-semibold text-white group-hover:text-brand-green transition-colors">{{
                                project.title }}</h3>
                            <a :href="project.link"
                                class="w-8 h-8 rounded-full border border-white/10 flex items-center justify-center text-gray-400 hover:bg-brand-cyan hover:border-brand-cyan hover:text-black transition-all transform hover:-rotate-45">
                                <i class="ph ph-arrow-right"></i>
                            </a>
                        </div>

                        <p class="text-gray-400 text-sm mb-6 line-clamp-3 flex-grow leading-relaxed">{{
                            project.description }}</p>

                        <!-- Tech Tags -->
                        <div class="pt-5 border-t border-white/[0.05] flex flex-wrap gap-2">
                            <span v-for="tag in project.tech" :key="tag"
                                class="text-xs font-medium text-gray-400 bg-white/[0.02] px-2.5 py-1 rounded-full border border-white/[0.05]">
                                {{ tag }}
                            </span>
                        </div>
                    </div>

                    <!-- Hover Border Glow -->
                    <div
                        class="absolute inset-0 border border-white/5 rounded-xl group-hover:border-brand-cyan/30 pointer-events-none transition-colors duration-300">
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
/* Scoped styles omitted, using global glass-card */
</style>