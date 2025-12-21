import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY

// Add this temporary log to see if variables are loading
console.log("Supabase URL loaded:", !!supabaseUrl); 

export const supabase = createClient(supabaseUrl, supabaseAnonKey)