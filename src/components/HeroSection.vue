<script setup lang="ts">
const emit = defineEmits(['scroll-to']);
</script>

<template>
    <section id="home" class="relative z-10 min-h-screen flex items-center justify-center pt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <div class="mb-8 relative inline-block animate-float">
                <div
                    class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3/4 h-3/4 bg-brand-cyan/20 blur-[60px] rounded-full">
                </div>

                <!-- Ensure image.png is in /public -->
                <img src="../../public/logo.svg" alt="Fullstack Master Logo"
                    class="relative z-10 w-full max-w-2xl mx-auto drop-shadow-[0_0_30px_rgba(74,222,128,0.2)]">
            </div>

            <p class="mt-8 max-w-2xl mx-auto text-lg md:text-xl text-gray-400 font-light font-mono">
                Architecting the digital future. We build scalable, high-performance web solutions with cutting-edge
                technology.
            </p>

            <div class="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
                <button @click="$emit('scroll-to', '#services')"
                    class="px-8 py-4 bg-brand-cyan/10 border border-brand-cyan text-brand-cyan hover:bg-brand-cyan hover:text-black font-bold tracking-wide transition-all duration-300 shadow-[0_0_20px_rgba(6,182,212,0.2)] hover:shadow-[0_0_30px_rgba(6,182,212,0.6)] rounded-sm uppercase">
                    Our Services
                </button>
                <button @click="$emit('scroll-to', '#contact')"
                    class="px-8 py-4 border border-gray-700 text-gray-300 hover:border-brand-green hover:text-brand-green font-bold tracking-wide transition-all duration-300 rounded-sm uppercase">
                    Let's Talk Code
                </button>
            </div>
        </div>
    </section>
</template>