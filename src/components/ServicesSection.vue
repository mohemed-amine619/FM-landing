<script setup lang="ts">
import type { Service } from '../types';

const services: Service[] = [
    {
        title: 'Fullstack Development',
        desc: 'Complete web solutions using Vue, React, Laravel and scalable cloud infrastructure.',
        icon: 'ph-code',
        tags: ['Vue.js', 'React', 'Laravel', 'PostgreSQL']
    },
    {
        title: 'UI/UX Design',
        desc: 'Cyberpunk, minimalist, or corporate. We craft interfaces that users love to interact with.',
        icon: 'ph-paint-brush',
        tags: ['Figma', 'Tailwind', 'Motion', 'Prototyping']
    },
    {
        title: 'Mobile Engineering',
        desc: 'Cross-platform mobile applications that perform like native on iOS and Android.',
        icon: 'ph-device-mobile',
        tags: ['React Native', 'Flutter', 'iOS', 'Android']
    },
    {
        title: 'Automation & AI',
        desc: 'Streamline operations with custom Python scripts, n8n workflows, and AI integration.',
        icon: 'ph-robot',
        tags: ['Python', 'n8n', 'OpenAI', 'Zapier']
    },
    {
        title: 'Cloud & DevOps',
        desc: 'Secure, scalable infrastructure design with automated CI/CD deployment pipelines.',
        icon: 'ph-cloud-arrow-up',
        tags: ['AWS', 'Docker', 'Kubernetes', 'GitHub Actions']
    },
    {
        title: 'SEO & Performance',
        desc: 'Technical SEO optimization and speed enhancements for maximum visibility.',
        icon: 'ph-rocket-launch',
        tags: ['Core Web Vitals', 'Analytics', 'PageSpeed', 'SSR']
    }
];
</script>

<template>
    <section id="services" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight"><span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">/</span> Capabilities</h2>
                <p class="text-gray-400 font-sans text-lg font-light">End-to-end development & infrastructure</p>
            </div>

            <!-- Updated grid to 3 columns on large screens for better balance with 6 items -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div v-for="(service, index) in services" :key="index"
                    class="glass-card p-6 rounded-xl group relative overflow-hidden h-full flex flex-col">
                    <!-- Hover Glow -->
                    <div
                        class="absolute -right-10 -top-10 w-32 h-32 bg-brand-cyan/10 rounded-full blur-[50px] group-hover:bg-brand-green/10 transition-colors duration-500">
                    </div>

                    <div
                        class="mb-6 inline-block p-3 rounded-xl bg-white/[0.03] border border-white/[0.05] text-brand-cyan group-hover:text-brand-green group-hover:bg-white/[0.05] transition-all duration-300 w-fit">
                        <i :class="['ph', service.icon, 'text-3xl']"></i>
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