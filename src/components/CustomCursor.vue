<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

const cursorRef = ref<HTMLElement | null>(null);
const cursorDotRef = ref<HTMLElement | null>(null);

let mouseX = 0;
let mouseY = 0;

const onMouseMove = (e: MouseEvent) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    gsap.to(cursorRef.value, {
        x: mouseX - 16, // Center offset
        y: mouseY - 16,
        duration: 1.2,
        ease: 'power3.out'
    });

    gsap.to(cursorDotRef.value, {
        x: mouseX - 4,
        y: mouseY - 4,
        duration: 0.1,
        ease: 'power3.out'
    });
};

const onMouseEnterHoverable = () => {
    gsap.to(cursorRef.value, { scale: 2, backgroundColor: 'rgba(4,154,181,0.1)', borderColor: 'rgba(4,154,181,0.5)', duration: 0.3 });
};

const onMouseLeaveHoverable = () => {
    gsap.to(cursorRef.value, { scale: 1, backgroundColor: 'transparent', borderColor: 'rgba(255,255,255,0.2)', duration: 0.3 });
};

onMounted(() => {
    window.addEventListener('mousemove', onMouseMove);
    
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
        <div ref="cursorRef" class="absolute top-0 left-0 w-8 h-8 rounded-full border border-white/20 transition-colors backdrop-blur-[2px]"></div>
        <div ref="cursorDotRef" class="absolute top-0 left-0 w-2 h-2 rounded-full bg-brand-cyan drop-shadow-[0_0_5px_rgba(4,154,181,1)]"></div>
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
