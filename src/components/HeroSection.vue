<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['scroll-to']);

// --- Typing Effect Logic ---
const typingText = ref('');
const phrases = [
    'Scalable Web Solutions',
    'Robust Laravel Backends',
    'Interactive Vue Interfaces',
    'Next-Gen Automation'
];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeSpeed = 100;
let timeoutId: number;

const type = () => {
    const currentPhrase = phrases[phraseIndex];

    // FIX: Guard clause to satisfy TypeScript strict null checks
    if (!currentPhrase) return;

    if (isDeleting) {
        typingText.value = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 50; // Deleting is faster
    } else {
        typingText.value = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 100; // Typing speed
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
        isDeleting = true;
        typeSpeed = 2000; // Pause at end of phrase
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; // Pause before new phrase
    }

    timeoutId = setTimeout(type, typeSpeed);
};

onMounted(() => {
    timeoutId = setTimeout(type, 1000);
});

onUnmounted(() => {
    clearTimeout(timeoutId);
});
</script>

<template>
    <section id="home" class="relative z-10 min-h-screen flex items-center justify-center pt-20 overflow-hidden">

        <!-- 1. Background Grid Effect (Cyberpunk Blueprint) -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <!-- Grid Pattern -->
            <div
                class="absolute inset-0 bg-[linear-gradient(rgba(6,182,212,0.05)_1px,transparent_1px),linear-gradient(90deg,rgba(6,182,212,0.05)_1px,transparent_1px)] bg-[size:4rem_4rem]">
            </div>
            <!-- Radial Mask to fade grid at edges -->
            <div
                class="absolute inset-0 bg-brand-dark [mask-image:radial-gradient(ellipse_at_center,transparent_20%,black_70%)]">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 text-center relative z-20">

            <!-- 2. Animated Logo Container -->
            <div class="mb-10 relative inline-block group">
                <!-- Dual-Layer Pulsing Glow -->
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[140%] h-[140%] bg-brand-cyan/20 blur-[80px] rounded-full animate-pulse-slow">
                </div>
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[100%] h-[100%] bg-brand-green/10 blur-[40px] rounded-full mix-blend-screen">
                </div>

                <!-- Logo Image -->
                <img src="/logo.svg" alt="Fullstack Master Logo"
                    class="relative z-10 w-full max-w-lg md:max-w-2xl mx-auto drop-shadow-[0_0_15px_rgba(6,182,212,0.3)] transition-transform duration-700 hover:scale-105 hover:drop-shadow-[0_0_30px_rgba(74,222,128,0.5)] animate-float">
            </div>

            <!-- 3. Dynamic Typing Headline -->
            <h1 class="text-3xl md:text-5xl lg:text-6xl font-bold text-white mb-6 tracking-tight h-20 md:h-auto">
                Building <span
                    class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green font-mono">{{
                    typingText }}</span><span class="animate-blink text-brand-cyan">_</span>
            </h1>

            <p class="mt-4 max-w-2xl mx-auto text-lg md:text-xl text-gray-400 font-light font-mono leading-relaxed">
                Architecting the digital future. We build high-performance web solutions with <span
                    class="text-brand-cyan">Laravel</span> & <span class="text-brand-green">Vue.js</span>.
            </p>

            <!-- 4. Enhanced Buttons -->
            <div class="mt-12 flex flex-col sm:flex-row gap-6 justify-center items-center">

                <!-- Primary Glow Button -->
                <button @click="$emit('scroll-to', '#services')"
                    class="group relative px-8 py-4 bg-brand-cyan/10 border border-brand-cyan/50 text-brand-cyan font-bold tracking-widest uppercase rounded-sm overflow-hidden transition-all duration-300 hover:bg-brand-cyan hover:text-brand-dark hover:shadow-[0_0_40px_rgba(6,182,212,0.6)]">
                    <span class="relative z-10">Explore Services</span>
                    <!-- Shine Effect -->
                    <div
                        class="absolute inset-0 h-full w-full scale-0 rounded-sm transition-all duration-300 group-hover:scale-100 group-hover:bg-brand-cyan/20">
                    </div>
                </button>

                <!-- Secondary Outline Button -->
                <button @click="$emit('scroll-to', '#contact')"
                    class="px-8 py-4 border border-gray-700 text-gray-300 font-mono text-sm tracking-wider uppercase rounded-sm transition-all duration-300 hover:border-brand-green hover:text-brand-green hover:bg-brand-green/5">
                    // Let's Talk Code
                </button>
            </div>
        </div>
    </section>
</template>

<style scoped>
.animate-blink {
    animation: blink 1s step-end infinite;
}

@keyframes blink {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0;
    }
}

.animate-pulse-slow {
    animation: pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>