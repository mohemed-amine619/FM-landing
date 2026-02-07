<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import type { NavItem } from '../types';

const isMobileMenuOpen = ref(false);
const isScrolled = ref(false);

const navItems: NavItem[] = [
    { name: 'Home', href: '#home' },
    { name: 'Services', href: '#services' },
    { name: 'Tech', href: '#tech' },
    { name: 'Contact', href: '#contact' },
];

const handleScroll = () => {
    isScrolled.value = window.scrollY > 50;
};

const scrollTo = (id: string) => {
    const el = document.querySelector(id);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
        isMobileMenuOpen.value = false;
    }
};

onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<template>
    <nav class="fixed w-full z-50 transition-all duration-300"
        :class="isScrolled ? 'bg-brand-dark/90 backdrop-blur-lg border-b border-white/5' : 'bg-transparent'">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <!-- Logo -->
                <div class="flex items-center gap-3 group cursor-pointer" @click="scrollTo('#home')">
                    <!-- Note: Put image.png in your public folder -->
                    <img src="../../public/logo.png" alt="Fullstack Master"
                        class="h-10 w-auto object-contain drop-shadow-[0_0_5px_rgba(6,182,212,0.5)] transition-transform hover:scale-105">
                    <div
                        class="font-sans font-bold text-xl tracking-wider uppercase flex flex-col leading-none md:block md:leading-normal">
                        <span class="text-white">Fullstack</span>
                        <span class="text-brand-cyan">Master</span>
                    </div>
                </div>

                <!-- Desktop Menu -->
                <div class="hidden md:block">
                    <div class="flex items-center space-x-8">
                        <a v-for="item in navItems" :key="item.name" @click.prevent="scrollTo(item.href)"
                            :href="item.href"
                            class="text-gray-300 hover:text-brand-green font-mono text-sm transition-colors duration-200 cursor-pointer">
                            <span class="text-brand-cyan mr-1">&lt;</span>{{ item.name }}<span
                                class="text-brand-cyan">/&gt;</span>
                        </a>
                        <button @click="scrollTo('#contact')"
                            class="px-6 py-2 border border-brand-cyan text-brand-cyan hover:bg-brand-cyan hover:text-brand-dark font-bold font-mono text-sm transition-all duration-300 rounded-sm">
                            START_PROJECT
                        </button>
                    </div>
                </div>

                <!-- Mobile Toggle -->
                <div class="md:hidden">
                    <button @click="isMobileMenuOpen = !isMobileMenuOpen" class="text-gray-300 hover:text-white">
                        <i :class="isMobileMenuOpen ? 'ph ph-x' : 'ph ph-list'" class="text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div v-if="isMobileMenuOpen" class="md:hidden bg-brand-navy border-b border-white/10">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a v-for="item in navItems" :key="item.name" @click.prevent="scrollTo(item.href)" :href="item.href"
                    class="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-white/5 cursor-pointer">
                    {{ item.name }}
                </a>
            </div>
        </div>
    </nav>
</template>