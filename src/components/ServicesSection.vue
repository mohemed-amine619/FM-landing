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
                <h2 class="text-3xl md:text-4xl font-bold text-white mb-4"><span class="text-brand-green">/</span>
                    Capabilities</h2>
                <p class="text-gray-400 font-mono">End-to-end development & automation</p>
            </div>

            <!-- Updated grid to 3 columns on large screens for better balance with 6 items -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div v-for="(service, index) in services" :key="index"
                    class="glass-card p-6 rounded-xl group relative overflow-hidden h-full flex flex-col">
                    <!-- Hover Glow -->
                    <div
                        class="absolute -right-10 -top-10 w-32 h-32 bg-brand-cyan/20 rounded-full blur-[50px] group-hover:bg-brand-green/20 transition-colors duration-500">
                    </div>

                    <div
                        class="mb-6 inline-block p-3 rounded-lg bg-white/5 text-brand-cyan group-hover:text-brand-green group-hover:scale-110 transition-all duration-300 w-fit">
                        <i :class="['ph', service.icon, 'text-3xl']"></i>
                    </div>

                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-brand-cyan transition-colors">{{
                        service.title }}</h3>
                    <p class="text-gray-400 text-sm leading-relaxed mb-4 flex-grow">{{ service.desc }}</p>

                    <div class="flex flex-wrap gap-2 mt-auto">
                        <span v-for="tag in service.tags" :key="tag"
                            class="inline-flex items-center text-xs font-mono text-gray-500 bg-white/5 px-2 py-1 rounded">
                            <span class="w-1.5 h-1.5 bg-brand-green rounded-full mr-2"></span>
                            {{ tag }}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.glass-card {
    background: rgba(11, 18, 33, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(6, 182, 212, 0.1);
    transition: all 0.3s ease;
}

.glass-card:hover {
    border-color: rgba(74, 222, 128, 0.5);
    transform: translateY(-5px);
    box-shadow: 0 10px 30px -10px rgba(74, 222, 128, 0.15);
}
</style>