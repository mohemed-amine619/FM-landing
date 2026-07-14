<script setup lang="ts">
import { ref, onMounted } from 'vue';
import gsap from 'gsap';

// State
const form = ref({
    name: '',
    email: '',
    message: ''
});

const isLoading = ref(false);
const formStatus = ref('');
const formStatusType = ref<'success' | 'error'>('success');

// Configuration
const FORMSPREE_ID = 'xnjbqvnq'; // Your specific ID
const ENDPOINT = `https://formspree.io/f/${FORMSPREE_ID}`;

const submitForm = async () => {
    formStatus.value = '';
    isLoading.value = true;

    try {
        const response = await fetch(ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(form.value)
        });

        if (response.ok) {
            formStatusType.value = 'success';
            formStatus.value = 'Message received. I will be in touch shortly.';
            form.value = { name: '', email: '', message: '' };
        } else {
            const data = await response.json();
            throw new Error(data.error || 'Server rejected transmission.');
        }
    } catch (error: any) {
        formStatusType.value = 'error';
        formStatus.value = 'Transmission Failed: ' + error.message;
    } finally {
        isLoading.value = false;
        if (formStatusType.value === 'success') {
            setTimeout(() => { formStatus.value = ''; }, 5000);
        }
    }
};

const sectionRef = ref(null);
const contentRef = ref(null);

onMounted(() => {
    gsap.fromTo(contentRef.value, 
        { y: 60, opacity: 0, scale: 0.95 }, 
        { 
            y: 0, opacity: 1, scale: 1, duration: 1.0, ease: "power4.out",
            scrollTrigger: { trigger: sectionRef.value, start: "top 75%" }
        }
    );
});
</script>

<template>
    <section id="contact" ref="sectionRef" class="py-24 relative z-10 overflow-hidden">
        <!-- Background decorative elements -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-to-tr from-brand-cyan/20 to-brand-green/20 mix-blend-screen blur-[150px] rounded-full pointer-events-none animate-pulse-glow">
        </div>

        <div class="max-w-4xl mx-auto px-4 relative z-20">
            <!-- Glass Card -->
            <div ref="contentRef" class="glass-card rounded-3xl p-8 md:p-16 relative overflow-hidden group">

                <!-- Elegant Accents -->
                <div
                    class="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-brand-cyan/80 to-transparent opacity-50 group-hover:opacity-100 transition-opacity duration-700">
                </div>

                <div class="flex flex-col items-center justify-center text-center mb-12">
                    <div
                        class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-brand-green/10 border border-brand-green/20 text-brand-green text-sm font-mono mb-6 w-fit">
                        <span class="relative flex h-2 w-2">
                            <span
                                class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                        </span>
                        Accepting New Projects
                    </div>

                    <h2 class="text-4xl md:text-6xl font-bold text-white mb-6 leading-tight tracking-tight">
                        Start Your Next <br />
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Enterprise Project</span>
                    </h2>

                    <p class="text-slate-400 leading-relaxed text-lg max-w-2xl">
                        Ready to scale? I bridge the gap between complex requirements and elegant, high-performance code.
                    </p>
                </div>

                <!-- The Form -->
                <form @submit.prevent="submitForm" class="max-w-2xl mx-auto space-y-6">

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- Name Input -->
                        <div class="relative group/input">
                            <i
                                class="ph ph-user absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                            <input v-model="form.name" type="text" required
                                class="w-full bg-black/40 border border-white/10 rounded-xl py-4 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-cyan/50 focus:ring-1 focus:ring-brand-cyan/50 focus:bg-black/60 transition-all outline-none"
                                placeholder="Full Name">
                        </div>

                        <!-- Email Input -->
                        <div class="relative group/input">
                            <i
                                class="ph ph-envelope absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                            <input v-model="form.email" type="email" required
                                class="w-full bg-black/40 border border-white/10 rounded-xl py-4 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-cyan/50 focus:ring-1 focus:ring-brand-cyan/50 focus:bg-black/60 transition-all outline-none"
                                placeholder="Work Email">
                        </div>
                    </div>

                    <!-- Message Input -->
                    <div class="relative group/input">
                        <i
                            class="ph ph-chat-text absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                        <textarea v-model="form.message" rows="4" required
                            class="w-full bg-black/40 border border-white/10 rounded-xl py-4 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-cyan/50 focus:ring-1 focus:ring-brand-cyan/50 focus:bg-black/60 transition-all outline-none resize-none"
                            placeholder="Detail your project requirements..."></textarea>
                    </div>

                    <!-- Submit Button -->
                    <button type="submit" :disabled="isLoading"
                        class="glow-button-primary w-full rounded-xl py-4 disabled:opacity-70 disabled:cursor-not-allowed group">

                        <span class="relative z-10 flex items-center justify-center gap-2 text-lg">
                            <i v-if="isLoading" class="ph ph-spinner animate-spin text-2xl"></i>
                            <span v-else>Request Consultation</span>
                            <i v-if="!isLoading"
                                class="ph ph-arrow-right group-hover:translate-x-1 transition-transform"></i>
                        </span>

                        <!-- Shine Effect -->
                        <div
                            class="absolute inset-0 -translate-x-full group-hover:translate-x-full transition-transform duration-1000 bg-gradient-to-r from-transparent via-white/20 to-transparent skew-x-12">
                        </div>
                    </button>

                    <!-- Status Message -->
                    <div v-if="formStatus"
                        :class="formStatusType === 'success' ? 'bg-brand-green/10 text-brand-green border-brand-green/20' : 'bg-red-500/10 text-red-400 border-red-500/20'"
                        class="text-center p-4 rounded-xl border font-mono text-sm flex items-center justify-center gap-2 animate-fade-in">
                        <i :class="formStatusType === 'success' ? 'ph-check-circle' : 'ph-warning-circle'"
                            class="ph text-xl"></i>
                        {{ formStatus }}
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>