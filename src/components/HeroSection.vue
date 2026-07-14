<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

const emit = defineEmits(['scroll-to']);

// --- Typing Effect Logic ---
const typingText = ref('');
const phrases = [
    'High-Performance Web Apps',
    'Custom AI Automations',
    'Enterprise Data Dashboards',
    'Scalable Cloud Architectures',
    'Premium SaaS Platforms'
];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeSpeed = 100;
let timeoutId: number;

const type = () => {
    const currentPhrase = phrases[phraseIndex];
    if (!currentPhrase) return;

    if (isDeleting) {
        typingText.value = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 40; 
    } else {
        typingText.value = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 80; 
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
        isDeleting = true;
        typeSpeed = 2500; 
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 500; 
    }

    timeoutId = setTimeout(type, typeSpeed);
};

// --- Advanced Interactive Refs ---
const parallaxContainer = ref<HTMLElement | null>(null);
const logoCardRef = ref<HTMLElement | null>(null);
const spotlightRef = ref<HTMLElement | null>(null);
const titleRef = ref<HTMLElement | null>(null);
const subtitleRef = ref<HTMLElement | null>(null);
const pillRef = ref<HTMLElement | null>(null);

onMounted(() => {
    timeoutId = setTimeout(type, 1500); // Start typing after reveal

    // Initial float animation for the glass shapes
    gsap.utils.toArray('.hero-shape').forEach((shape: any, i: number) => {
        gsap.to(shape, {
            y: "+=30",
            rotation: i % 2 === 0 ? 15 : -15,
            duration: gsap.utils.random(4, 7),
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut",
            delay: i * 0.7
        });
    });

    // Cinematic Reveal Sequence (start immediately, let Preloader cover it if needed)
    const tl = gsap.timeline({ delay: 0.2 });

    if (pillRef.value) {
        tl.fromTo(pillRef.value, 
            { y: 30, autoAlpha: 0 },
            { y: 0, autoAlpha: 1, duration: 0.8, ease: 'power4.out' }
        );
    }
    
    if (logoCardRef.value) {
        tl.fromTo(logoCardRef.value,
            { scale: 0.8, autoAlpha: 0, rotationX: 20 },
            { scale: 1, autoAlpha: 1, rotationX: 0, duration: 1.0, ease: 'back.out(1.5)' },
            "-=0.6"
        );
    }

    if (titleRef.value) {
        tl.fromTo(titleRef.value,
            { y: 100, autoAlpha: 0, rotation: 2 },
            { y: 0, autoAlpha: 1, rotation: 0, duration: 1.0, ease: 'power4.out' },
            "-=0.8"
        );
    }

    if (subtitleRef.value) {
        tl.fromTo(subtitleRef.value,
            { y: 30, autoAlpha: 0 },
            { y: 0, autoAlpha: 1, duration: 0.8, ease: 'power3.out' },
            "-=0.8"
        );
    }

    const btns = gsap.utils.toArray('.hero-btn');
    if (btns.length > 0) {
        tl.fromTo(btns,
            { y: 20, autoAlpha: 0 },
            { y: 0, autoAlpha: 1, duration: 0.8, stagger: 0.15, ease: 'back.out(1.2)' },
            "-=0.6"
        );
    }
});

onUnmounted(() => {
    clearTimeout(timeoutId);
});
</script>

