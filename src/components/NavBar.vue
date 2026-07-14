<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import type { NavItem } from '../types';

const emit = defineEmits(['scroll-to']);
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
    emit('scroll-to', id);
    isMobileMenuOpen.value = false;
};

onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<template>
    <nav class="fixed w-full z-50 transition-all duration-500"
        :class="isScrolled ? 'glass-panel py-2' : 'bg-transparent py-4'">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <!-- Logo -->
                <div class="flex items-center gap-3 group cursor-pointer" @click="scrollTo('#home')">
                    <div class="relative flex items-center justify-center w-12 h-12 rounded-xl bg-white/[0.02] border border-white/[0.05] group-hover:border-brand-cyan/50 transition-all duration-500 overflow-hidden group-hover:shadow-[0_0_20px_rgba(4,154,181,0.4)]">
                        <div class="absolute inset-0 bg-gradient-to-br from-brand-cyan/30 to-brand-green/30 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <img src="/logo.svg" alt="Fullstack Master Logo"
                            class="relative h-7 w-auto object-contain drop-shadow-[0_0_12px_rgba(4,154,181,0.8)] transition-transform duration-500 group-hover:scale-110 group-hover:drop-shadow-[0_0_25px_rgba(37,220,125,1)]">
                    </div>
                    <div
                        class="font-sans font-bold text-xl tracking-tight flex flex-col leading-none md:block md:leading-normal">
                        <span class="text-white drop-shadow-md">Fullstack</span><span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green drop-shadow-lg">Master</span>
                    </div>
                </div>

                <!-- Desktop Menu -->
                <div class="hidden md:block">
                    <div class="flex items-center space-x-8">
                        <a v-for="item in navItems" :key="item.name" @click.prevent="scrollTo(item.href)"
                            :href="item.href"
                            class="text-gray-400 hover:text-white font-sans text-sm font-medium transition-colors duration-200 cursor-pointer relative group">
                            {{ item.name }}
                            <span class="absolute -bottom-1 left-0 w-0 h-[2px] bg-brand-cyan transition-all duration-300 group-hover:w-full rounded-full"></span>
                        </a>
                        <button @click="scrollTo('#contact')"
                            class="glow-button">
                            <span class="relative z-10 font-sans tracking-wide text-sm font-medium">Book Consultation</span>
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
        <div v-if="isMobileMenuOpen" class="md:hidden glass-panel">
            <div class="px-4 pt-2 pb-4 space-y-2">
                <a v-for="item in navItems" :key="item.name" @click.prevent="scrollTo(item.href)" :href="item.href"
                    class="block px-3 py-3 rounded-lg text-base font-medium text-slate-300 hover:text-white hover:bg-white/5 cursor-pointer transition-colors">
                    {{ item.name }}
                </a>
            </div>
        </div>
    </nav>
</template>