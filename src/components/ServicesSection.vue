<script setup lang="ts">
import type { Service } from '../types';

const services: Service[] = [
    {
        title: 'Fullstack Development',
        desc: 'Complete web solutions using Vue, React, Node.js and scalable cloud infrastructure.',
        icon: 'ph-code',
        tags: ['Vue.js', 'React', 'Node.js', 'PostgreSQL']
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
    }
];
</script>

<template>
    <section id="services" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-white mb-4"><span class="text-brand-green">/</span>
                    Capabilities</h2>
                <p class="text-gray-400 font-mono">End-to-end development services</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div v-for="(service, index) in services" :key="index"
                    class="glass-card p-8 rounded-xl group relative overflow-hidden">
                    <div
                        class="absolute -right-10 -top-10 w-32 h-32 bg-brand-cyan/20 rounded-full blur-[50px] group-hover:bg-brand-green/20 transition-colors duration-500">
                    </div>

                    <div
                        class="mb-6 inline-block p-4 rounded-lg bg-white/5 text-brand-cyan group-hover:text-brand-green group-hover:scale-110 transition-all duration-300">
                        <i :class="['ph', service.icon, 'text-3xl']"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-brand-cyan transition-colors">{{
                        service.title }}</h3>
                    <p class="text-gray-400 text-sm leading-relaxed mb-4">{{ service.desc }}</p>

                    <ul class="space-y-2">
                        <li v-for="tag in service.tags" :key="tag"
                            class="flex items-center text-xs font-mono text-gray-500">
                            <span class="w-1.5 h-1.5 bg-brand-green rounded-full mr-2"></span>
                            {{ tag }}
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
</template>