<script setup lang="ts">
import { ref } from 'vue';

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
            formStatus.value = 'Message received. We will be in touch shortly.';
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
</script>

<template>
    <section id="contact" class="py-24 relative z-10 overflow-hidden">
        <!-- Background decorative elements -->
        <div class="absolute top-0 right-0 w-96 h-96 bg-brand-cyan/5 blur-[100px] rounded-full pointer-events-none">
        </div>
        <div class="absolute bottom-0 left-0 w-96 h-96 bg-brand-green/5 blur-[100px] rounded-full pointer-events-none">
        </div>

        <div class="max-w-4xl mx-auto px-4 relative z-20">
            <!-- Glass Card -->
            <div class="glass-card rounded-2xl p-8 md:p-12 relative overflow-hidden group">

                <!-- Neon Corner Accents -->
                <div
                    class="absolute top-0 left-0 w-20 h-20 border-t-2 border-l-2 border-brand-cyan rounded-tl-2xl opacity-50 group-hover:opacity-100 transition-opacity">
                </div>
                <div
                    class="absolute bottom-0 right-0 w-20 h-20 border-b-2 border-r-2 border-brand-green rounded-br-2xl opacity-50 group-hover:opacity-100 transition-opacity">
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-5 gap-12">

                    <!-- Left Side: Call to Action -->
                    <div class="lg:col-span-2 flex flex-col justify-center text-left">
                        <div
                            class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-green/10 border border-brand-green/20 text-brand-green text-xs font-mono mb-6 w-fit">
                            <span class="relative flex h-2 w-2">
                                <span
                                    class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                                <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                            </span>
                            Accepting New Projects
                        </div>

                        <h2 class="text-3xl md:text-4xl font-bold text-white mb-4 leading-tight">
                            Start Your Next <br />
                            <span
                                class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-green">Big
                                Project</span>
                        </h2>

                        <p class="text-gray-400 mb-8 leading-relaxed">
                            Ready to scale? We bridge the gap between complex requirements and elegant, high-performance
                            code.
                        </p>

                        <div class="flex items-center gap-3 text-sm text-gray-500 font-mono">
                            <i class="ph ph-clock text-brand-cyan text-lg"></i>
                            <span>Avg. Response time: &lt; 24h</span>
                        </div>
                    </div>

                    <!-- Right Side: The Form -->
                    <form @submit.prevent="submitForm" class="lg:col-span-3 space-y-5">

                        <!-- Name Input -->
                        <div class="relative group/input">
                            <i
                                class="ph ph-user absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                            <input v-model="form.name" type="text" required
                                class="w-full bg-brand-dark/50 border border-gray-700 rounded-lg py-3.5 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan focus:bg-brand-navy/80 transition-all outline-none"
                                placeholder="Your Name">
                        </div>

                        <!-- Email Input -->
                        <div class="relative group/input">
                            <i
                                class="ph ph-envelope absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                            <input v-model="form.email" type="email" required
                                class="w-full bg-brand-dark/50 border border-gray-700 rounded-lg py-3.5 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan focus:bg-brand-navy/80 transition-all outline-none"
                                placeholder="name@company.com">
                        </div>

                        <!-- Message Input -->
                        <div class="relative group/input">
                            <i
                                class="ph ph-chat-text absolute left-4 top-4 text-gray-500 group-focus-within/input:text-brand-cyan transition-colors"></i>
                            <textarea v-model="form.message" rows="4" required
                                class="w-full bg-brand-dark/50 border border-gray-700 rounded-lg py-3.5 pl-12 pr-4 text-white placeholder-gray-600 focus:border-brand-green focus:ring-1 focus:ring-brand-green focus:bg-brand-navy/80 transition-all outline-none resize-none"
                                placeholder="Tell us about your project goals..."></textarea>
                        </div>

                        <!-- Submit Button -->
                        <button type="submit" :disabled="isLoading"
                            class="group relative w-full py-4 bg-gradient-to-r from-brand-cyan via-brand-blue to-brand-cyan bg-[length:200%_auto] text-white font-bold uppercase tracking-widest rounded-lg overflow-hidden transition-all hover:bg-[100%_center] hover:shadow-[0_0_20px_rgba(6,182,212,0.4)] disabled:opacity-70 disabled:cursor-not-allowed">

                            <span class="relative z-10 flex items-center justify-center gap-2">
                                <i v-if="isLoading" class="ph ph-spinner animate-spin text-xl"></i>
                                <span v-else>Ignite Your Project</span>
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
                            class="text-center p-3 rounded-lg border font-mono text-sm flex items-center justify-center gap-2 animate-fade-in">
                            <i :class="formStatusType === 'success' ? 'ph-check-circle' : 'ph-warning-circle'"
                                class="ph text-lg"></i>
                            {{ formStatus }}
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.glass-card {
    background: rgba(11, 18, 33, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

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