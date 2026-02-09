<script setup lang="ts">
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
        link: 'https://fintech-dash-umber.vercel.app/'
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
</script>

<template>
    <section id="portfolio" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

            <!-- Header -->
            <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
                <div>
                    <h2 class="text-3xl md:text-4xl font-bold text-white mb-2">
                        <span class="text-brand-green">/</span> Deployed Systems
                    </h2>
                    <p class="text-gray-400 font-mono">Selected case studies from our mission logs</p>
                </div>
            </div>

            <!-- Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="(project, index) in projects" :key="index"
                    class="group relative rounded-xl overflow-hidden glass-card h-full flex flex-col">

                    <!-- Image Area with Overlay -->
                    <div class="relative h-52 overflow-hidden">
                        <!-- Color overlay that fades on hover -->
                        <div
                            class="absolute inset-0 bg-brand-navy/60 mix-blend-multiply group-hover:bg-transparent transition-all duration-500 z-10">
                        </div>
                        <!-- Image zoom effect -->
                        <img :src="project.image" :alt="project.title"
                            class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">

                        <!-- Category Tag -->
                        <div
                            class="absolute top-4 left-4 z-20 px-3 py-1 bg-black/50 backdrop-blur-md border border-white/10 rounded-full text-xs font-mono text-brand-cyan">
                            {{ project.category }}
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="p-6 flex flex-col flex-grow">
                        <div class="flex justify-between items-start mb-4">
                            <h3 class="text-xl font-bold text-white group-hover:text-brand-green transition-colors">{{
                                project.title }}</h3>
                            <a :href="project.link"
                                class="w-8 h-8 rounded-full border border-white/10 flex items-center justify-center text-gray-400 hover:bg-brand-cyan hover:border-brand-cyan hover:text-black transition-all transform hover:-rotate-45">
                                <i class="ph ph-arrow-right"></i>
                            </a>
                        </div>

                        <p class="text-gray-400 text-sm mb-6 line-clamp-3 flex-grow leading-relaxed">{{
                            project.description }}</p>

                        <!-- Tech Tags -->
                        <div class="pt-4 border-t border-white/5 flex flex-wrap gap-2">
                            <span v-for="tag in project.tech" :key="tag"
                                class="text-[10px] font-mono text-gray-500 bg-white/5 px-2 py-1 rounded border border-transparent group-hover:border-brand-green/20 transition-colors">
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
.glass-card {
    background: rgba(11, 18, 33, 0.4);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.05);
}
</style>