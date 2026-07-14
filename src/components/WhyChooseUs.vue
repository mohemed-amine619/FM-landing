<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

const sectionRef = ref(null);
const cardsRef = ref<HTMLElement[]>([]);

const reasons = [
    { title: 'Award-Winning Design', desc: 'Crafting digital experiences that feel native, intuitive, and luxurious.', icon: 'ph-medal' },
    { title: 'Zero Latency Architecture', desc: 'Engineered for sub-second load times globally via edge deployment.', icon: 'ph-activity' },
    { title: 'Enterprise Grade Security', desc: 'Bank-level encryption and continuous vulnerability assessment.', icon: 'ph-lock-key' },
    { title: 'Adaptive Scalability', desc: 'Infrastructure that scales automatically from 10 to 10M users.', icon: 'ph-arrows-out' }
];

onMounted(() => {
    gsap.fromTo(cardsRef.value, 
        { y: 60, opacity: 0, scale: 0.95 }, 
        { 
            y: 0, opacity: 1, scale: 1, duration: 0.8, stagger: 0.15, ease: "power4.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 70%" }
        }
    );
});
</script>

<template>
    <section id="why-us" ref="sectionRef" class="py-24 relative z-10 border-y border-white/[0.02] bg-brand-dark/40 backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight">Why <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Work With Me</span></h2>
                <p class="text-slate-400 font-sans text-lg font-light max-w-2xl mx-auto">I don't just write code. I architect solutions that give your business an unfair advantage.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div v-for="(reason, index) in reasons" :key="index" ref="cardsRef"
                    class="glass-card p-6 rounded-2xl group overflow-hidden relative">
                    <div class="absolute inset-0 bg-gradient-to-br from-brand-cyan/5 to-brand-green/5 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
                    <div class="w-12 h-12 rounded-full bg-white/[0.03] border border-white/[0.05] flex items-center justify-center mb-6 group-hover:bg-brand-cyan/20 group-hover:border-brand-cyan/50 transition-all duration-500">
                        <i :class="['ph', reason.icon, 'text-2xl text-brand-cyan']"></i>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-2">{{ reason.title }}</h3>
                    <p class="text-sm text-slate-400 leading-relaxed">{{ reason.desc }}</p>
                </div>
            </div>
        </div>
    </section>
</template>
