<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

interface Testimonial {
    name: string;
    role: string;
    company: string;
    content: string;
    rating: number;
}

const allTestimonials: Testimonial[] = [
    {
        name: 'Tarek M.',
        role: 'Directeur Général',
        company: 'Private Client',
        content: 'L\'infrastructure cloud sur mesure développée pour notre gestion des données a été une véritable révolution. La fiabilité et la sécurité de l\'architecture sont d\'un niveau exceptionnel.',
        rating: 5
    },
    {
        name: 'Sarah L.',
        role: 'VP of Engineering',
        company: 'Tech Startup',
        content: 'The architectural decisions made by him were spot on. We were able to scale our backend to handle millions of real-time requests without a single downtime incident. His DevOps expertise is unmatched.',
        rating: 5
    },
    {
        name: 'Amine B.',
        role: 'Directeur Systèmes d\'Information',
        company: 'Financial Services',
        content: 'L\'intégration de notre nouvelle API est d\'une fluidité remarquable. Le système de traitement sécurisé des paiements fonctionne sans la moindre faille. Un travail d\'architecture de très haut niveau.',
        rating: 5
    },
    {
        name: 'Elena R.',
        role: 'Product Manager',
        company: 'Enterprise Client',
        content: 'We needed a highly scalable backend to handle our massive user base. The final product exceeded our expectations. The real-time data processing is flawless and highly optimized.',
        rating: 5
    },
    {
        name: 'Karim S.',
        role: 'CTO',
        company: 'SaaS Platform',
        content: 'La refonte de notre plateforme de services a été gérée de main de maître. La nouvelle infrastructure gère désormais des pics de trafic massifs lors de nos lancements sans aucun ralentissement.',
        rating: 5
    },
    {
        name: 'Lydia A.',
        role: 'Fondatrice d\'Agence Tech',
        company: 'Digital Agency',
        content: 'Nous sommes ravis de la livraison de notre nouveau tableau de bord. L\'interface est rapide, moderne et le résultat est totalement pixel-perfect. L\'expertise technique est indéniable.',
        rating: 5
    }
];

// Split into two rows for the marquee
const row1 = allTestimonials.slice(0, 3);
const row2 = allTestimonials.slice(3, 6);

const sectionRef = ref(null);
const headerRef = ref(null);

onMounted(() => {
    // Header Reveal
    gsap.fromTo(headerRef.value, 
        { y: -30, opacity: 0 }, 
        { 
            y: 0, opacity: 1, duration: 0.4, ease: "power3.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 80%" }
        }
    );
});
</script>

