<script setup lang="ts">
import { onMounted } from 'vue';
import gsap from 'gsap';

onMounted(() => {
    // Animate the gradient orbs smoothly with GSAP
    gsap.utils.toArray('.bg-orb').forEach((orb: any, i: number) => {
        gsap.to(orb, {
            x: () => gsap.utils.random(-200, 200),
            y: () => gsap.utils.random(-200, 200),
            rotation: () => gsap.utils.random(0, 360),
            duration: gsap.utils.random(15, 25),
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut",
            delay: i * -2,
        });
    });
});
</script>

<template>
    <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden bg-brand-dark">
        <!-- Aurora Gradient Mesh -->
        <div class="absolute inset-0 opacity-40">
            <!-- Orb 1: Cyan -->
            <div
                class="bg-orb absolute top-[-10%] left-[-10%] w-[60%] h-[60%] rounded-full transform-gpu"
                style="background: radial-gradient(circle, rgba(4,154,181,0.2) 0%, transparent 60%);">
            </div>
            <!-- Orb 2: Green -->
            <div
                class="bg-orb absolute bottom-[-10%] right-[-10%] w-[70%] h-[70%] rounded-full transform-gpu"
                style="background: radial-gradient(circle, rgba(37,220,125,0.15) 0%, transparent 60%);">
            </div>
            <!-- Orb 3: Blue -->
            <div
                class="bg-orb absolute top-[40%] right-[10%] w-[50%] h-[50%] rounded-full transform-gpu"
                style="background: radial-gradient(circle, rgba(4,145,195,0.2) 0%, transparent 60%);">
            </div>
            <!-- Orb 4: Second Green -->
            <div
                class="bg-orb absolute bottom-[20%] left-[20%] w-[45%] h-[45%] rounded-full transform-gpu"
                style="background: radial-gradient(circle, rgba(7,199,85,0.15) 0%, transparent 60%);">
            </div>
        </div>

        <!-- Removed noise overlay to fix PC lag -->
    </div>
</template>
