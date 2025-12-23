import os
from dotenv import load_dotenv
from supabase import create_client
from utils.mail_generator import create_inbox_hook, generate_newsletter_html
from datetime import datetime, timedelta

# Load ENV and Init Supabase
# Tell dotenv to look one folder up for the .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

supabase = create_client(os.getenv("PUBLIC_SUPABASE_URL"), os.getenv("PUBLIC_SUPABASE_ANON_KEY"))

def process_weekly_newsletter():
    # 1. Calculate the time range (Last 7 days)
    last_week = (datetime.now() - timedelta(days=7)).isoformat()
    
    # 2. Fetch from Supabase
    response = supabase.table("archives")\
        .select("title, summary, url, tag")\
        .gte("created_at", last_week)\
        .order("created_at", desc=True)\
        .limit(5)\
        .execute()
    
    articles = response.data
    
    if not articles:
        print("No new articles to send this week.")
        return

    # 3. Generate Content
    week_label = f"The Pulse: Week of {datetime.now().strftime('%B %d')}"
    subject, preheader_html = create_inbox_hook(articles[0]['title'], articles[0]['summary'])
    body_html = preheader_html + generate_newsletter_html(articles, week_label)
    
    # 4. Trigger Email (Example using Resend/SendGrid)
    print(f"Newsletter Ready: {subject}")
    # send_email(to="subscribers@list.com", subject=subject, html=body_html)

if __name__ == "__main__":
    process_weekly_newsletter()

# Temporary testing block
if __name__ == "__main__":
    # Mock data to simulate Supabase results
    test_articles = [{
        "title": "Testing the Agentic Hub Newsletter",
        "tag": "Research",
        "summary": "This is a test summary to verify the layout and typography of our new newsletter design.",
        "url": "http://localhost:4321/pulse"
    }]
    
    # Generate the HTML
    html_output = generate_newsletter_html(test_articles, "Test Week 01")
    
    # Save to a local file
    with open("email_preview.html", "w") as f:
        f.write(html_output)
    
    print("Preview generated! Open 'email_preview.html' in your browser.")