<template>
    <section id="testimonials" ref="sectionRef" class="py-24 relative z-10 overflow-hidden bg-black/20 border-y border-white/[0.02]">

        <!-- Glow Accents -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-[1px] bg-gradient-to-r from-transparent via-brand-cyan/20 to-transparent"></div>
        <!-- Background Atmosphere (Glowing Orbs) -->
        <div class="absolute inset-0 pointer-events-none opacity-50 transform-gpu">
            <div
                class="absolute top-20 left-0 w-[500px] h-[500px] rounded-full -translate-x-1/2 animate-pulse-glow"
                style="background: radial-gradient(circle, rgba(4,154,181,0.15) 0%, transparent 60%);">
            </div>
            <div
                class="absolute bottom-20 right-0 w-[500px] h-[500px] rounded-full translate-x-1/2 animate-pulse-glow" style="animation-delay: 1.5s; background: radial-gradient(circle, rgba(37,220,125,0.15) 0%, transparent 60%);">
            </div>
            <div
                class="absolute top-1/2 left-1/2 w-[800px] h-[300px] rounded-full -translate-x-1/2 -translate-y-1/2 animate-pulse-slow pointer-events-none"
                style="background: radial-gradient(ellipse, rgba(129,140,248,0.1) 0%, transparent 60%);">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <!-- Section Header -->
            <div ref="headerRef" class="text-center mb-20">
                <div class="inline-flex items-center gap-3 px-5 py-2 rounded-full border border-white/10 bg-white/[0.02] backdrop-blur-md mb-6">
                    <span class="w-2 h-2 rounded-full bg-brand-cyan animate-pulse"></span>
                    <span class="text-xs font-mono text-brand-cyan uppercase tracking-widest">Client Intel</span>
                </div>
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight">
                    Trusted by <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Industry Leaders</span>
                </h2>
            </div>
        </div>

        <!-- Infinite Marquee Section -->
        <div class="relative w-full flex flex-col gap-6 md:gap-8 overflow-hidden py-4">
            <!-- Left Gradient Fade -->
            <div class="absolute top-0 left-0 w-24 md:w-64 h-full bg-gradient-to-r from-[#0a0a0a] to-transparent z-20 pointer-events-none"></div>
            <!-- Right Gradient Fade -->
            <div class="absolute top-0 right-0 w-24 md:w-64 h-full bg-gradient-to-l from-[#0a0a0a] to-transparent z-20 pointer-events-none"></div>

            <!-- Row 1: Marquee Left -->
            <div class="flex marquee-left w-max hover-pause">
                <div class="flex gap-6 md:gap-8 px-3 md:px-4 shrink-0" v-for="n in 3" :key="'r1-'+n">
                    <!-- Duplicate the items to create seamless loop -->
                    <div v-for="(item, index) in row1" :key="index" class="glass-card w-[320px] md:w-[450px] p-6 md:p-8 rounded-3xl flex flex-col relative group border border-white/[0.05] hover:border-brand-cyan/30 transition-colors duration-500">
                        <div class="flex gap-1 mb-4">
                            <i v-for="star in 5" :key="star" class="ph-fill ph-star text-sm md:text-base text-brand-cyan"></i>
                        </div>
                        <p class="text-gray-300 font-light text-base md:text-lg leading-relaxed flex-grow mb-8">
                            "{{ item.content }}"
                        </p>
                        <div class="flex items-center gap-4 mt-auto">
                            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-brand-cyan/20 to-brand-green/20 border border-white/10 flex items-center justify-center">
                                <span class="text-white font-bold">{{ item.name.charAt(0) }}</span>
                            </div>
                            <div>
                                <h4 class="text-white font-semibold tracking-wide">{{ item.name }}</h4>
                                <p class="text-xs md:text-sm text-gray-500 font-mono mt-1">{{ item.role }} @ <span class="text-brand-cyan">{{ item.company }}</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Row 2: Marquee Right -->
            <div class="flex marquee-right w-max hover-pause mt-4">
                <div class="flex gap-6 md:gap-8 px-3 md:px-4 shrink-0" v-for="n in 3" :key="'r2-'+n">
                    <div v-for="(item, index) in row2" :key="index" class="glass-card w-[320px] md:w-[450px] p-6 md:p-8 rounded-3xl flex flex-col relative group border border-white/[0.05] hover:border-brand-green/30 transition-colors duration-500">
                        <div class="flex gap-1 mb-4">
                            <i v-for="star in 5" :key="star" class="ph-fill ph-star text-sm md:text-base text-brand-green"></i>
                        </div>
                        <p class="text-gray-300 font-light text-base md:text-lg leading-relaxed flex-grow mb-8">
                            "{{ item.content }}"
                        </p>
                        <div class="flex items-center gap-4 mt-auto">
                            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-brand-green/20 to-brand-cyan/20 border border-white/10 flex items-center justify-center">
                                <span class="text-white font-bold">{{ item.name.charAt(0) }}</span>
                            </div>
                            <div>
                                <h4 class="text-white font-semibold tracking-wide">{{ item.name }}</h4>
                                <p class="text-xs md:text-sm text-gray-500 font-mono mt-1">{{ item.role }} @ <span class="text-brand-green">{{ item.company }}</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>
</template>

<style scoped>
/* Infinite Marquee Animations */
.marquee-left {
    animation: scroll-left 40s linear infinite;
    will-change: transform;
    transform: translateZ(0);
}

.marquee-right {
    /* To scroll right natively, we start from a negative translate and go to 0 */
    animation: scroll-right 40s linear infinite;
    will-change: transform;
    transform: translateZ(0);
}

/* Pause animation on hover */
.hover-pause:hover {
    animation-play-state: paused;
}

@keyframes scroll-left {
    0% {
        transform: translateX(0);
    }
    100% {
        /* Translate left by exactly one set of the items (-33.33% because we duplicate 3 times) */
        transform: translateX(calc(-33.33333%));
    }
}

@keyframes scroll-right {
    0% {
        transform: translateX(calc(-33.33333%));
    }
    100% {
        transform: translateX(0);
    }
}
</style>