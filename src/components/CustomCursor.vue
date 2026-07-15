<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

const cursorRef = ref<HTMLElement | null>(null);
const cursorDotRef = ref<HTMLElement | null>(null);

let xTo: any;
let yTo: any;
let xDotTo: any;
let yDotTo: any;

const onMouseMove = (e: MouseEvent) => {
    // gsap.quickTo is infinitely faster than gsap.to for mouse tracking
    if (xTo && yTo && xDotTo && yDotTo) {
        xTo(e.clientX - 16);
        yTo(e.clientY - 16);
        xDotTo(e.clientX - 4);
        yDotTo(e.clientY - 4);
    }
};

const onMouseEnterHoverable = () => {
    gsap.to(cursorRef.value, { scale: 2, backgroundColor: 'rgba(4,154,181,0.1)', borderColor: 'rgba(4,154,181,0.5)', duration: 0.3 });
};

const onMouseLeaveHoverable = () => {
    gsap.to(cursorRef.value, { scale: 1, backgroundColor: 'transparent', borderColor: 'rgba(255,255,255,0.2)', duration: 0.3 });
};

onMounted(() => {
    // Initialize quickTo for maximum FPS
    xTo = gsap.quickTo(cursorRef.value, "x", { duration: 0.4, ease: "power3.out" });
    yTo = gsap.quickTo(cursorRef.value, "y", { duration: 0.4, ease: "power3.out" });
    xDotTo = gsap.quickTo(cursorDotRef.value, "x", { duration: 0.1, ease: "power3.out" });
    yDotTo = gsap.quickTo(cursorDotRef.value, "y", { duration: 0.1, ease: "power3.out" });

    window.addEventListener('mousemove', onMouseMove, { passive: true });
    
    // Add hover effect to all buttons and links
    document.querySelectorAll('a, button, input, textarea, .glass-card').forEach(el => {
        el.addEventListener('mouseenter', onMouseEnterHoverable);
        el.addEventListener('mouseleave', onMouseLeaveHoverable);
    });
});

onUnmounted(() => {
    window.removeEventListener('mousemove', onMouseMove);
    document.querySelectorAll('a, button, input, textarea, .glass-card').forEach(el => {
        el.removeEventListener('mouseenter', onMouseEnterHoverable);
        el.removeEventListener('mouseleave', onMouseLeaveHoverable);
    });
});
</script>

<template>
    <div class="pointer-events-none fixed inset-0 z-[9999] overflow-hidden hidden md:block">
        <div ref="cursorRef" class="absolute top-0 left-0 w-8 h-8 rounded-full border border-white/20 transition-colors transform-gpu"></div>
        <div ref="cursorDotRef" class="absolute top-0 left-0 w-2 h-2 rounded-full bg-brand-cyan shadow-[0_0_10px_rgba(4,154,181,0.8)] transform-gpu"></div>
    </div>
</template>

<style>
/* Hide default cursor on desktop */
@media (pointer: fine) {
    body {
        cursor: none;
    }
    a, button, input, textarea {
        cursor: none;
    }
}
</style>
