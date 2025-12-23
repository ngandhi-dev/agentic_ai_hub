// src/pages/api/send-test.ts
import type { APIRoute } from 'astro';

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();
    const { html, subject } = body;
    // Use import.meta.env for Astro env variables
    const apiKey = import.meta.env.RESEND_API_KEY;
    if (!apiKey) {
      console.error("❌ API Key Missing in Server Environment");
      return new Response(JSON.stringify({ error: 'Server configuration error: Missing API Key' }), { status: 500 });
    }
    // Replace this with your actual Email Provider API call (Example: Resend)
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${import.meta.env.RESEND_API_KEY}`,
      },
      body: JSON.stringify({
        from: 'Agentic Pulse <onboarding@resend.dev>',
        to: ['nehag16@gmail.com'], // Hardcoded for safety
        subject: `[TEST] ${subject}`,
        html: html,
      }),
    });

    if (response.ok) {
      return new Response(JSON.stringify({ message: 'Email sent!' }), { status: 200 });
    } else {
      return new Response(JSON.stringify({ error: 'Failed to send' }), { status: 500 });
    }
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 500 });
  }
};