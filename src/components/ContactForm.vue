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

// ---------------------------------------------------------
// CONFIGURATION
// ---------------------------------------------------------
// 1. Go to https://formspree.io/
// 2. Create a new form
// 3. Paste your Form ID here (e.g., "mdoq...")
const FORMSPREE_ID = 'YOUR_FORM_ID_HERE';
const ENDPOINT = `https://formspree.io/f/${FORMSPREE_ID}`;

const submitForm = async () => {
    // Reset status
    formStatus.value = '';
    isLoading.value = true;

    // Validation
    if (FORMSPREE_ID === 'YOUR_FORM_ID_HERE') {
        formStatusType.value = 'error';
        formStatus.value = 'Configuration Error: Please add your Formspree ID in ContactForm.vue';
        isLoading.value = false;
        return;
    }

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
            formStatus.value = 'Transmission Successful. We will contact you shortly.';
            form.value = { name: '', email: '', message: '' }; // Clear form
        } else {
            const data = await response.json();
            throw new Error(data.error || 'Server rejected transmission.');
        }
    } catch (error: any) {
        formStatusType.value = 'error';
        formStatus.value = 'Transmission Failed: ' + error.message;
    } finally {
        isLoading.value = false;

        // Auto-clear success message
        if (formStatusType.value === 'success') {
            setTimeout(() => {
                formStatus.value = '';
            }, 5000);
        }
    }
};
</script>

<template>
    <section id="contact" class="py-24 relative z-10">
        <div class="max-w-4xl mx-auto px-4">
            <!-- Glass Card Container -->
            <div class="glass-card rounded-2xl p-8 md:p-12 border-t-4 border-t-brand-cyan relative overflow-hidden">

                <!-- Header -->
                <div class="text-center mb-12 relative z-10">
                    <h2 class="text-3xl font-bold text-white mb-2">Initialize Connection</h2>
                    <p class="text-gray-400 font-mono">Let's build something extraordinary together.</p>
                </div>

                <!-- Form -->
                <form @submit.prevent="submitForm" class="space-y-6 relative z-10">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- Name Input -->
                        <div class="space-y-2">
                            <label class="text-xs font-mono text-brand-cyan uppercase">Name_ID</label>
                            <input v-model="form.name" type="text" required
                                class="w-full bg-brand-dark/50 border border-gray-700 rounded p-3 text-white focus:border-brand-green focus:outline-none focus:ring-1 focus:ring-brand-green transition-all placeholder-gray-600"
                                placeholder="John Doe">
                        </div>

                        <!-- Email Input -->
                        <div class="space-y-2">
                            <label class="text-xs font-mono text-brand-cyan uppercase">Email_Addr</label>
                            <input v-model="form.email" type="email" required
                                class="w-full bg-brand-dark/50 border border-gray-700 rounded p-3 text-white focus:border-brand-green focus:outline-none focus:ring-1 focus:ring-brand-green transition-all placeholder-gray-600"
                                placeholder="john@example.com">
                        </div>
                    </div>

                    <!-- Message Input -->
                    <div class="space-y-2">
                        <label class="text-xs font-mono text-brand-cyan uppercase">Project_Brief</label>
                        <textarea v-model="form.message" rows="4" required
                            class="w-full bg-brand-dark/50 border border-gray-700 rounded p-3 text-white focus:border-brand-green focus:outline-none focus:ring-1 focus:ring-brand-green transition-all placeholder-gray-600"
                            placeholder="Tell us about your project requirements..."></textarea>
                    </div>

                    <!-- Submit Button -->
                    <button type="submit" :disabled="isLoading"
                        class="w-full py-4 bg-gradient-to-r from-brand-cyan to-brand-blue text-black font-bold uppercase tracking-widest hover:shadow-[0_0_20px_rgba(34,211,238,0.4)] transition-all transform hover:-translate-y-1 rounded-sm disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2">
                        <i v-if="isLoading" class="ph ph-spinner animate-spin text-xl"></i>
                        {{ isLoading ? 'TRANSMITTING...' : 'EXECUTE_TRANSMISSION' }}
                    </button>

                    <!-- Status Message -->
                    <div v-if="formStatus"
                        :class="formStatusType === 'success' ? 'bg-brand-green/10 text-brand-green border-brand-green/20' : 'bg-red-500/10 text-red-400 border-red-500/20'"
                        class="text-center p-3 mt-4 border rounded font-mono text-sm transition-all flex items-center justify-center gap-2">
                        <i :class="formStatusType === 'success' ? 'ph-check-circle' : 'ph-warning-circle'"
                            class="ph text-lg"></i>
                        {{ formStatus }}
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<style scoped>
.glass-card {
    background: rgba(11, 18, 33, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(6, 182, 212, 0.1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
</style>