<script setup lang="ts">
interface TechItem {
    name: string;
    icon: string;
    color: string;
}

const techStack: TechItem[] = [
    { name: 'Vue.js', icon: 'ph-file-vue', color: '#42b883' },
    { name: 'React', icon: 'ph-atom', color: '#61dafb' },
    { name: 'Tailwind', icon: 'ph-wind', color: '#38bdf8' },
    { name: 'Node.js', icon: 'ph-terminal-window', color: '#68a063' },
    { name: 'Python', icon: 'ph-file-py', color: '#3776ab' },
    { name: 'AWS', icon: 'ph-cloud', color: '#ff9900' },
    { name: 'Docker', icon: 'ph-shipping-container', color: '#2496ed' },
    { name: 'TypeScript', icon: 'ph-code-simple', color: '#3178c6' },
    { name: 'Laravel', icon: 'ph-hard-drive', color: '#ff2d20' },
    { name: 'Figma', icon: 'ph-figma-logo', color: '#f24e1e' },
    { name: 'Kubernetes', icon: 'ph-cube', color: '#326ce5' },
    { name: 'OpenAI', icon: 'ph-robot', color: '#ffffff' }, // White for contrast
    { name: 'GitHub', icon: 'ph-github-logo', color: '#fafafa' },
    { name: 'PostgreSQL', icon: 'ph-database', color: '#336791' },
    { name: 'Flutter', icon: 'ph-device-mobile-camera', color: '#02569b' },
    { name: 'n8n', icon: 'ph-gear', color: '#ff6d5a' },
    { name: 'Zapier', icon: 'ph-plugs-connected', color: '#ff4a00' },
    { name: 'CI/CD', icon: 'ph-git-branch', color: '#f59e0b' },
    { name: 'PageSpeed', icon: 'ph-rocket-launch', color: '#00cba9' }
];
</script>
<template>
    <section id="tech" class="py-12 border-y border-white/5 bg-brand-navy/50 overflow-hidden relative z-10">
        <div class="max-w-7xl mx-auto px-4 mb-8 text-center">
            <h3 class="font-mono text-brand-cyan text-sm tracking-widest uppercase">Powered By Modern Tech</h3>
        </div>

        <div class="relative flex overflow-x-hidden">
            <div class="animate-marquee whitespace-nowrap flex space-x-12 items-center">
                <div v-for="(tech, index) in [...techStack, ...techStack]" :key="index"
                    class="text-2xl font-bold flex items-center space-x-2 transition-transform hover:scale-110"
                    :style="{ color: tech.color }">
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