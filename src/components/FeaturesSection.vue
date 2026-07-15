<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

const sectionRef = ref(null);
const cardsRef = ref<HTMLElement[]>([]);

const features = [
    { title: 'Lightning Fast', desc: 'Built for speed with optimal performance metrics.', icon: 'ph-lightning' },
    { title: 'Secure by Default', desc: 'Enterprise-grade security embedded at the core.', icon: 'ph-shield-check' },
    { title: 'Scalable Architecture', desc: 'Designed to grow seamlessly with your user base.', icon: 'ph-trend-up' }
];

onMounted(() => {
    gsap.fromTo(cardsRef.value, 
        { y: 50, opacity: 0 }, 
        { 
            y: 0, opacity: 1, duration: 1.5, stagger: 0.3, ease: "power3.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 75%" }
        }
    );
});
</script>

<template>
    <section id="features" ref="sectionRef" class="py-24 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div v-for="(feature, index) in features" :key="index" ref="cardsRef"
                    class="glass-card p-8 rounded-2xl group relative overflow-hidden flex flex-col items-center text-center">
                    <div class="w-16 h-16 rounded-full bg-brand-cyan/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-500">
                        <i :class="['ph', feature.icon, 'text-3xl text-brand-cyan']"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3">{{ feature.title }}</h3>
                    <p class="text-slate-400 leading-relaxed">{{ feature.desc }}</p>
                </div>
            </div>
        </div>
    </section>
</template>
