<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

const sectionRef = ref(null);
const contentRef = ref(null);

onMounted(() => {
    gsap.fromTo(contentRef.value, 
        { x: -50, opacity: 0 }, 
        { 
            x: 0, opacity: 1, duration: 0.5, ease: "power4.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 75%" }
        }
    );
});
</script>

<template>
    <section id="about" ref="sectionRef" class="py-24 relative z-10 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div ref="contentRef" class="max-w-3xl">
                <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-blue/10 border border-brand-blue/20 text-brand-blue text-sm font-mono mb-6">
                    Mission
                </div>
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-6 tracking-tight">
                    Engineering the <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Future</span> of Digital Infrastructure.
                </h2>
                <p class="text-slate-400 text-lg leading-relaxed mb-8">
                    I believe that technology should empower businesses to reach their highest potential. My mission is to architect and deploy premium, highly scalable software solutions that deliver measurable results and exceptional user experiences.
                </p>
            </div>
        </div>
    </section>
</template>
