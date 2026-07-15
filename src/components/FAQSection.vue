<script setup lang="ts">
import { ref, onMounted } from 'vue';
import gsap from 'gsap';

const faqs = [
    {
        question: 'What technologies do you use?',
        answer: 'I specialize in a modern, scalable stack including Vue.js, React, Node.js, Python, Laravel, and Go. My infrastructure is typically deployed on AWS or GCP using Docker and Kubernetes.'
    },
    {
        question: 'How long does a typical project take?',
        answer: 'Depending on the complexity, an MVP or first phase typically takes 8 to 12 weeks. I use agile methodologies to deliver functional iterations quickly.'
    },
    {
        question: 'Do you offer post-launch support?',
        answer: 'Absolutely. I offer dedicated SLAs to ensure your infrastructure remains secure, updated, and highly performant at all times.'
    },
    {
        question: 'How do you handle security?',
        answer: 'Security is embedded at the architectural level. I implement end-to-end encryption, follow OWASP best practices, and ensure full GDPR/local compliance depending on your operating region.'
    }
];

const activeIndex = ref<number | null>(0);

const toggleFaq = (index: number) => {
    activeIndex.value = activeIndex.value === index ? null : index;
};

const sectionRef = ref(null);
const faqItemsRef = ref<HTMLElement[]>([]);

onMounted(() => {
    gsap.fromTo(faqItemsRef.value, 
        { y: 30, opacity: 0 },
        { 
            y: 0, opacity: 1, duration: 0.4, stagger: 0.055, ease: 'power3.out',
            scrollTrigger: { trigger: sectionRef.value, start: 'top 80%' }
        }
    );
});
</script>

<template>
    <section id="faq" ref="sectionRef" class="py-24 relative z-10">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight">Frequently Asked <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Questions</span></h2>
                <p class="text-slate-400 font-sans text-lg font-light">Everything you need to know about working with me.</p>
            </div>

            <div class="space-y-4">
                <div v-for="(faq, index) in faqs" :key="index" ref="faqItemsRef"
                    class="glass-card rounded-2xl overflow-hidden transition-all duration-300"
                    :class="activeIndex === index ? 'border-brand-cyan/40 bg-white/[0.04]' : 'border-white/[0.05] bg-white/[0.02]'">
                    
                    <button @click="toggleFaq(index)" class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none">
                        <span class="font-medium text-white text-lg">{{ faq.question }}</span>
                        <div class="flex-shrink-0 ml-4 w-8 h-8 rounded-full border border-white/10 flex items-center justify-center transition-transform duration-300"
                            :class="activeIndex === index ? 'rotate-180 bg-brand-cyan/20 text-brand-cyan border-brand-cyan/50' : 'text-gray-400'">
                            <i class="ph" :class="activeIndex === index ? 'ph-minus' : 'ph-plus'"></i>
                        </div>
                    </button>
                    
                    <div class="px-6 overflow-hidden transition-all duration-500 max-h-0"
                        :style="{ maxHeight: activeIndex === index ? '200px' : '0px', opacity: activeIndex === index ? 1 : 0, paddingBottom: activeIndex === index ? '1.5rem' : '0px' }">
                        <p class="text-slate-400 leading-relaxed">{{ faq.answer }}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
