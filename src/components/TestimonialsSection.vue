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
        name: 'Tarik M.',
        role: 'Directeur Général',
        company: 'Algiers',
        content: 'Le système ERP sur mesure développé pour notre entreprise de plus de 40 employés a été une véritable révolution. Il a parfaitement rationalisé nos opérations internes et considérablement optimisé notre gestion quotidienne.',
        rating: 5
    },
    {
        name: 'Amine B.',
        role: 'Fondateur de Startup',
        company: 'Oran',
        content: 'L\'intégration de l\'API backend est d\'une fluidité remarquable. Le système de traitement sécurisé des paiements locaux via CIB et EDAHABIA fonctionne sans la moindre faille. Un travail d\'architecture de très haut niveau.',
        rating: 5
    },
    {
        name: 'Karim S.',
        role: 'Trader Indépendant',
        company: 'Constantine',
        content: 'Le bot Python créé sur mesure pour mon terminal MetaTrader 5 est d\'une précision redoutable. L\'exécution de mes stratégies algorithmiques sur le XAUUSD et le BTCUSDm est ultra-rapide et parfaitement fiable.',
        rating: 5
    },
    {
        name: 'Lydia A.',
        role: 'Fondatrice d\'Agence Tech',
        company: 'Algiers',
        content: 'Nous sommes ravis de la livraison de notre nouveau tableau de bord. L\'interface est rapide, moderne et le résultat est totalement pixel-perfect. L\'expertise sur Vue.js et Tailwind CSS est indéniable.',
        rating: 5
    },
    {
        name: 'Yassine D.',
        role: 'Directeur Technique',
        company: 'Algiers',
        content: 'La migration de notre infrastructure vers le cloud a été gérée de main de maître. La plateforme gère désormais des pics de trafic massifs sans aucun ralentissement.',
        rating: 5
    },
    {
        name: 'Nadia F.',
        role: 'CEO',
        company: 'Annaba',
        content: 'Le système d\'analyse de données personnalisé qu\'ils ont conçu nous permet de prendre des décisions stratégiques en temps réel. L\'architecture backend est extrêmement robuste.',
        rating: 5
    }
];
</script>

<template>
    <section id="testimonials" class="py-24 relative z-10 overflow-hidden">

        <!-- Background Atmosphere (Glowing Orbs) -->
        <div class="absolute inset-0 pointer-events-none opacity-80 mix-blend-screen">
            <div
                class="absolute top-20 left-0 w-[500px] h-[500px] bg-brand-cyan/20 rounded-full blur-[120px] -translate-x-1/2 animate-pulse-glow">
            </div>
            <div
                class="absolute bottom-20 right-0 w-[500px] h-[500px] bg-brand-green/20 rounded-full blur-[120px] translate-x-1/2 animate-pulse-glow" style="animation-delay: 1.5s;">
            </div>
            <div
                class="absolute top-1/2 left-1/2 w-[800px] h-[300px] bg-brand-purple/10 rounded-full blur-[150px] -translate-x-1/2 -translate-y-1/2 animate-pulse-slow pointer-events-none">
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