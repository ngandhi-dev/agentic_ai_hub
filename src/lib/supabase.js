import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL || 'https://nokustzcyvjrzvfblshh.supabase.co';
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY || 'sb_publishable_763rYqcOXf62GGQTYFCLhw_qPICkVFV';

// Add this temporary log to see if variables are loading
console.log("Supabase URL loaded:", !!supabaseUrl); 

// Log to help debugging in GitHub Actions (optional)
if (!supabaseUrl || !supabaseKey) {
  console.warn("Supabase credentials missing!");
}
if (import.meta.env.PUBLIC_SUPABASE_URL === undefined) {
  console.warn("⚠️ BUILD WARNING: PUBLIC_SUPABASE_URL is undefined. Check GitHub Secrets.");
}
export const supabase = createClient(supabaseUrl, supabaseAnonKey)