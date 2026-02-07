<script setup lang="ts">
interface TechItem {
    name: string;
    icon: string;
}

const techStack: TechItem[] = [
    { name: 'Vue.js', icon: 'ph-vue-logo' },
    { name: 'React', icon: 'ph-atom' },
    { name: 'Tailwind', icon: 'ph-wind' },
    { name: 'Node.js', icon: 'ph-terminal-window' },
    { name: 'Python', icon: 'ph-snake' },
    { name: 'AWS', icon: 'ph-cloud' },
    { name: 'Docker', icon: 'ph-container-ship' },
    { name: 'TypeScript', icon: 'ph-code-simple' },
];
</script>

<template>
    <section id="tech" class="py-12 border-y border-white/5 bg-brand-navy/50 overflow-hidden relative z-10">
        <div class="max-w-7xl mx-auto px-4 mb-8 text-center">
            <h3 class="font-mono text-brand-cyan text-sm tracking-widest uppercase">Powered By Modern Tech</h3>
        </div>

        <!-- Infinite Scroll Container -->
        <div class="relative flex overflow-x-hidden group">
            <!-- 
           The 'animate-marquee' class is defined in your tailwind.config.js 
           We use 'hover:pause' to stop the scroll when the user hovers over it.
      -->
            <div class="animate-marquee whitespace-nowrap flex space-x-12 items-center hover:pause">
                <!-- First Set -->
                <div v-for="tech in techStack" :key="tech.name"
                    class="text-2xl font-bold text-gray-600 hover:text-white transition-colors flex items-center space-x-2">
                    <i :class="['ph', tech.icon]"></i>
                    <span>{{ tech.name }}</span>
                </div>

                <!-- Second Set (Duplicate for seamless loop) -->
                <div v-for="tech in techStack" :key="`${tech.name}-duplicate`"
                    class="text-2xl font-bold text-gray-600 hover:text-white transition-colors flex items-center space-x-2">
                    <i :class="['ph', tech.icon]"></i>
                    <span>{{ tech.name }}</span>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
/* Optional: Pause the animation when hovering */
.hover\:pause:hover {
    animation-play-state: paused;
}
</style>