<template>
    <section id="home" ref="parallaxContainer" class="relative z-10 min-h-[100svh] flex items-center justify-center pt-20 pb-10 overflow-hidden">
        
        <!-- Interactive Spotlight -->
        <div ref="spotlightRef" class="pointer-events-none fixed top-0 left-0 w-[600px] h-[600px] rounded-full opacity-40 z-0 -translate-x-1/2 -translate-y-1/2 transform-gpu will-change-transform" style="background: radial-gradient(circle, rgba(4,154,181,0.2) 0%, rgba(37,220,125,0.05) 40%, transparent 70%);"></div>

        <!-- 1. Floating Glass Orbs -->
        <div class="absolute inset-0 pointer-events-none z-0">
            <!-- Large Frosted Orb -->
            <div data-depth="0.3" class="hero-shape absolute top-[20%] left-[10%] w-32 h-32 rounded-full border border-white/10 bg-gradient-to-br from-brand-cyan/20 to-transparent backdrop-blur-2xl shadow-[inset_0_1px_1px_rgba(255,255,255,0.2),0_10px_40px_-10px_rgba(4,154,181,0.3)]"></div>
            
            <!-- Floating Glass Hexagon -->
            <div data-depth="0.7" class="hero-shape absolute top-[65%] right-[15%] w-24 h-24 border border-white/10 bg-gradient-to-tr from-brand-green/20 to-transparent backdrop-blur-3xl shadow-[inset_0_1px_1px_rgba(255,255,255,0.2)]" style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"></div>
            
            <!-- Distant Glass Triangle -->
            <div data-depth="0.1" class="hero-shape absolute top-[30%] right-[30%] w-16 h-16 border-b border-r border-white/10 bg-gradient-to-tl from-brand-blue/20 to-transparent backdrop-blur-md rotate-45"></div>
        </div>

        <div class="max-w-7xl mx-auto px-4 text-center relative z-20 w-full flex flex-col items-center">

            <!-- Announcement Pill -->
            <div ref="pillRef" class="flex justify-center mb-10 opacity-0">
                <div class="inline-flex items-center gap-2 px-5 py-2 rounded-full border border-white/10 bg-white/[0.03] backdrop-blur-xl shadow-[0_0_20px_rgba(4,154,181,0.1),inset_0_1px_1px_rgba(255,255,255,0.1)] text-xs font-mono tracking-widest uppercase text-brand-cyan relative overflow-hidden group">
                    <span class="absolute inset-0 bg-gradient-to-r from-transparent via-brand-cyan/10 to-transparent -translate-x-full group-hover:translate-x-full duration-1000 ease-in-out"></span>
                    <span class="relative flex h-2 w-2 mr-1">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-brand-green opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-brand-green"></span>
                    </span>
                    Solo Expert • Accepting New Projects
                </div>
            </div>

            <!-- 2. 3D Animated Logo Container -->
            <div class="mb-12 relative inline-block group" style="perspective: 1000px;">
                <!-- Dual-Layer Pulsing Glow -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[200%] h-[200%] bg-brand-cyan/20 blur-[100px] rounded-full animate-pulse-slow pointer-events-none group-hover:bg-brand-cyan/40 transition-colors duration-1000 transform-gpu will-change-transform"></div>
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] h-[150%] bg-brand-green/20 blur-[80px] rounded-full pointer-events-none group-hover:bg-brand-green/40 transition-colors duration-1000 transform-gpu will-change-transform" style="animation-delay: 2s;"></div>

                <!-- 3D Card Base -->
                <div ref="logoCardRef" class="relative z-10 w-32 h-32 md:w-40 md:h-40 mx-auto bg-gradient-to-br from-white/[0.08] to-white/[0.01] rounded-[2.5rem] border border-white/10 flex items-center justify-center shadow-[inset_0_1px_1px_rgba(255,255,255,0.2),0_20px_60px_-15px_rgba(4,154,181,0.5)] backdrop-blur-3xl overflow-hidden cursor-pointer opacity-0 transform-style-3d">
                    <!-- Glass glare effect -->
                    <div class="absolute inset-0 bg-gradient-to-tr from-transparent via-white/[0.05] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>
                    <img src="/logo.svg" alt="Logo" class="relative z-10 w-full h-full object-contain filter drop-shadow-[0_0_25px_rgba(4,154,181,0.8)] group-hover:drop-shadow-[0_0_50px_rgba(37,220,125,1)] transition-all duration-700 ease-out translate-z-[50px]">
                </div>
            </div>

            <!-- 3. Cinematic Typing Headline -->
            <div class="mb-6 py-2 w-full max-w-5xl mx-auto flex flex-col items-center justify-center">
                <h1 ref="titleRef" class="text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-extrabold text-white tracking-tight min-h-[120px] md:min-h-[160px] font-sans leading-tight opacity-0 origin-bottom flex flex-wrap justify-center items-center gap-x-3 gap-y-2">
                    <span>I Architect</span>
                    <span class="relative flex items-center">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan via-brand-blue to-brand-green drop-shadow-[0_0_30px_rgba(4,154,181,0.5)]">{{ typingText }}</span>
                        <span class="inline-block ml-1 md:ml-2 w-1 md:w-2 h-[1em] bg-brand-cyan animate-blink shadow-[0_0_15px_rgba(4,154,181,1)]"></span>
                    </span>
                </h1>
            </div>

            <div class="overflow-hidden mb-12">
                <p ref="subtitleRef" class="max-w-3xl mx-auto text-lg md:text-xl text-slate-400 font-light leading-relaxed opacity-0">
                    I craft highly-performant digital infrastructure for ambitious businesses. From robust <span class="text-white font-medium">enterprise backends</span> to award-winning <span class="text-white font-medium">user experiences</span>, I build platforms that drive measurable growth.
                </p>
            </div>

            <!-- 4. Enhanced Magnetic Buttons -->
            <div class="flex flex-col sm:flex-row gap-6 justify-center items-center w-full mb-20">
                <!-- Primary Glow Button -->
                <div class="hero-btn opacity-0">
                    <button @click="$emit('scroll-to', '#about')"
                        class="glow-button-primary flex items-center gap-3 px-10 py-4 text-lg">
                        <span class="relative z-10 font-sans tracking-wide">Explore My Expertise</span>
                        <i class="ph-bold ph-arrow-right text-xl relative z-10"></i>
                    </button>
                </div>

                <!-- Secondary Outline Button -->
                <div class="hero-btn opacity-0">
                    <button @click="$emit('scroll-to', '#contact')"
                        class="glow-button flex items-center gap-2 px-8 py-4 text-base bg-transparent border-white/20 hover:bg-white/[0.05]">
                        <span class="font-sans tracking-wide">Work With Me</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Subtle Scroll Indicator -->
        <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 opacity-50 hover:opacity-100 transition-opacity cursor-pointer z-20" @click="$emit('scroll-to', '#about')">
            <span class="text-[10px] uppercase tracking-[0.3em] font-mono text-brand-cyan font-bold">Scroll</span>
            <div class="w-[2px] h-16 bg-white/10 relative overflow-hidden rounded-full">
                <div class="absolute top-0 left-0 w-full h-1/2 bg-gradient-to-b from-brand-cyan to-brand-green animate-scroll-down rounded-full shadow-[0_0_10px_rgba(4,154,181,0.8)]"></div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.animate-blink {
    animation: blink 0.8s step-end infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

.animate-pulse-slow {
    animation: pulse 6s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.transform-style-3d {
    transform-style: preserve-3d;
}

.translate-z-\[50px\] {
    transform: translateZ(50px);
}
</style>