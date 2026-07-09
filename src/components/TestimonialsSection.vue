<script setup lang="ts">
interface Testimonial {
    name: string;
    role: string;
    company: string;
    content: string;
    rating: number;
}

const testimonials: Testimonial[] = [
    {
        name: 'James Caldoni',
        role: 'CTO',
        company: 'FinStack Global',
        content: 'I have worked with dozens of agencies, but Fullstack Master is different. Their code quality is cleaner than our in-house team. They didn\'t just build what we asked; they optimized our entire architecture for scale.',
        rating: 5
    },
    {
        name: 'Sarah Chen',
        role: 'Product Lead',
        company: 'Orbit SaaS',
        content: 'Deadlines are sacred to them. We launched our platform two weeks ahead of schedule. The Vue.js frontend is buttery smooth, and user retention has jumped 40% since the redesign.',
        rating: 5
    },
    {
        name: 'Michael Ross',
        role: 'Founder',
        company: 'AutoFlow Systems',
        content: 'We were drowning in manual data entry. The automation workflows they built with Python and n8n saved us roughly $120k/year in operational costs. It is not just code; it is smart business logic.',
        rating: 5
    },
    {
        name: 'Elena V.',
        role: 'CEO',
        company: 'GreenScale',
        content: 'They took our messy MVP and turned it into an enterprise-grade Laravel application. Security, performance, and scalability were handled perfectly. Investors were impressed during due diligence.',
        rating: 5
    },
    {
        name: 'David K.',
        role: 'Director',
        company: 'LuxeCommerce',
        content: 'Speed equals revenue. After they optimized our Core Web Vitals and server response times, our conversion rate increased by 25% overnight. Best investment we have made this year.',
        rating: 5
    },
    {
        name: 'Amara Singh',
        role: 'Head of Ops',
        company: 'Nexus Logistics',
        content: 'Communication was flawless. Daily updates, transparent workflows, and zero technical jargon. They felt like a true partner, not just hired hands. We are already planning Phase 2.',
        rating: 5
    }
];
</script>

<template>
    <section id="testimonials" class="py-24 relative z-10 overflow-hidden">

        <!-- Background Atmosphere (Glowing Orbs) -->
        <div class="absolute inset-0 pointer-events-none opacity-40">
            <div
                class="absolute top-20 left-0 w-[500px] h-[500px] bg-brand-cyan/5 rounded-full blur-[100px] -translate-x-1/2">
            </div>
            <div
                class="absolute bottom-20 right-0 w-[500px] h-[500px] bg-brand-green/5 rounded-full blur-[100px] translate-x-1/2">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

            <!-- Section Header -->
            <div class="text-center mb-16 relative">
                <div class="inline-block relative">
                    <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">/</span> Client Intel
                    </h2>
                </div>
                <p class="text-slate-400 font-sans text-lg mt-4 max-w-2xl mx-auto font-light">
                    Transmission logs from secured enterprise collaborations. <br class="hidden md:block" />
                    <span class="text-brand-cyan text-sm mt-2 block font-medium">Status: 100% Satisfied</span>
                </p>
            </div>

            <!-- Testimonials Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
                <div v-for="(item, index) in testimonials" :key="index"
                    class="glass-card p-8 rounded-2xl relative group flex flex-col h-full overflow-hidden">

                    <!-- Top Gradient Line -->
                    <div
                        class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-brand-cyan/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                    </div>

                    <!-- Decorative Quote Icon (Background Watermark) -->
                    <div
                        class="absolute -top-4 -right-4 text-8xl text-white/[0.02] font-serif leading-none select-none pointer-events-none group-hover:text-brand-cyan/[0.05] transition-colors duration-500">
                        "
                    </div>

                    <!-- Stars -->
                    <div class="flex gap-1 mb-6 relative z-10">
                        <i v-for="n in 5" :key="n" class="ph-fill ph-star text-sm transition-colors duration-300"
                            :class="n <= item.rating ? 'text-brand-cyan drop-shadow-[0_0_8px_rgba(4,154,181,0.4)]' : 'text-gray-800'">
                        </i>
                    </div>

                    <!-- Content -->
                    <div class="flex-grow relative z-10">
                        <p
                            class="text-gray-300 leading-relaxed font-light text-lg group-hover:text-white transition-colors duration-300">
                            "{{ item.content }}"
                        </p>
                    </div>

                    <!-- Author Info -->
                    <div
                        class="flex items-center gap-4 mt-8 pt-6 border-t border-white/[0.05] relative z-10 transition-colors">
                        <!-- Avatar / Initials -->
                        <div
                            class="w-12 h-12 rounded-full bg-black/50 border border-white/10 flex items-center justify-center relative overflow-hidden group-hover:border-brand-cyan/50 transition-colors">
                            <span class="text-brand-cyan font-medium font-sans text-lg relative z-10">{{
                                item.name.charAt(0) }}</span>
                        </div>

                        <div>
                            <h4 class="text-white font-semibold text-sm tracking-wide">{{ item.name }}</h4>
                            <p class="text-xs text-gray-400 font-sans font-light mt-0.5">{{ item.role }} <span
                                    class="text-gray-600">@</span> {{ item.company }}</p>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>
</template>

<style scoped>
/* Scoped styles omitted, using global glass-card */
</style>