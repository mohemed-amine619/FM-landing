<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

const sectionRef = ref(null);
const numbersRef = ref<HTMLElement[]>([]);

const stats = [
    { label: 'Global Clients', value: 35, suffix: '+', prefix: '' },
    { label: 'Enterprise Systems Architected', value: 120, suffix: '', prefix: '' },
    { label: 'API Requests Scaled', value: 250, suffix: 'M+', prefix: '' },
    { label: 'System Uptime', value: 99.99, suffix: '%', prefix: '' }
];

onMounted(() => {
    // Reveal animation
    gsap.fromTo(sectionRef.value, 
        { opacity: 0, y: 30 },
        { opacity: 1, y: 0, duration: 1.5, ease: 'power3.out', scrollTrigger: { trigger: sectionRef.value, start: 'top 85%' } }
    );

    // Number counting animation
    numbersRef.value.forEach((el, index) => {
        const targetValue = stats[index].value;
        const isFloat = !Number.isInteger(targetValue);
        
        gsap.to(el, {
            innerHTML: targetValue,
            duration: 2.5,
            ease: "power2.out",
            snap: { innerHTML: isFloat ? 0.01 : 1 },
            scrollTrigger: {
                trigger: sectionRef.value,
                start: "top 80%"
            }
        });
    });
});
</script>

<template>
    <section id="stats" ref="sectionRef" class="py-16 relative z-10 border-y border-white/[0.05] bg-black/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/[0.05] mb-16">
                <div v-for="(stat, index) in stats" :key="index" class="text-center px-4">
                    <div class="text-3xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-br from-brand-cyan to-brand-green mb-2">
                        {{ stat.prefix }}<span ref="numbersRef">0</span>{{ stat.suffix }}
                    </div>
                    <div class="text-xs md:text-sm font-mono text-gray-500 uppercase tracking-widest">{{ stat.label }}</div>
                </div>
            </div>

        </div>
    </section>
</template>
