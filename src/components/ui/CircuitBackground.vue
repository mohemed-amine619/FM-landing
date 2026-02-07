<script setup lang="ts">
// Pure presentation component
</script>

<template>
    <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        <!-- Top Left Circuit -->
        <svg class="absolute top-0 left-0 w-64 h-64 md:w-96 md:h-96 text-brand-green/20" viewBox="0 0 400 400"
            fill="none" stroke="currentColor" stroke-width="2">
            <path d="M0 50 H50 L80 80 H150 L180 110" class="circuit-line" style="animation-duration: 5s" />
            <circle cx="180" cy="110" r="4" fill="currentColor" />
            <path d="M0 150 H80 L120 190 H200" class="circuit-line" style="animation-duration: 7s" />
            <circle cx="200" cy="190" r="4" fill="currentColor" />
            <path d="M50 0 V50 L80 80 V150" class="circuit-line" style="animation-duration: 6s" />
        </svg>

        <!-- Bottom Right Circuit -->
        <svg class="absolute bottom-0 right-0 w-64 h-64 md:w-96 md:h-96 text-brand-cyan/20 rotate-180"
            viewBox="0 0 400 400" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M0 50 H50 L80 80 H150 L180 110" class="circuit-line" style="animation-duration: 5s" />
            <circle cx="180" cy="110" r="4" fill="currentColor" />
            <path d="M0 150 H80 L120 190 H200" class="circuit-line" style="animation-duration: 8s" />
            <circle cx="200" cy="190" r="4" fill="currentColor" />
        </svg>

        <!-- Gradient Orbs -->
        <div
            class="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-cyan/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/2">
        </div>
        <div
            class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-brand-green/10 rounded-full blur-[120px] translate-y-1/2 -translate-x-1/2">
        </div>
    </div>
</template>

<style scoped>
.circuit-line {
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
    animation: drawLine 8s linear infinite;
}

@keyframes drawLine {
    to {
        stroke-dashoffset: 0;
    }
}
</style>
