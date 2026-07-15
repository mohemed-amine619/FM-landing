<script setup lang="ts">
import { onMounted, ref } from 'vue';
import gsap from 'gsap';

const preloaderRef = ref(null);
const logoRef = ref(null);
const progressRef = ref(null);
const emit = defineEmits(['loaded']);

onMounted(() => {
    const tl = gsap.timeline({
        onComplete: () => {
            emit('loaded');
            gsap.to(preloaderRef.value, { yPercent: -100, duration: 0.4, ease: 'power4.inOut' });
        }
    });

    // Logo pulse and progress bar fill
    tl.to(logoRef.value, { scale: 1.1, duration: 0.5, ease: 'power2.out' })
      .to(progressRef.value, { width: '100%', duration: 0.5, ease: 'power2.inOut' }, '<')
      .to(logoRef.value, { scale: 0, opacity: 0, duration: 1.0, ease: 'back.in(1.5)' }, '+=0.2');
});
</script>

<template>
    <div ref="preloaderRef" class="fixed inset-0 z-[100] bg-brand-dark flex flex-col items-center justify-center">
        <div ref="logoRef" class="w-24 h-24 mb-8">
            <img src="/logo.svg" alt="Loading" class="w-full h-full object-contain filter" />
        </div>
        <div class="w-48 h-1 bg-white/[0.05] rounded-full overflow-hidden">
            <div ref="progressRef" class="h-full w-0 bg-gradient-to-r from-brand-cyan to-brand-green"></div>
        </div>
    </div>
</template>
