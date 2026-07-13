<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['scroll-to']);

// --- Typing Effect Logic ---
const typingText = ref('');
const phrases = [
    'Enterprise Management Systems',
    'Scalable Digital Infrastructures',
    'Quantitative Financial Solutions',
    'Exceptional User Experiences'
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

        <!-- 1. Background Grid Effect (Sophisticated & Moving) -->
        <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
            <!-- Grid Pattern -->
            <div
                class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.04)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.04)_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_0%,#000_70%,transparent_100%)] animate-grid">
            </div>
            <!-- Ambient glow -->
            <div
                class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] opacity-20 pointer-events-none">
                <div class="absolute inset-0 bg-gradient-to-b from-brand-cyan/20 to-transparent blur-[100px] rounded-full"></div>
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 text-center relative z-20">

            <!-- Announcement Pill -->
            <div class="animate-fade-in-up flex justify-center mb-8">
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-brand-cyan/30 bg-brand-cyan/10 backdrop-blur-md shadow-[0_0_15px_rgba(4,154,181,0.15)] text-sm font-medium text-brand-cyan">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-brand-cyan opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-brand-cyan"></span>
                    </span>
                    Available for New Enterprise Projects
                </div>
            </div>

            <!-- 2. Animated Logo Container -->
            <div class="mb-10 relative inline-block group animate-float">
                <!-- Dual-Layer Pulsing Glow -->
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[180%] h-[180%] bg-brand-cyan/25 blur-[90px] rounded-full animate-pulse-slow pointer-events-none group-hover:bg-brand-cyan/40 transition-colors duration-700">
                </div>
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[130%] h-[130%] bg-brand-green/25 blur-[60px] rounded-full mix-blend-screen pointer-events-none group-hover:bg-brand-green/40 transition-colors duration-700">
                </div>

                <!-- Logo Image -->
                <div class="relative z-10 w-28 h-28 md:w-36 md:h-36 mx-auto bg-brand-dark/60 rounded-[2rem] border border-brand-cyan/30 flex items-center justify-center shadow-[0_0_30px_rgba(4,154,181,0.3)] p-6 backdrop-blur-2xl group-hover:border-brand-green/60 transition-all duration-700 group-hover:shadow-[0_0_80px_rgba(37,220,125,0.5)] group-hover:-translate-y-3 overflow-hidden">
                    <!-- Inner subtle gradient -->
                    <div class="absolute inset-0 bg-gradient-to-br from-brand-cyan/30 via-transparent to-brand-green/30 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
                    <img src="/logo.svg" alt="Logo" class="relative z-10 w-full h-full object-contain filter drop-shadow-[0_0_25px_rgba(4,154,181,0.7)] group-hover:drop-shadow-[0_0_40px_rgba(37,220,125,1)] transition-all duration-700 group-hover:scale-110">
                </div>
            </div>

            <!-- 3. Dynamic Typing Headline -->
            <div class="animate-fade-in-up">
                <h1 class="text-4xl md:text-6xl lg:text-7xl font-extrabold text-white mb-6 tracking-tight h-24 md:h-auto font-sans leading-tight drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]">
                    Engineering <span
                        class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan via-brand-purple to-brand-green drop-shadow-[0_0_25px_rgba(4,154,181,0.6)]">{{
                        typingText }}</span><span class="animate-blink text-brand-cyan drop-shadow-[0_0_15px_rgba(4,154,181,1)]">|</span>
                </h1>

                <p class="mt-6 max-w-2xl mx-auto text-lg md:text-xl text-slate-400 font-light leading-relaxed">
                    We craft high-performance digital infrastructure for ambitious businesses. From complex <span class="text-white font-medium">enterprise systems</span> and scalable <span class="text-white font-medium">backend architectures</span> to advanced <span class="text-white font-medium">algorithmic solutions</span>, we build platforms that drive measurable growth.
                </p>
            </div>

            <!-- 4. Enhanced Buttons -->
            <div class="mt-12 flex flex-col sm:flex-row gap-6 justify-center items-center animate-fade-in-up" style="animation-delay: 0.2s;">
                <!-- Primary Glow Button -->
                <button @click="$emit('scroll-to', '#services')"
                    class="glow-button-primary flex items-center gap-2">
                    <span class="relative z-10 font-sans tracking-wide">Explore Services</span>
                    <i class="ph-bold ph-arrow-right"></i>
                </button>

                <!-- Secondary Outline Button -->
                <button @click="$emit('scroll-to', '#contact')"
                    class="glow-button flex items-center gap-2">
                    <span class="font-sans text-sm tracking-wide">Book a Consultation</span>
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